# Kalshi Speckit Reproduction Repo

This repo captures the exact Spec Kit plus Codex workflow currently used across the local Kalshi repos so it can be repeated without rebuilding the process from memory.

It is based on three local evidence sources:
- the Kalshi repos themselves
- `/home/ai/.bash_history`
- `/home/ai/.codex/history.jsonl`

## Observed Constants

- Bootstrap command: `specify init . --ai codex --ai-skills --force`
- Observed `speckit` version: `0.5.1.dev0`
- Integration: `codex`
- Branch numbering: `sequential`
- Observed extensions: none in the inspected Kalshi repos
- Observed skill bundle:
  - `speckit-constitution`
  - `speckit-specify`
  - `speckit-clarify`
  - `speckit-plan`
  - `speckit-checklist`
  - `speckit-tasks`
  - `speckit-analyze`
  - `speckit-implement`
  - `speckit-taskstoissues`

## Observed Kalshi Speckit Repos

- `/home/ai/kalshi-edge-saas`
- `/home/ai/kalshi-edging-quant`
- `/home/ai/clawd/projects/kalshi-quant-dashboard`
- `/home/ai/clawd/projects/kalshi-weather-quant`
- `/home/ai/clawd/projects/kalshi-integration-event-publisher`

## Workflow Variants

1. Greenfield SaaS build:
   `constitution -> specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement`
2. Brownfield approved-delta migration:
   `constitution -> specify -> plan -> checklist -> tasks -> analyze -> implement`
3. Large-system phased build:
   `analyze -> revise specify -> revise plan -> revise tasks -> re-analyze -> phased implement prompts`

The important observed nuance is that you do not always do one monolithic `speckit-implement` run. In the dashboard flow, you first lock the system into strict phased mode, then run multiple scoped `speckit-implement` prompts such as `Phase 2 only`, `Phase 3 only`, and `Phase 4 only`.

## Use This Repo

1. Inventory current Kalshi Spec Kit repos:
   `./scripts/inventory-kalshi-speckit.sh`
2. Bootstrap a new Spec Kit repo the same way:
   `./scripts/bootstrap-speckit-repo.sh /path/to/repo`
3. Generate the exact skill link format used in history:
   `./scripts/skill-link.sh /path/to/repo speckit-plan`
4. Verify a repo has the expected Speckit/Codex structure:
   `./scripts/verify-speckit-setup.sh /path/to/repo`
5. Use the prompt bundles in `prompts/` that match the workflow you want to reproduce.

## Repo Contents

- [kalshi-speckit-manifest.json](/home/ai/jesses-book-of-cool-speckit/kalshi-speckit-manifest.json)
  Current observed repo inventory and workflow summary.
- [docs/observed-repos.md](/home/ai/jesses-book-of-cool-speckit/docs/observed-repos.md)
  Repo-by-repo Spec Kit usage.
- [docs/workflow-patterns.md](/home/ai/jesses-book-of-cool-speckit/docs/workflow-patterns.md)
  The actual workflow variants you have been using.
- [docs/usage.md](/home/ai/jesses-book-of-cool-speckit/docs/usage.md)
  How to use this repo as a reproducibility playbook.
- [prompts/](/home/ai/jesses-book-of-cool-speckit/prompts)
  History-derived prompt bundles.
- [scripts/](/home/ai/jesses-book-of-cool-speckit/scripts)
  Helper scripts for inventory, bootstrap, verification, and skill-link generation.
