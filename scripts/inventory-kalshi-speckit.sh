#!/usr/bin/env bash
set -euo pipefail

roots=("$@")
if [[ ${#roots[@]} -eq 0 ]]; then
  roots=(/home/ai /home/ai/clawd/projects)
fi

mapfile -t specify_dirs < <(find "${roots[@]}" -maxdepth 3 -type d -name .specify 2>/dev/null | sort -u)

echo "Observed Kalshi Spec Kit repos"
echo "=============================="

for specify_dir in "${specify_dirs[@]}"; do
  repo="${specify_dir%/.specify}"
  [[ "$repo" == *kalshi* ]] || continue

  version="$(grep -m1 '"speckit_version"' "$specify_dir/init-options.json" 2>/dev/null | sed -E 's/.*"([^"]+)".*/\1/' || true)"
  [[ -n "$version" ]] || version="unknown"

  has_extensions="no"
  [[ -f "$specify_dir/extensions.yml" ]] && has_extensions="yes"

  if [[ -d "$repo/specs" ]]; then
    features="$(find "$repo/specs" -maxdepth 2 -mindepth 2 -type f -name spec.md 2>/dev/null \
      | sed "s#^$repo/specs/##; s#/spec.md##" \
      | sort \
      | paste -sd ',' -)"
    [[ -n "$features" ]] || features="none"
  else
    features="none"
  fi

  if [[ -d "$repo/.agents/skills" ]]; then
    skills="$(find "$repo/.agents/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null \
      | xargs -r -n1 basename \
      | sort \
      | paste -sd ',' -)"
    [[ -n "$skills" ]] || skills="none"
  else
    skills="none"
  fi

  printf '\nrepo: %s\n' "$repo"
  printf '  speckit_version: %s\n' "$version"
  printf '  has_extensions: %s\n' "$has_extensions"
  printf '  features: %s\n' "$features"
  printf '  skills: %s\n' "$skills"
done
