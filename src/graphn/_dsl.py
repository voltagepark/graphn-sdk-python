"""Minimal DSL readers used by workflow create/update auto-link.

The CLI parses with pkg/dsl. We only need the top-level ``agents``,
``functions``, and ``mcp_servers`` maps so we can save_bundle the same
way ``graphn wf create`` does. A full YAML dependency is not worth it
for three mappings of ``name: ref`` entries.
"""

from __future__ import annotations

import re
from typing import Literal

Section = Literal["agents", "functions", "mcp_servers"]

_SECTION_HEADER = re.compile(
    r"^(?P<indent>[ \t]*)(?P<section>agents|functions|mcp_servers):[ \t]*(?:#.*)?$"
)
_ENTRY = re.compile(r"^(?P<indent>[ \t]*)(?P<name>[^\s:#][^:]*?)\s*:\s*(?P<value>.*)$")
_RES_REF = re.compile(r"^res://(?:agents|functions|mcp-servers|mcp_servers)/([^/\s]+)\s*$")


def dsl_resource_refs(dsl: str) -> dict[Section, dict[str, str]]:
    """Return ``{section: {local_name: ref_string}}`` from workflow DSL."""

    found: dict[Section, dict[str, str]] = {
        "agents": {},
        "functions": {},
        "mcp_servers": {},
    }
    lines = dsl.splitlines()
    i = 0
    while i < len(lines):
        header = _SECTION_HEADER.match(lines[i])
        if header is None:
            i += 1
            continue
        section = header.group("section")
        parent_indent = header.group("indent")
        i += 1
        while i < len(lines):
            raw = lines[i]
            if not raw.strip() or raw.lstrip().startswith("#"):
                i += 1
                continue
            entry = _ENTRY.match(raw)
            if entry is None or len(entry.group("indent")) <= len(parent_indent):
                break
            name = entry.group("name").strip().strip("\"'")
            value = entry.group("value").split("#", 1)[0].strip().strip("\"'")
            found[section][name] = value  # type: ignore[literal-required]
            i += 1
    return found


def resource_id_from_ref(ref: str) -> str | None:
    """Extract ``fn_…`` / ``ag_…`` from a ``res://functions/fn_…`` value."""

    match = _RES_REF.match(ref.strip().strip("\"'"))
    if match is None:
        return None
    return match.group(1)
