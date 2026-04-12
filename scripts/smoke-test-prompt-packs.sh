#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

./scripts/generate-prompt-pack.sh \
  --workflow greenfield \
  --vars-file examples/SAMPLE-GREENFIELD-VALUES.env \
  --out "$tmp_dir/greenfield-pack.md" >/dev/null

./scripts/generate-prompt-pack.sh \
  --workflow brownfield \
  --vars-file examples/SAMPLE-BROWNFIELD-VALUES.env \
  --out "$tmp_dir/brownfield-pack.md" >/dev/null

./scripts/generate-prompt-pack.sh \
  --workflow phased \
  --vars-file examples/golden/kalshi-quant-dashboard/prompt-pack-values.env \
  --out "$tmp_dir/phased-pack.md" >/dev/null

for pack in "$tmp_dir"/*.md; do
  grep -q '^# Generated Prompt Pack$' "$pack"
  grep -q 'unresolved_placeholders: none' "$pack"
done
