# Observed Kalshi Spec Kit Repos

This is the local Kalshi repo inventory that currently shows real `speckit` usage.

## Shared Setup

- `specify init . --ai codex --ai-skills --force` appears in `/home/ai/.bash_history`
- all inspected Kalshi Spec Kit repos have:
  - `.specify/init-options.json`
  - `.agents/skills/speckit-*.md`
  - `.specify/integrations/codex.manifest.json`
  - `speckit_version: 0.5.1.dev0`
  - no `.specify/extensions.yml`

## Repo Inventory

| Repo | Feature Specs Present | Notes |
|---|---|---|
| `/home/ai/kalshi-edge-saas` | `001-weather-last-hour-edge` | Greenfield SaaS workflow with full end-to-end Spec Kit prompt sequence. |
| `/home/ai/kalshi-edging-quant` | `001-dead-bracket-no-sweep`, `002-publisher-order-handoff` | Brownfield incremental update workflow with strict approved-delta language. |
| `/home/ai/clawd/projects/kalshi-quant-dashboard` | `001-quant-ops-dashboard` | Large monorepo workflow with repeated `speckit-implement` phase prompts. |
| `/home/ai/clawd/projects/kalshi-weather-quant` | `001-execution-boundary-migration` | Multi-repo migration workflow spanning weather-quant, publisher, and executor. |
| `/home/ai/clawd/projects/kalshi-integration-event-publisher` | none under `specs/` | Has the full Codex Speckit skill bundle installed and is referenced by other Kalshi migrations. |

## Observed Feature Files

- `kalshi-edge-saas`
  - `spec.md`
  - `plan.md`
  - `research.md`
  - `data-model.md`
  - `quickstart.md`
  - `tasks.md`
  - `checklists/requirements.md`
  - `checklists/quality.md`
  - `contracts/public-api.yaml`
- `kalshi-edging-quant`
  - `001-dead-bracket-no-sweep/*`
  - `002-publisher-order-handoff/*`
- `kalshi-quant-dashboard`
  - `001-quant-ops-dashboard/*`
  - includes `contracts/rest-api.openapi.yaml`, `contracts/live-updates.yaml`, `contracts/rbac-matrix.md`, `contracts/session-capabilities.md`, and more
- `kalshi-weather-quant`
  - `001-execution-boundary-migration/*`

## Observed Skill Bundle

Every inspected Kalshi Spec Kit repo contains the same Codex skill set:

- `speckit-analyze`
- `speckit-checklist`
- `speckit-clarify`
- `speckit-constitution`
- `speckit-implement`
- `speckit-plan`
- `speckit-specify`
- `speckit-tasks`
- `speckit-taskstoissues`

## Why This Matters

The reproducible part is not just that these repos have `.specify/`. The important observed pattern is:

- same init flags
- same Codex skill bundle
- same `speckit` version
- same feature-folder layout under `specs/`
- repeated use of customized prompt bodies layered on top of the stock skill commands

That last point is why this repo includes prompt bundles rather than only generic instructions.
