# SpecKit Command Framework

This repo is a reusable framework for building applications with the same SpecKit plus Codex command structure used to create the Kalshi apps in this environment.

The repo is organized in two layers:

- framework: reusable command sequences, prompt templates, helper scripts, and workflow guidance
- examples: the Kalshi repos and history-derived prompt bundles that proved the framework shape in real use

Kalshi is the reference example, not the product scope of this repo.

## Core Idea

The repeatable part is not just `specify init`.

The real system is:

1. initialize a repo with SpecKit and Codex skills
2. choose the correct workflow shape
3. run the skill commands in a consistent order
4. use explicit prompt bodies to constrain scope
5. re-run `analyze/specify/plan/tasks` when drift appears
6. split `speckit-implement` into multiple passes when the project is large

## Observed Base Command Structure

Bootstrap:

```bash
specify init . --ai codex --ai-skills --force
```

Observed base skill set:

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

## Start Here

- [docs/command-structure.md](/home/ai/jesses-book-of-cool-speckit/docs/command-structure.md)
  Exact reusable command shapes.
- [docs/workflow-patterns.md](/home/ai/jesses-book-of-cool-speckit/docs/workflow-patterns.md)
  When to use each workflow type.
- [docs/usage.md](/home/ai/jesses-book-of-cool-speckit/docs/usage.md)
  How to apply the framework to a new repo.
- [prompts/framework/](/home/ai/jesses-book-of-cool-speckit/prompts/framework)
  Reusable prompt templates with placeholders.
- [examples/kalshi/README.md](/home/ai/jesses-book-of-cool-speckit/examples/kalshi/README.md)
  The concrete Kalshi examples this framework was derived from.

## Helper Scripts

- `./scripts/bootstrap-speckit-repo.sh /path/to/repo`
- `./scripts/inventory-speckit.sh`
- `./scripts/inventory-kalshi-speckit.sh`
- `./scripts/skill-link.sh /path/to/repo speckit-plan`
- `./scripts/verify-speckit-setup.sh /path/to/repo`

## Important Distinction

This repo is now opinionated toward reuse:

- `prompts/framework/` contains adaptable templates
- the older Kalshi-specific bundles remain as concrete examples
- the docs explain the generic workflow first, then show Kalshi as a worked example corpus
