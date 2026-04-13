# Validation Rubric

Use this rubric to decide whether a run is reproducing the same quality bar.

## `spec.md`

Pass if:

- the scope is explicit and bounded
- clarifications are resolved into concrete decisions
- each user story has an independent test path
- roles, permissions, and edge cases are explicit
- the spec reads like a product definition, not an implementation draft

Fail if:

- major ambiguity remains
- key roles or admin surfaces are implied instead of stated
- success criteria are vague
- acceptance scenarios are missing

## `plan.md`

Pass if:

- the technical context matches the real problem
- the project structure matches intended implementation paths
- contracts, data model, quickstart, and design outputs are named explicitly
- the plan includes validation strategy and deployment readiness
- the constitution check still passes

Fail if:

- the source tree is inconsistent with intended files
- the plan assumes future-state architecture that does not exist yet
- validation, observability, or auth are only implied

## Checklist Artifacts

Pass if:

- `requirements.md` and `quality.md` both exist before implementation
- the checklist contains concrete, reviewable checks
- the checklist surfaces ambiguity, coverage gaps, and operational risk
- every checklist item is marked PASS or FAIL before implementation
- both `requirements.md` and `quality.md` are fully PASS before implementation starts

Fail if:

- the checklist is generic and non-binding
- it cannot be used to reject a weak spec or plan
- any checklist item remains unchecked
- implementation starts while a checklist still has FAIL items

## `tasks.md`

Pass if:

- tasks are grouped by setup, foundation, user stories, and polish or equivalent phases
- every task has a concrete output path
- every task has a dependency or prerequisite statement
- every task has an explicit verification step
- tests appear before implementation work for each story or phase

Fail if:

- tasks are broad or non-verifiable
- validation work is missing
- the task list cannot be phased safely

## `analyze` Gate

Pass if:

- contradictions, gaps, and overbuild are addressed before coding
- checklist failures route back to artifact repair instead of implementation
- the rerun path is artifact repair, not implementation

Fail if:

- the team notes the findings and codes anyway

## Phased `implement` Prompt

Pass if:

- the phase names the exact task IDs or scope bullets in play
- later phases are explicitly excluded
- validation requirements are written into the prompt
- the phase is dependency-closed

Fail if:

- the phase prompt is a broad “build the rest” instruction
- UI, API, ingest, and admin surfaces are all mixed without a reason

## Code / Validation Gate

Pass if:

- lint passes
- typecheck passes
- test suites for the touched scope pass
- build passes
- task status and docs remain aligned with the implementation

Fail if:

- the phase is declared done without a clean validation run
- contracts, runtime, and docs disagree
