#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

status=0

check_file() {
  local file="$1"
  while IFS=: read -r line target; do
    [[ -n "$target" ]] || continue

    case "$target" in
      http:*|https:*|mailto:*|'#'*|/home/*|/path/*|*'{REPO_PATH}'*)
        continue
        ;;
    esac

    target="${target%%#*}"
    [[ -n "$target" ]] || continue

    local resolved
    resolved="$(realpath -m "$(dirname "$file")/$target")"
    if [[ ! -e "$resolved" ]]; then
      printf 'BROKEN %s:%s -> %s\n' "$file" "$line" "$target" >&2
      status=1
    fi
  done < <(
    perl -ne '
      my $line = $.;
      while (/\[[^\]]+\]\(([^)]+)\)/g) {
        print "$line:$1\n";
      }
    ' "$file"
  )
}

while IFS= read -r file; do
  check_file "$file"
done < <(find . -type f -name '*.md' | sort)

exit "$status"
