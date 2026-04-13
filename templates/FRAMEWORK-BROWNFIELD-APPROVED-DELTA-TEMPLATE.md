# Brownfield Approved-Delta Template

Use this when updating an existing application and you want minimal drift.

Replace all `{...}` placeholders.

How to use this file:

1. replace the placeholders
2. paste each section as its own prompt
3. keep unchanged behavior explicit in every brownfield prompt
4. reject any artifact that broadens scope beyond the approved delta
5. do not implement until `requirements.md` and `quality.md` are fully PASS and `analyze` confirms there is no hidden redesign

## Constitution Update

```text
[$speckit-constitution]({REPO_PATH}/.agents/skills/speckit-constitution/SKILL.md) Update the project constitution for an existing Spec Kit-managed application.

Context:
This repository already exists and is being updated incrementally.

Current update goal:
{DELTA_GOAL}

Critical invariant:
All other functionality must remain exactly the same unless a change is absolutely required to complete this update.

Update the constitution so future brownfield changes follow these principles:
- treat this as an incremental update, not a new build
- preserve current behavior unless the approved delta explicitly modifies it
- prefer the smallest possible safe diff
- avoid unrelated refactors, cleanups, renames, and file churn
```

## Specify Delta

```text
[$speckit-specify]({REPO_PATH}/.agents/skills/speckit-specify/SKILL.md) Update the existing specification for this Spec Kit-managed application to reflect a narrowly scoped change.

Primary repo:
- {PRIMARY_REPO}

Related repos/services:
- {RELATED_REPO_1}
- {RELATED_REPO_2}

Requested update:
{REQUESTED_DELTA}

Baseline assumptions:
- the current implemented behavior is the source-of-truth baseline
- {UNTOUCHED_AREA_1} should remain the same
- {UNTOUCHED_AREA_2} should remain the same
- this update changes only {IN_SCOPE_DELTA}

Update the spec to include:
1. existing baseline behavior relevant to this change
2. requested delta
3. exact in-scope changes
4. explicit out-of-scope changes
5. service responsibility boundaries
6. contract and reliability requirements
7. observability requirements
8. rollout constraints
```

## Plan Delta

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md) Update the existing implementation plan for this Spec Kit-managed application to incorporate the approved change.

Objective:
{PLAN_OBJECTIVE}

Planning constraints:
- preserve current implementation and architecture unless this specific change requires modification
- make the fewest possible code changes
- change the fewest possible files
- do not redesign unrelated systems
- explicitly call out untouched areas that must remain unchanged
```

## Checklist

```text
[$speckit-checklist]({REPO_PATH}/.agents/skills/speckit-checklist/SKILL.md) Generate or update checklist artifacts for this incremental brownfield change.

Create at minimum:
- `requirements.md` for delta scope, untouched behavior, acceptance criteria, and parity expectations
- `quality.md` for implementation readiness, cross-artifact alignment, migration safety, and validation gates

Checklist rules:
- every item must be concrete enough to PASS or FAIL
- explicitly verify unchanged behavior outside the approved delta
- keep deeper migration- or domain-specific checklists too when they materially reduce drift
```

## Tasks Delta

```text
[$speckit-tasks]({REPO_PATH}/.agents/skills/speckit-tasks/SKILL.md) Generate only the incremental implementation tasks needed for this approved update from spec.md, plan.md, and checklist artifacts.

Task requirements:
- organize tasks by migration objective and user/operator story
- include exact file paths where practical
- keep tasks granular enough for safe AI implementation
- include only the minimal implementation changes required
- include validation and parity tasks
- prefer fewer files and fewer changed lines whenever possible
```

## Checklist Review Gate

```text
[$speckit-checklist]({REPO_PATH}/.agents/skills/speckit-checklist/SKILL.md) Review spec.md, plan.md, tasks.md, and checklist artifacts for this incremental brownfield change.

Score `requirements.md` and `quality.md` completely:
- mark every checklist item PASS or FAIL
- cite the artifact that satisfies each PASS item
- do not leave any checklist item unchecked

If any checklist item is FAIL or unchecked:
- return BLOCKED
- list the exact failed items
- state whether spec.md, plan.md, or tasks.md must change
- do not recommend implementation
```

## Analyze Delta

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Analyze the updated spec.md, plan.md, tasks.md, and scored checklist artifacts for this incremental brownfield change.

Find:
- scope creep beyond the requested delta
- service-boundary ambiguity
- missing task coverage
- weak contract definitions
- missing parity validation
- unnecessary refactors or file touches

Treat any FAIL or unchecked item in `requirements.md` or `quality.md` as a blocking issue.
```

## Implement Delta

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) Implement only the approved delta for this existing Spec Kit-managed application, using the updated spec.md, plan.md, tasks.md, and scored checklist artifacts.

Implementation rules:
- only proceed if `requirements.md` and `quality.md` are fully PASS
- if any checklist item is FAIL or unchecked, stop and return BLOCKED instead of asking to proceed anyway
- use the current implementation as the baseline
- implement only the approved delta
- preserve all other existing behavior unless the approved artifacts explicitly require otherwise
- change the fewest possible lines in the fewest possible files
- keep request/message contracts explicit, traceable, and auditable

After each major checkpoint:
- report what changed
- report what was validated
- report any remaining tasks
- report any blocker or mismatch discovered
```
