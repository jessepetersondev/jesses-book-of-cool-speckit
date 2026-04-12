#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' >&2
usage: generate-prompt-pack.sh --workflow greenfield|brownfield|phased [options]

options:
  --repo PATH                set REPO_PATH
  --project NAME             set PROJECT_NAME
  --vars-file FILE           load KEY=VALUE pairs
  --set KEY=VALUE            set or override a placeholder value
  --out FILE                 write output to FILE instead of stdout
EOF
  exit 1
}

workflow=""
repo_path=""
project_name=""
vars_file=""
out_file=""

declare -A vars

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workflow)
      workflow="${2:-}"
      shift 2
      ;;
    --repo)
      repo_path="${2:-}"
      shift 2
      ;;
    --project)
      project_name="${2:-}"
      shift 2
      ;;
    --vars-file)
      vars_file="${2:-}"
      shift 2
      ;;
    --set)
      pair="${2:-}"
      [[ "$pair" == *=* ]] || usage
      key="${pair%%=*}"
      value="${pair#*=}"
      vars["$key"]="$value"
      shift 2
      ;;
    --out)
      out_file="${2:-}"
      shift 2
      ;;
    *)
      usage
      ;;
  esac
done

[[ -n "$workflow" ]] || usage

case "$workflow" in
  greenfield)
    template="templates/FRAMEWORK-GREENFIELD-TEMPLATE.md"
    ;;
  brownfield)
    template="templates/FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md"
    ;;
  phased)
    template="templates/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md"
    ;;
  *)
    usage
    ;;
esac

if [[ -n "$vars_file" ]]; then
  [[ -f "$vars_file" ]] || {
    echo "missing vars file: $vars_file" >&2
    exit 1
  }
  while IFS= read -r line; do
    [[ -n "$line" ]] || continue
    [[ "${line:0:1}" == "#" ]] && continue
    [[ "$line" == *=* ]] || continue
    key="${line%%=*}"
    value="${line#*=}"
    vars["$key"]="$value"
  done < "$vars_file"
fi

if [[ -n "$repo_path" ]]; then
  vars["REPO_PATH"]="$repo_path"
fi

if [[ -n "$project_name" ]]; then
  vars["PROJECT_NAME"]="$project_name"
fi

content="$(<"$template")"

for key in "${!vars[@]}"; do
  token="{$key}"
  replacement="${vars[$key]}"
  content="${content//"$token"/"$replacement"}"
done

unresolved="$(
  printf '%s\n' "$content" \
    | grep -oE '\{[A-Z0-9_]+\}' \
    | sort -u \
    | tr '\n' ' ' \
    | sed 's/[[:space:]]*$//' || true
)"

timestamp="$(date +%F)"

header="# Generated Prompt Pack

- workflow: $workflow
- template: $template
- generated_at: $timestamp"

if [[ -n "${vars[REPO_PATH]:-}" ]]; then
  header="$header
- repo_path: ${vars[REPO_PATH]}"
fi

if [[ -n "${vars[PROJECT_NAME]:-}" ]]; then
  header="$header
- project_name: ${vars[PROJECT_NAME]}"
fi

if [[ -n "$unresolved" ]]; then
  header="$header
- unresolved_placeholders: $unresolved"
else
  header="$header
- unresolved_placeholders: none"
fi

output="$header

$content"

if [[ -n "$out_file" ]]; then
  mkdir -p "$(dirname "$out_file")"
  printf '%s\n' "$output" > "$out_file"
  echo "wrote: $out_file"
else
  printf '%s\n' "$output"
fi
