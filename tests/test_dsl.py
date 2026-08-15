"""Tests for the tiny DSL section reader used by workflow auto-link."""

from graphn._dsl import dsl_resource_refs, resource_id_from_ref


def test_dsl_resource_refs_top_level() -> None:
    dsl = """document:
  dsl: "1.0.0"
  name: smoke
functions:
  echo: "res://functions/fn_01"
agents:
  Bot: ""
mcp_servers:
  github: res://mcp-servers/mcp_01
"""
    refs = dsl_resource_refs(dsl)
    assert refs["functions"] == {"echo": "res://functions/fn_01"}
    assert refs["agents"] == {"Bot": ""}
    assert refs["mcp_servers"] == {"github": "res://mcp-servers/mcp_01"}


def test_resource_id_from_ref() -> None:
    assert resource_id_from_ref("res://functions/fn_01") == "fn_01"
    assert resource_id_from_ref("") is None
    assert resource_id_from_ref("echo") is None
