# Greenfield Sequence Template

Use this when starting a new application.

Replace all `{...}` placeholders.

How to use this file:

1. replace the placeholders
2. paste each section as its own prompt
3. inspect the generated artifact after each step
4. do not move to `plan` until `clarify` closes major ambiguity
5. do not move to `implement` until `analyze` says the artifacts are ready

## Constitution

```text
[$speckit-constitution]({REPO_PATH}/.agents/skills/speckit-constitution/SKILL.md) Create project principles for this repo.

Project:
{PROJECT_NAME}

Principles:
- {PRINCIPLE_1}
- {PRINCIPLE_2}
- {PRINCIPLE_3}
- Keep scope narrow for the first release
- Every implementation task must have a verifiable completion condition
- Prefer production-oriented structure over throwaway scaffolding
```

## Specify

```text
[$speckit-specify]({REPO_PATH}/.agents/skills/speckit-specify/SKILL.md) Create a baseline product specification for {PROJECT_NAME}.

Core concept:
{PRODUCT_DESCRIPTION}

In scope:
- {IN_SCOPE_1}
- {IN_SCOPE_2}
- {IN_SCOPE_3}

Out of scope:
- {OUT_OF_SCOPE_1}
- {OUT_OF_SCOPE_2}
- {OUT_OF_SCOPE_3}

The spec must include:
1. Business objective
2. Target user persona
3. User workflows
4. Functional requirements
5. Non-functional requirements
6. Data requirements
7. User stories with acceptance criteria
8. Assumptions
9. Risks
10. Open questions
11. Success metrics

Do not jump into implementation yet.
Do not create code.
```

## Clarify

```text
[$speckit-clarify]({REPO_PATH}/.agents/skills/speckit-clarify/SKILL.md) Interrogate the spec for ambiguity and missing decisions.

Focus especially on:
- scope boundaries
- required data sources
- user journeys
- page or interface map
- legal/compliance boundaries if relevant
- what belongs in phase 1 versus later phases

Update the spec so tasks can be generated without major drift.
```

## Plan

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md) Create the implementation plan for {PROJECT_NAME} based on the approved spec.

The plan must include:
1. System architecture
2. Frontend or interface architecture
3. Backend or service architecture
4. Data model
5. Contracts
6. Validation and testing strategy
7. Rollout plan
8. Risk register
9. Mapping from each user story to technical components

Planning principles:
- keep the MVP thin and production-oriented
- separate concerns cleanly
- do not invent large platform capabilities not required by the spec

Do not generate implementation tasks yet.
```

## Checklist

```text
[$speckit-checklist]({REPO_PATH}/.agents/skills/speckit-checklist/SKILL.md) Generate a quality checklist for the approved spec and plan.

The checklist should verify:
- scope remains narrow
- requirements are complete enough for implementation
- user stories are testable
- plan.md remains aligned to spec.md
- there are no vague or unverifiable acceptance criteria

Create a single general quality checklist if possible.
Name it quality.md if the template allows.
```

## Tasks

```text
[$speckit-tasks]({REPO_PATH}/.agents/skills/speckit-tasks/SKILL.md) Generate actionable implementation tasks from the approved spec.md and plan.md.

Task generation requirements:
- organize tasks by user story
- include exact file paths where appropriate
- keep tasks granular enough for safe AI implementation
- include validation tasks
- mark safe parallel tasks
- ensure every task has a verifiable completion condition
```

## Analyze

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Analyze spec.md, plan.md, tasks.md, and the quality checklist for consistency and implementation readiness.

Find:
- contradictions between scope and plan
- unresolved vague terms
- missing task coverage
- missing quality-gate coverage
- architecture that is too broad for the intended release
```

## Implement

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) Implement the project strictly from spec.md, plan.md, tasks.md, and the quality checklist.

Rules:
- do not expand scope beyond the approved release
- preserve alignment between code, contracts, docs, and tests
- after each checkpoint, report what was implemented, what was validated, what remains, and any blockers
```
