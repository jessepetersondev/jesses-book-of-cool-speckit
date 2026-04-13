# Prompt Cookbook

These are reusable prompt fragments that preserve the command structure and operating style used in the real runs.

## Scope Clamps

Use when the scope needs to stay narrow:

```text
- keep scope narrow for the first release
- do not invent unrelated platform features
- do not broaden scope beyond the approved release
```

## No-Code / No-Tasks Gates

Use during `specify` and `plan`:

```text
Do not jump into implementation yet.
Do not create code.
Do not generate implementation tasks yet.
```

## Clarify Language

Use when ambiguity is still dangerous:

```text
Interrogate the spec for ambiguity and missing decisions.
Update the spec so ambiguity is minimized before planning.
Do not proceed while major responsibility or contract ambiguity remains.
```

## Brownfield Preservation

Use when existing behavior must stay stable:

```text
Use the current implemented system as the source-of-truth baseline.
Preserve all existing behavior except the approved delta.
Do not broaden scope into redesign, cleanup, modernization, or unrelated architecture work.
Change the fewest possible lines in the fewest possible files.
```

## Checklist Language

Use when generating quality gates:

```text
Generate a quality checklist for the approved spec and plan.
Create a single general quality checklist if possible.
Name it quality.md if the template allows.
```

## Analyze Gate Language

Use when validating readiness:

```text
Analyze spec.md, plan.md, tasks.md, and the quality checklist for consistency and implementation readiness.
Find contradictions, vague terms, missing task coverage, and overbuilt architecture.
Re-run analysis after artifact repairs and verify the remaining issues are closed before implementation begins.
```

## Strict Phased Mode Language

Use before per-phase implementation:

```text
Work in strict phased mode for all subsequent implementation runs.
Identify the exact task IDs in scope for the phase plus any direct prerequisites.
Implement only that dependency-closed set.
Do not start later phases in this run.
```

## Phase Validation Language

Use at the end of every phase:

```text
Run lint, typecheck, tests, and build for every touched package before stopping.
End each phase with completed task IDs, files changed, validation run, blockers or follow-up risks, and the next recommended phase.
```

## Multi-Repo Boundary Language

Use when more than one repo participates in the change:

```text
Define the responsibility boundary for each repo explicitly.
Do not let the migration redefine unrelated parts of the participating systems.
Keep the publishing, execution, and decisioning boundaries traceable and auditable.
```

## Dashboard-Like System Language

Use when the product is a large control plane or observability dashboard:

```text
Require explicit auth/RBAC, observability, degraded-state behavior, live/historical parity, and deep-linkable detail routes.
Support mixed-source ingestion for current-state reality instead of assuming future-state convergence already exists.
Split implementation into backend ingestion, API/auth, and UI phases instead of one giant run.
```
