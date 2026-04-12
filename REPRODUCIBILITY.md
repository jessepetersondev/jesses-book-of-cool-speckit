# Reproducibility

This file states what must stay stable if another developer wants to reproduce the same style of result.

## Reproducibility Matrix

| Axis | Expected value |
|---|---|
| Bootstrap command | `specify init . --ai codex --ai-skills --force` |
| Observed SpecKit version | `0.5.1.dev0` |
| AI integration | `codex` |
| Shell assumption | `bash` |
| Core skill set | `constitution`, `specify`, `clarify`, `plan`, `checklist`, `tasks`, `analyze`, `implement`, `taskstoissues` |
| Workflow families | greenfield, brownfield approved-delta, phased multi-implement |
| Artifact root | `specs/<feature-id>/` |
| Checklist location | `specs/<feature-id>/checklists/` |
| Large-system operating mode | strict phased multi-implement |
| Primary example repo | `/home/ai/clawd/projects/kalshi-quant-dashboard` |
| Primary example feature | `001-quant-ops-dashboard` |

## Dashboard Reference Environment

From the actual `kalshi-quant-dashboard` quickstart:

- Node.js 22 LTS
- `pnpm` 10+
- Docker and Docker Compose
- sibling strategy repos plus publisher and executor repos available locally

Reference source:

- `/home/ai/clawd/projects/kalshi-quant-dashboard/specs/001-quant-ops-dashboard/quickstart.md`

## Stable Controls

These should stay stable across projects if you want similar outcomes:

- choose the workflow before writing prompts
- keep the command order stable
- use prompt bodies to constrain scope
- inspect artifacts between steps
- use `analyze` as a hard gate
- split large builds into multiple `speckit-implement` runs
- validate every phase before starting the next one

## Variables That Can Change

These may change without breaking the operating model:

- product domain
- feature id
- exact repo path
- exact source tree
- number of clarify passes
- number of implementation phases
- exact validation commands for the target repo

## Dashboard Example Output Surface

The latest real completed-style dashboard run produced:

- `spec.md`
- `plan.md`
- `data-model.md`
- `quickstart.md`
- `contracts/*`
- `checklists/dashboard.md`
- `checklists/requirements.md`
- `tasks.md`

Use the artifact map here:

- [examples/golden/kalshi-quant-dashboard/ARTIFACT-MAP.md](examples/golden/kalshi-quant-dashboard/ARTIFACT-MAP.md)

## Non-Deterministic Points And How To Control Them

| Risk | Control |
|---|---|
| vague requirements widen the plan | run more `clarify` passes |
| plan drifts from real file layout | revise `plan.md` before tasks or implement |
| tasks miss verification or admin/control work | regenerate `tasks.md` and re-run `analyze` |
| one implement run touches too much | switch to strict phased mode |
| late contract drift invalidates completed tasks | re-open the affected tasks and re-close after validation |

## Reproduction Target

The goal is not to reproduce the exact same app.

The goal is to reproduce:

- the same command structure
- the same artifact quality bar
- the same analyze-and-repair loop
- the same phased implementation discipline when the system is large
