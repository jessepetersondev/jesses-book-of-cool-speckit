# Usage

This is the practical how-to.

## 1. Create A New Repo

```bash
mkdir my-app
cd my-app
specify init . --ai codex --ai-skills --force
```

Or use:

```bash
../../scripts/bootstrap-speckit-repo.sh /path/to/repo
```

## 2. Verify The Repo

```bash
../../scripts/verify-speckit-setup.sh /path/to/repo
```

## 3. Generate A Skill Link

```bash
../../scripts/skill-link.sh /path/to/repo speckit-plan
```

Example output:

```text
[$speckit-plan](/path/to/repo/.agents/skills/speckit-plan/SKILL.md)
```

## 4. Choose A Workflow

Use:

- [FRAMEWORK-GREENFIELD-TEMPLATE.md](../../templates/FRAMEWORK-GREENFIELD-TEMPLATE.md) for new products
- [FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md](../../templates/FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md) for existing apps where only one narrow change is allowed
- [FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md](../../templates/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md) for large systems that need multiple implementation passes

## 5. Generate Or Fill A Prompt Pack

You can either fill the template manually or generate a prompt pack:

```bash
../../scripts/generate-prompt-pack.sh \
  --workflow phased \
  --vars-file ../../examples/golden/kalshi-quant-dashboard/prompt-pack-values.env \
  --out /tmp/prompt-pack.md
```

Generated example:

- [examples/golden/kalshi-quant-dashboard/generated-phase-2-pack.md](../../examples/golden/kalshi-quant-dashboard/generated-phase-2-pack.md)

Ready-to-run vars files:

- phased dashboard example: [examples/golden/kalshi-quant-dashboard/prompt-pack-values.env](../../examples/golden/kalshi-quant-dashboard/prompt-pack-values.env)
- greenfield sample: [examples/SAMPLE-GREENFIELD-VALUES.env](../../examples/SAMPLE-GREENFIELD-VALUES.env)
- brownfield sample: [examples/SAMPLE-BROWNFIELD-VALUES.env](../../examples/SAMPLE-BROWNFIELD-VALUES.env)

## 6. Fill In The Template

Replace placeholders such as:

- `{REPO_PATH}`
- `{PROJECT_NAME}`
- `{PRODUCT_DESCRIPTION}`
- `{IN_SCOPE_1}`
- `{OUT_OF_SCOPE_1}`
- `{PRIMARY_REPO}`
- `{RELATED_REPO_1}`
- `{DELTA_GOAL}`
- `{PHASE_NAME}`
- `{PHASE_SCOPE_1}`

## 7. Paste One Block At A Time Into Codex

Do not paste the entire template as one mega-prompt.

The operating pattern is:

1. open the selected template
2. replace the placeholders
3. paste the first block into Codex
4. wait for the artifact update
5. inspect the result
6. paste the next block

Do not skip straight to `implement`.

## 8. Inspect The Artifacts After Each Step

At minimum, check that:

- `spec.md` matches the requested scope
- `plan.md` solves the scope you actually approved
- `quality.md` or checklist items are concrete and testable
- `tasks.md` is granular and covers validation

If one of those artifacts is weak, fix it before moving forward.

## 9. Use `analyze` As A Gate

The normal pattern is:

1. define the rules
2. define the scope
3. remove ambiguity
4. design the system
5. create quality gates
6. generate tasks
7. analyze for drift
8. implement

## 10. What To Do When The Artifacts Drift

If `speckit-analyze` finds:

- missing task coverage
- contradictions between `spec.md` and `plan.md`
- overbuilt architecture
- underspecified requirements

Then go back and revise the source artifact. Do not just note the problem and keep coding.

Typical correction loop:

```text
analyze -> revise spec -> revise plan -> regenerate tasks -> analyze again -> implement
```

Use the routing table here:

- [rerun-routing.md](../reproducibility/rerun-routing.md)

## 11. When To Split Into Multiple Implement Runs

Use phased implementation when:

- the feature spans multiple packages
- one run would touch too many files
- backend, contracts, and UI should land in separate passes
- you want phase-level validation checkpoints

The dashboard example used this pattern successfully.

## 12. Reproducing The Same Result Across Projects

The reusable part is the command structure, not the product domain.

To reproduce the same operating style every time:

- keep the command order stable
- adapt only the prompt body and scope bullets
- use the same analyze gate before implementation
- split large builds into multiple `speckit-implement` runs
- preserve unchanged behavior explicitly in brownfield work

See also:

- [reproduce.md](../reproducibility/reproduce.md)
- [reproducibility.md](../reproducibility/reproducibility.md)
- [validation-rubric.md](../reproducibility/validation-rubric.md)
- [examples/golden/kalshi-quant-dashboard/BEFORE-AND-AFTER-ANALYZE.md](../../examples/golden/kalshi-quant-dashboard/BEFORE-AND-AFTER-ANALYZE.md)
- [examples/golden/kalshi-quant-dashboard/README.md](../../examples/golden/kalshi-quant-dashboard/README.md)
