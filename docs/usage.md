# How To Use This Repo

## 1. Inspect Current Local Kalshi Speckit Usage

Run:

```bash
./scripts/inventory-kalshi-speckit.sh
```

This shows:

- repo path
- observed `speckit` version
- whether extensions are present
- feature IDs under `specs/`
- installed Speckit skill directories

## 2. Bootstrap A New Repo The Same Way

Observed bootstrap command:

```bash
specify init . --ai codex --ai-skills --force
```

Helper:

```bash
./scripts/bootstrap-speckit-repo.sh /path/to/new-repo
```

## 3. Generate The Exact Skill-Link Format Used In History

Example:

```bash
./scripts/skill-link.sh /home/ai/clawd/projects/kalshi-quant-dashboard speckit-plan
```

Output:

```text
[$speckit-plan](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-plan/SKILL.md)
```

That matches the history format used in `/home/ai/.codex/history.jsonl`.

## 4. Pick The Prompt Bundle That Matches The Job

- New narrow product build:
  `prompts/greenfield/kalshi-edge-saas-sequence.md`
- Existing multi-repo execution migration:
  `prompts/brownfield/kalshi-weather-migration-sequence.md`
- Existing approved-delta brownfield update with minimal-change rules:
  `prompts/brownfield/kalshi-edging-approved-delta-sequence.md`
- Large dashboard or control plane with multiple `speckit-implement` passes:
  `prompts/dashboard/`

## 5. Verify A Repo Before Running Prompts

Run:

```bash
./scripts/verify-speckit-setup.sh /path/to/repo
```

This checks for:

- `.specify/init-options.json`
- `.specify/integrations/codex.manifest.json`
- `.agents/skills/speckit-implement/SKILL.md`
- feature folders under `specs/`

## 6. Reproduce The Multi-Implement Pattern

For dashboard-style work, do not stop at a single implement run.

Observed pattern:

1. run the pre-implement prompt bundle
2. create any missing checklist files like `dashboard.md`
3. run the strict phased-mode prompt
4. run phase-specific `speckit-implement` prompts one at a time

This is the key detail that would be easy to lose if the process were only documented as "use Spec Kit."
