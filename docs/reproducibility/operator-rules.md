# Operator Rules

These are the non-obvious manual rules behind the repo. They are the difference between a decent SpecKit run and the results you have actually been getting.

## Core Rules

1. Pick the workflow before writing prompts.
   Greenfield, approved-delta brownfield, and phased multi-implement are different control systems, not different labels for the same thing.

2. Never jump straight to `speckit-implement`.
   The artifact chain is the product of the workflow, not optional paperwork.

3. Use prompt bodies as control surfaces.
   The skill name alone does not carry enough constraints to reproduce a good result.

4. Use `clarify` aggressively when the scope is still fuzzy.
   The dashboard example used multiple clarify passes because one pass was not enough to make the spec implementation-safe.

5. Create checklist artifacts before implementation.
   The repo should have explicit checklist files before coding starts.

6. Score checklist artifacts after `tasks` and before implementation.
   `requirements.md` and `quality.md` are not ready until every item is marked PASS or FAIL.

7. Treat `analyze` as a gate, not a report.
   If drift is found, repair the artifacts first.

8. Use multiple `speckit-implement` runs for large systems.
   Large features should be broken into dependency-closed phases.

9. Keep each phase narrow and dependency-closed.
   The phase prompt should say exactly what belongs in the run and exactly what does not.

10. Update `tasks.md` as implementation progresses.
   A phased build is easier to control when task status stays in sync with the actual code.

11. End every phase with validation.
    The dashboard-style pattern is not complete until lint, typecheck, tests, and build have all run.

12. Keep canonical truth and compiled packs separate.
    `spec.md`, `plan.md`, `data-model.md`, `contracts/*`, `checklists/*`, `tasks.md`, `tasks.json`, and accepted `phase-summaries/*.json` are canonical. `generated/<feature-id>/phase-packs/*.md` are compiled artifacts only.

13. If a clean phase changes canonical truth, invalidate downstream packs immediately.
    Update the source artifact, write the accepted phase summary, reconcile the pack set, and discard every older downstream pack before the next run.

14. Refuse stale packs by snapshot.
    The pack `snapshot_id` must match `.speckit/feature-state.json` before the next `speckit-implement` run starts.

## Observed Manual Behaviors Worth Preserving

- create named checklist files before `speckit-implement`
- score checklist files completely before `speckit-implement`
- create `dashboard.md` first when the workflow depends on a concrete dashboard artifact
- repeat the same `speckit-implement` prompt when the phase needs another controlled pass
- re-open and re-close drifted tasks when contracts or runtime behavior change late
- write a structured accepted phase summary after every clean phase
- regenerate current and downstream packs immediately after accepted artifact repairs

## Dashboard-Specific Examples

- Multiple clarify passes were used up front to lock down taxonomy, PnL semantics, security, and user journeys.
- A separate pre-implement revision pass was used before phased implementation began.
- Strict phased mode was set before the per-phase prompts.
- The preserved implementation prompts start at Phase 2 because the important pattern was the controlled phase split, not one giant run.

## What To Do When You Are Unsure

Use the safer control:

- choose the narrower scope
- choose the smaller diff
- choose the artifact repair path
- choose another phased run instead of broadening the current one
