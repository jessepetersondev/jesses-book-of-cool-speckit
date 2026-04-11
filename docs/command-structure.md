# Command Structure

This is the reusable command structure that other builders can copy.

## Bootstrap

```bash
specify init . --ai codex --ai-skills --force
```

## Skill Link Format

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md)
```

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
...
```

## Reusable Rules

- always constrain scope in the prompt body
- use `clarify` before planning when the product definition is still fuzzy
- use `analyze` before implementation when you need consistency checks
- force `quality.md` or other checklist artifacts when you want a persistent control surface
- break large builds into multiple implement passes instead of one monolithic run
