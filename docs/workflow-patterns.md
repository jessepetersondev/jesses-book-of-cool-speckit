# Workflow Patterns

This is the actual workflow shape observed across the local Kalshi Spec Kit repos.

## 1. Greenfield SaaS Build

Observed in: `/home/ai/kalshi-edge-saas`

Sequence:

1. `speckit-constitution`
2. `speckit-specify`
3. `speckit-clarify`
4. `speckit-plan`
5. `speckit-checklist`
6. `speckit-tasks`
7. `speckit-analyze`
8. `speckit-implement`

Notes:

- this is the cleanest full greenfield pattern
- the prompts are not generic one-liners; they are heavily scoped to the exact product wedge
- the checklist was used both as a normal requirements-quality pass and again to request a single `quality.md` file

## 2. Brownfield Approved-Delta Migration

Observed in:

- `/home/ai/clawd/projects/kalshi-weather-quant`
- `/home/ai/kalshi-edging-quant`

Sequence:

1. update or create a brownfield constitution
2. update the existing `spec.md` only for the requested delta
3. update the implementation `plan.md` only for the requested delta
4. create a migration `quality.md`
5. generate only the incremental tasks
6. analyze aggressively for scope creep and unnecessary churn
7. run `speckit-implement` with strict approved-delta language

Critical brownfield characteristics:

- preserve the current implementation as the baseline
- explicitly define untouched behavior
- minimize changed files and changed lines
- do not let Spec Kit turn an incremental migration into a rewrite
- use multi-repo wording when publisher and executor repos are involved

Observed extra note:

- before implementation, the user explicitly asked: `Create the quality.md file for this app before we do speckit implement.`

## 3. Strict Phased Multi-Implement Workflow

Observed in: `/home/ai/clawd/projects/kalshi-quant-dashboard`

Sequence:

1. initial greenfield build prompts
2. analyze for missing coverage
3. revise `spec.md`
4. revise `plan.md`
5. regenerate `tasks.md`
6. re-run `speckit-analyze`
7. set strict phased implementation mode
8. run `speckit-implement` for a single phase only
9. repeat `speckit-implement` for later phases

Observed phase prompts:

- `Implement Phase 2 only for 001-quant-ops-dashboard`
- `Implement Phase 3 only for 001-quant-ops-dashboard`
- `Implement Phase 4 only for 001-quant-ops-dashboard`

Observed strict phased-mode rules:

- read all design artifacts before coding
- identify exact in-scope task IDs first
- implement only dependency-closed task sets
- update `tasks.md` as tasks are completed
- run lint, typecheck, tests, and build before stopping
- end each phase with completed task IDs, changed files, validation, blockers, and next recommended phase

Observed extra note:

- before phased implementation, the user explicitly said: `create the dashboard.md first`

## Practical Takeaway

The reproduction target is not just "run Spec Kit."

The real repeatable pattern is:

- start with the stock Speckit skill
- add a very explicit prompt body that constrains scope
- regenerate artifacts when analyze finds drift
- split implementation into multiple `speckit-implement` runs when the feature is large
- use brownfield-safe prompts for existing systems and phased prompts for large new systems
