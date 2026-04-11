#!/usr/bin/env bash
set -euo pipefail

print_only="false"

if [[ ${1:-} == "--print-only" ]]; then
  print_only="true"
  shift
fi

if [[ $# -ne 1 ]]; then
  echo "usage: $0 [--print-only] /path/to/repo" >&2
  exit 1
fi

repo_path="$1"
cmd=(specify init . --ai codex --ai-skills --force)

echo "repo: $repo_path"
echo "command: ${cmd[*]}"

if [[ "$print_only" == "true" ]]; then
  exit 0
fi

mkdir -p "$repo_path"
cd "$repo_path"
"${cmd[@]}"
