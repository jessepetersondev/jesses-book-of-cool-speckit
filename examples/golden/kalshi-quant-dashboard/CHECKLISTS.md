# Checklists

Real source files:

- `/home/ai/clawd/projects/kalshi-quant-dashboard/specs/001-quant-ops-dashboard/checklists/dashboard.md`
- `/home/ai/clawd/projects/kalshi-quant-dashboard/specs/001-quant-ops-dashboard/checklists/requirements.md`

## Why These Matter

The dashboard run did not use a checklist as decoration. The checklists acted as review gates before planning and implementation.

## Dashboard Checklist Categories

The deep checklist reviews:

- requirement completeness
- requirement clarity
- requirement consistency and acceptance quality
- scenario and edge-case coverage
- operational and dependency coverage

This is the stronger example of what a quality gate should look like.

## Requirements Checklist Categories

The high-level checklist validates:

- no implementation details leak into the spec
- requirements are testable and unambiguous
- success criteria are measurable
- user scenarios and edge cases are complete
- scope is clearly bounded

## Reproduction Bar

If you want similar results:

- create at least one checklist before coding
- make the checklist strong enough to reject a weak spec or plan
- keep both a deep operational checklist and a high-level spec quality checklist when the product is large
