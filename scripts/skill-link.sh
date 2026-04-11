#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 /path/to/repo speckit-plan" >&2
  exit 1
fi

repo="$1"
skill="$2"
skill_path="$repo/.agents/skills/$skill/SKILL.md"

if [[ ! -f "$skill_path" ]]; then
  echo "missing skill file: $skill_path" >&2
  exit 1
fi

printf '[$%s](%s)\n' "$skill" "$skill_path"
