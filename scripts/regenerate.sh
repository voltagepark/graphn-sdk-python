#!/usr/bin/env bash
# Regenerate src/graphn/_generated/ from the public OpenAPI spec.
#
# Source of truth precedence:
#   1. --spec <path-or-url>            explicit override
#   2. $GRAPHN_OPENAPI_SPEC env var    explicit override
#   3. ../takao/svc/graphn-cp/api/openapi.yaml    sibling repo checkout
#   4. https://api.graphn.ai/openapi.yaml         live production spec
#
# Designed to be re-runnable. Wipes and replaces src/graphn/_generated/
# every invocation. Hand-written modules under src/graphn/ are never
# touched.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GENERATED_DIR="${REPO_ROOT}/src/graphn/_generated"
DEFAULT_SIBLING="${REPO_ROOT}/../takao/svc/graphn-cp/api/openapi.yaml"
LIVE_URL="https://api.graphn.ai/openapi.yaml"

spec=""
keep_intermediate=0

usage() {
    cat <<EOF
Usage: $(basename "$0") [--spec <path-or-url>] [--keep-intermediate]

Options:
  --spec <path|url>      Override the OpenAPI spec source.
  --keep-intermediate    Don't delete the openapi-python-client work tree.
  -h, --help             Show this message.

Environment:
  GRAPHN_OPENAPI_SPEC    Same effect as --spec.
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --spec)
            spec="$2"
            shift 2
            ;;
        --keep-intermediate)
            keep_intermediate=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown argument: $1" >&2
            usage >&2
            exit 2
            ;;
    esac
done

if [[ -z "${spec}" && -n "${GRAPHN_OPENAPI_SPEC:-}" ]]; then
    spec="${GRAPHN_OPENAPI_SPEC}"
fi
if [[ -z "${spec}" && -f "${DEFAULT_SIBLING}" ]]; then
    spec="${DEFAULT_SIBLING}"
fi
if [[ -z "${spec}" ]]; then
    spec="${LIVE_URL}"
fi

echo "[regenerate] using spec: ${spec}"

if ! command -v openapi-python-client >/dev/null 2>&1; then
    echo "[regenerate] openapi-python-client not found; install with:" >&2
    echo "             pip install -e '.[dev]'" >&2
    exit 1
fi

WORKDIR="$(mktemp -d -t graphn-openapi-XXXXXX)"
trap '[[ ${keep_intermediate} -eq 0 ]] && rm -rf "${WORKDIR}" || echo "[regenerate] kept intermediate at ${WORKDIR}"' EXIT

# openapi-python-client emits a full package; we only want the typed
# transport layer (models, api, client). The wrapper meta=none mode
# keeps the layout flat.
config_file="${WORKDIR}/config.yaml"
cat >"${config_file}" <<EOF
package_name_override: _graphn_generated
project_name_override: _graphn_generated
use_path_prefixes_for_title_model_names: false
field_constraints: true
EOF

generator_args=(
    --meta=none
    --config "${config_file}"
    --output-path "${WORKDIR}/out"
    --overwrite
)

if [[ "${spec}" == http://* || "${spec}" == https://* ]]; then
    openapi-python-client generate --url "${spec}" "${generator_args[@]}"
else
    openapi-python-client generate --path "${spec}" "${generator_args[@]}"
fi

if [[ ! -d "${WORKDIR}/out" ]]; then
    echo "[regenerate] expected ${WORKDIR}/out to exist after generation" >&2
    exit 1
fi

rm -rf "${GENERATED_DIR}"
mkdir -p "${GENERATED_DIR}"
# The generator writes into a flat directory when meta=none; copy the
# entire tree back in.
cp -R "${WORKDIR}/out/." "${GENERATED_DIR}/"

cat >"${GENERATED_DIR}/__init__.py" <<'PYEOF'
"""Generated transport layer.

This package is overwritten by ``scripts/regenerate.sh``. Do NOT edit
by hand — changes will be lost on the next regeneration.
"""
PYEOF

echo "[regenerate] wrote ${GENERATED_DIR}"
echo "[regenerate] review with: git status src/graphn/_generated"
