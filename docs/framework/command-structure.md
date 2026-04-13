# Command Structure

This file is the stripped-down operating reference for the framework.

## Bootstrap

```bash
specify init . --ai codex --ai-skills --force
```

## Prompt Anatomy

Every SpecKit prompt should have four parts:

1. the skill link
2. the objective
3. the scope boundaries
4. the constraints and required outputs

Bad:

```text
/speckit.plan
```

Good:

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md) Create the implementation plan for {PROJECT_NAME} from the approved spec.

Constraints:
- keep scope narrow
- do not invent unrelated platform features
- produce contracts, data model, quickstart, and validation strategy
```

## Skill Link Format

Use this exact link shape when composing prompts:

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md)
```

## Artifact Flow

The normal dependency chain is:

```text
constitution -> spec.md -> clarified spec.md -> plan.md -> quality.md -> tasks.md -> analyze findings -> implementation
```

If an artifact is weak, fix that artifact before moving forward.

## Greenfield Sequence

```text
speckit-constitution
speckit-specify
speckit-clarify
speckit-plan
speckit-checklist
speckit-tasks
speckit-analyze
speckit-implement
```

Intent:

- define guardrails
- define the product
- remove ambiguity
- design the system
- create quality gates
- generate implementation tasks
- audit the artifacts
- only then implement

Run rule:

- each item is a separate prompt
- inspect the generated artifact before advancing
- if `clarify` exposes missing product decisions, revise the spec there instead of hoping `plan` will fix it later

## Brownfield Sequence

```text
speckit-constitution
speckit-specify
speckit-plan
speckit-checklist
speckit-tasks
speckit-analyze
speckit-implement
```

Intent:

- preserve existing behavior
- define the delta only
- design only the incremental impact
- create parity and migration checks
- generate only delta tasks
- audit for drift
- implement only the approved delta

Run rule:

- the prompt body must explicitly state what stays unchanged
- tasks should cover only the delta plus parity validation
- if `analyze` finds unrelated redesign, revise the artifacts before coding

## Phased Sequence

```text
speckit-analyze
speckit-specify
speckit-plan
speckit-tasks
speckit-analyze
speckit-implement strict phased mode
speckit-implement phase 1
speckit-implement phase 2
speckit-implement phase 3
...
```

Intent:

- stabilize the artifacts first
- lock the implementation into phase boundaries
- implement one dependency-closed slice at a time

Run rule:

- do not start phased coding until the second `analyze` says the artifacts are aligned
- every phase prompt should name the exact task IDs or scope bullets in play
- every phase ends with validation before the next phase starts

## The Operating Rules

1. Never rely on the bare command name when scope matters. Put the constraints in the prompt body.
2. Use `clarify` before `plan` when the product definition is still fuzzy.
3. Use `analyze` as a gate before implementation, not as an afterthought.
4. If `analyze` finds drift, revise the artifacts and re-run it.
5. Use multiple `speckit-implement` runs for large systems instead of one giant run.
6. Prefer narrow prompts that name allowed scope, untouched scope, and expected deliverables.
