# How To Use This Framework

## 1. Bootstrap A Repo

Observed base command:

```bash
specify init . --ai codex --ai-skills --force
```

Helper:

```bash
./scripts/bootstrap-speckit-repo.sh /path/to/repo
```

## 2. Verify The Repo Has The Expected Shape

```bash
./scripts/verify-speckit-setup.sh /path/to/repo
```

This checks for:

- `.specify/init-options.json`
- `.specify/integrations/codex.manifest.json`
- `.agents/skills/speckit-implement/SKILL.md`

## 3. Choose A Workflow Type

- new build:
  use `prompts/framework/greenfield-sequence-template.md`
- existing app with one narrow update:
  use `prompts/framework/brownfield-approved-delta-template.md`
- large project with multiple implement passes:
  use `prompts/framework/phased-multi-implement-template.md`

## 4. Fill In The Placeholders

Replace items such as:

- `{REPO_PATH}`
- `{PROJECT_NAME}`
- `{PRODUCT_DESCRIPTION}`
- `{IN_SCOPE}`
- `{OUT_OF_SCOPE}`
- `{PRIMARY_REPO}`
- `{RELATED_REPOS}`
- `{TARGET_FLOW}`
- `{PHASE_NAME}`
- `{PHASE_SCOPE}`

## 5. Generate Skill Links In The Same Format

```bash
./scripts/skill-link.sh /path/to/repo speckit-plan
```

Example output:

```text
[$speckit-plan](/path/to/repo/.agents/skills/speckit-plan/SKILL.md)
```

## 6. Use Analyze As A Control Gate

Do not treat `speckit-analyze` as optional.

Use it to catch:

- missing task coverage
- scope drift
- contradictions between `spec.md`, `plan.md`, and `tasks.md`
- places where the generated plan is broader than intended

## 7. Use Multiple `speckit-implement` Runs When Needed

If the project is large:

1. set strict phased mode
2. define the exact task IDs for the phase
3. run one phase only
4. validate
5. repeat for the next phase

That is the main command-structure nuance that made the Kalshi dashboard flow work.

## 8. Use The Kalshi Material As Examples

If you want concrete examples of how the templates were actually used, see:

- [examples/kalshi/README.md](/home/ai/jesses-book-of-cool-speckit/examples/kalshi/README.md)
- the history-derived bundles already present under `prompts/`
