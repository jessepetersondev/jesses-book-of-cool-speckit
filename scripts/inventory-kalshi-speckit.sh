#!/usr/bin/env bash
set -euo pipefail

roots=("$@")
if [[ ${#roots[@]} -eq 0 ]]; then
  roots=(/home/ai /home/ai/clawd/projects)
fi

echo "Observed Kalshi Spec Kit repos"
echo "=============================="

./scripts/inventory-speckit.sh "${roots[@]}" | awk '
  BEGIN {
    keep = 0
  }
  /^Observed Spec Kit repos$/ { next }
  /^=======================$/ { next }
  /^repo: / {
    keep = ($0 ~ /kalshi/)
  }
  {
    if (keep) print
  }
'
