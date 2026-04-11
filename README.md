# SpecKit Command Framework

This repo is a reusable framework for creating applications with the same SpecKit plus Codex command structure used to build the Kalshi apps here.

It is now flattened so the important material is visible from the main repo page and top-level file list instead of being buried in nested folders.

Kalshi is the example corpus, not the scope of the framework.

## What This Repo Gives You

- the exact bootstrap command
- the reusable workflow shapes
- copyable prompt templates
- real example prompt bundles from the Kalshi builds
- helper scripts for bootstrap, verification, skill-link generation, and repo inventory

## Base Bootstrap

```bash
specify init . --ai codex --ai-skills --force
```

Observed base skills:

- `speckit-constitution`
- `speckit-specify`
- `speckit-clarify`
- `speckit-plan`
- `speckit-checklist`
- `speckit-tasks`
- `speckit-analyze`
- `speckit-implement`
- `speckit-taskstoissues`

## Reusable Workflow Types

1. Greenfield build
   `constitution -> specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement`
2. Brownfield approved-delta update
   `constitution -> specify-delta -> plan-delta -> checklist -> tasks-delta -> analyze -> implement-delta`
3. Large phased build
   `analyze -> revise specify -> revise plan -> revise tasks -> re-analyze -> strict phased mode -> multiple implement passes`

## Main Files

- [COMMAND-STRUCTURE.md](/home/ai/jesses-book-of-cool-speckit/COMMAND-STRUCTURE.md)
  Exact reusable command shapes.
- [WORKFLOW-PATTERNS.md](/home/ai/jesses-book-of-cool-speckit/WORKFLOW-PATTERNS.md)
  When to use each workflow type.
- [USAGE.md](/home/ai/jesses-book-of-cool-speckit/USAGE.md)
  How to apply the framework to a new repo.
- [FRAMEWORK-GREENFIELD-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-GREENFIELD-TEMPLATE.md)
  Reusable greenfield prompt sequence.
- [FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md)
  Reusable brownfield minimal-diff prompt sequence.
- [FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md)
  Reusable phased implementation prompt sequence.
- [KALSHI-EXAMPLES.md](/home/ai/jesses-book-of-cool-speckit/KALSHI-EXAMPLES.md)
  The concrete example bundles this framework was derived from.
- [KALSHI-EXAMPLE-CORPUS.md](/home/ai/jesses-book-of-cool-speckit/KALSHI-EXAMPLE-CORPUS.md)
  The example repo corpus behind the framework.

## Quick Start

1. Bootstrap a repo:

```bash
./scripts/bootstrap-speckit-repo.sh /path/to/repo
```

2. Verify it:

```bash
./scripts/verify-speckit-setup.sh /path/to/repo
```

3. Generate a skill link in the same format used by the command history:

```bash
./scripts/skill-link.sh /path/to/repo speckit-plan
```

4. Pick one workflow template:

- [FRAMEWORK-GREENFIELD-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-GREENFIELD-TEMPLATE.md)
- [FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md)
- [FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md](/home/ai/jesses-book-of-cool-speckit/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md)

5. Replace the placeholders and run the matching `speckit-*` sequence.

## Main-Page Summary

The repeatable system is:

1. initialize a repo with SpecKit and Codex skills
2. choose the correct workflow shape
3. write a strong prompt body for each skill invocation
4. use `clarify` when product definition is still fuzzy
5. use `analyze` as a control gate before implementation
6. regenerate `spec.md`, `plan.md`, and `tasks.md` when drift appears
7. split `speckit-implement` into multiple runs when the project is large

## Helper Scripts

- `./scripts/bootstrap-speckit-repo.sh /path/to/repo`
- `./scripts/inventory-speckit.sh`
- `./scripts/inventory-kalshi-speckit.sh`
- `./scripts/skill-link.sh /path/to/repo speckit-plan`
- `./scripts/verify-speckit-setup.sh /path/to/repo`

## Example Bundles

Greenfield:

- [EXAMPLE-KALSHI-EDGE-SAAS-GREENFIELD.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-EDGE-SAAS-GREENFIELD.md)

Brownfield:

- [EXAMPLE-KALSHI-WEATHER-MIGRATION.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-WEATHER-MIGRATION.md)
- [EXAMPLE-KALSHI-EDGING-APPROVED-DELTA.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-EDGING-APPROVED-DELTA.md)

Phased:

- [EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md)
- [EXAMPLE-KALSHI-DASHBOARD-02-PRE-IMPLEMENT-REVISION.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-02-PRE-IMPLEMENT-REVISION.md)
- [EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md)
- [EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md)
- [EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md)
- [EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md](/home/ai/jesses-book-of-cool-speckit/EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md)
