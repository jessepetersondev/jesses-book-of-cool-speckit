#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 /path/to/repo" >&2
  exit 1
fi

repo="$1"

required_files=(
  ".specify/init-options.json"
  ".specify/integrations/codex.manifest.json"
  ".agents/skills/speckit-implement/SKILL.md"
)

missing=0
for rel in "${required_files[@]}"; do
  if [[ ! -f "$repo/$rel" ]]; then
    echo "missing: $repo/$rel"
    missing=1
  else
    echo "ok: $repo/$rel"
  fi
done

if [[ -d "$repo/specs" ]]; then
  echo "features:"
  find "$repo/specs" -maxdepth 2 -mindepth 2 -type f -name spec.md 2>/dev/null \
    | sed "s#^$repo/specs/##; s#/spec.md##" \
    | sort
else
  echo "features: none"
fi

version="$(grep -m1 '"speckit_version"' "$repo/.specify/init-options.json" 2>/dev/null | sed -E 's/.*"([^"]+)".*/\1/' || true)"
[[ -n "$version" ]] || version="unknown"
echo "speckit_version: $version"

if [[ $missing -ne 0 ]]; then
  exit 1
fi
