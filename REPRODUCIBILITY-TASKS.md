# Reproducibility Tasks

This file turns the missing repo improvements into explicit tasks and tracks them as completed work.

Primary source example:

- `/home/ai/clawd/projects/kalshi-quant-dashboard/specs/001-quant-ops-dashboard/`

## Task List

- [x] T001 Add an end-to-end replay guide in [REPRODUCE.md](REPRODUCE.md)
- [x] T002 Add a golden example set for the latest real dashboard run in [examples/golden/kalshi-quant-dashboard/README.md](examples/golden/kalshi-quant-dashboard/README.md)
- [x] T003 Add a hard rerun-routing table in [RERUN-ROUTING.md](RERUN-ROUTING.md)
- [x] T004 Add explicit operator rules in [OPERATOR-RULES.md](OPERATOR-RULES.md)
- [x] T005 Add a reusable prompt fragment library in [PROMPT-COOKBOOK.md](PROMPT-COOKBOOK.md)
- [x] T006 Add a reproducibility matrix in [REPRODUCIBILITY.md](REPRODUCIBILITY.md)
- [x] T007 Add a prompt-pack generator plus a real dashboard sample in [scripts/generate-prompt-pack.sh](scripts/generate-prompt-pack.sh) and [examples/golden/kalshi-quant-dashboard/generated-phase-2-pack.md](examples/golden/kalshi-quant-dashboard/generated-phase-2-pack.md)
- [x] T008 Add a validation rubric in [VALIDATION-RUBRIC.md](VALIDATION-RUBRIC.md)

## Completion Order

1. Add the replay guide so there is one canonical way to follow the process.
2. Add the golden dashboard example set so the expected artifact quality is concrete.
3. Add rerun routing so developers know what to do when artifacts drift.
4. Add operator rules so the non-obvious manual behaviors are explicit.
5. Add the prompt cookbook so the reusable command language is easy to apply.
6. Add the reproducibility matrix so the expected environment and stable controls are visible.
7. Add the prompt-pack generator and a real dashboard sample pack.
8. Add the validation rubric so developers can judge whether they are reproducing the same quality bar.

## Definition Of Done

- every missing reproducibility asset exists in the repo
- the docs point to the latest real dashboard example set
- the generated prompt-pack script produces a usable phased pack
- root navigation links to the new assets
