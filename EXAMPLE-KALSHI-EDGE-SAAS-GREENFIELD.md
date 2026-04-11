# Kalshi Edge SaaS Greenfield Sequence

Observed source: `/home/ai/.codex/history.jsonl`, session `019d54d5-78a1-7cd3-be25-00b638eeb7b2`

Use this when you want the same greenfield SaaS pattern that was used for `kalshi-edge-saas`.

If you reuse this in another repo, replace the absolute repo path. The text below preserves the observed prompt bodies.

## 1. Constitution

```text
[$speckit-constitution](/home/ai/kalshi-edge-saas/.agents/skills/speckit-constitution/SKILL.md) Create project principles for this repo.

Project:
A SaaS web application that identifies potential edge in Kalshi weather markets during the final hour before market close/resolution, and presents those opportunities to users in a clear, explainable dashboard.

Principles:
- Build only for one narrow wedge first: Kalshi weather last-hour opportunity detection
- Do not broaden scope to all Kalshi categories
- Do not broaden scope to all weather strategies
- The first release is a SaaS analysis/ranking tool, not a giant trading platform
- Every surfaced opportunity must be explainable using explicit inputs and scoring logic
- Prefer deterministic, auditable rules over vague AI-driven scoring in v1
- Separate ingestion, normalization, scoring, persistence, API, UI, and alerting concerns
- Preserve a thin vertical-slice architecture for the MVP
- Every user story must have acceptance criteria
- Every implementation task must have a verifiable completion condition
- No fake edge claims; the system must present evidence, confidence, and rationale
- Backtesting and live monitoring must be designed for auditability
- Do not assume any external weather source, Kalshi endpoint, or market metadata shape without explicitly researching and validating it
- Minimize speculative subsystems and premature complexity
- Prefer one clear dashboard and one clear user journey in v1
- The app must be production-oriented, modular, and extensible for future weather categories or other Kalshi verticals
```

## 2. Specify

```text
[$speckit-specify](/home/ai/kalshi-edge-saas/.agents/skills/speckit-specify/SKILL.md) Create a baseline product specification for a SaaS web application called "Kalshi Weather Last Hour Edge".

Core concept:
This product helps users identify possible edge opportunities in Kalshi weather markets during the final hour before the market closes or is effectively decided.

The first release must be tightly constrained.

In-scope product vision:
- A SaaS dashboard for users
- Focused only on Kalshi weather markets
- Focused only on the final hour before market close / resolution
- Focused only on surfacing, ranking, and explaining candidate opportunities
- The app should ingest live market data and relevant supporting weather/reference inputs
- The app should compute a transparent last-hour opportunity score
- The app should show users why a market was flagged
- The app should track whether flagged opportunities would have performed well after being surfaced
- The app may support alerts/watchlists in MVP only if they remain narrow and simple

Out of scope for first release:
- All Kalshi categories outside weather
- Broad all-day market scanning
- Complex automated trading infrastructure unless explicitly justified later
- Social/community features
- Brokerage-style portfolio management
- Highly complex ML models
- Multi-strategy edge engines
- Broad financial analytics unrelated to the weather last-hour wedge

The specification must define the product as a SaaS website tool, not just an internal script.

The spec must include:
1. Business objective
2. Target user persona
3. Exact definition of "last-hour weather edge" for MVP
4. Glossary for:
   - edge
   - candidate opportunity
   - last hour
   - confidence
   - market rationale
   - outcome tracking
5. User workflows for the SaaS site
6. Functional requirements
7. Non-functional requirements
8. Data requirements
9. Explainability requirements
10. Outcome tracking requirements
11. User stories with acceptance criteria
12. Non-goals
13. Assumptions
14. Risks
15. Open questions
16. Success metrics

Important constraints:
- This is a narrow SaaS MVP
- The product should emphasize explainability over black-box scoring
- The MVP should surface candidate opportunities, not claim guaranteed profit
- The product should be framed as a decision-support and opportunity-ranking tool
- Keep the first release small enough to ship safely

The user stories should reflect a real SaaS dashboard, for example:
- seeing current last-hour candidate markets
- filtering/ranking them
- viewing why a market is flagged
- reviewing historical flagged opportunities
- optionally subscribing and receiving alerts

Do not jump into implementation yet.
Do not create code.
Focus on a high-quality product spec.
```

## 3. Clarify

```text
[$speckit-clarify](/home/ai/kalshi-edge-saas/.agents/skills/speckit-clarify/SKILL.md) Interrogate the Kalshi Weather Last Hour Edge spec for ambiguity and missing decisions.

Focus especially on clarifying:
- What exact weather market types are in scope first
- What exactly counts as the "last hour"
- Whether the app is advisory only, alerting only, semi-automated, or execution-enabled
- Whether execution is out of scope for MVP
- Which exact data sources are required versus optional
- What inputs determine the opportunity score
- What evidence and rationale must be shown to the user
- How confidence is represented
- How historical performance of surfaced opportunities is tracked
- Whether users need accounts, saved watchlists, subscriptions, and billing in MVP
- Which pages exist in the MVP SaaS site
- What the main user journey is from sign-in to opportunity review
- Which parts are public marketing site content versus authenticated product features
- What legal/compliance/disclaimer boundaries are needed
- What exact success metric defines a successful MVP
- What should be postponed to phase 2

Update the spec so ambiguity is minimized before planning.

Be aggressive about identifying vague phrases such as:
- edge
- confidence
- anomaly
- mispricing
- resolution timing
- strong setup
- profitable
- signal quality

Do not proceed with technical planning until the spec is specific enough that tasks can be generated without major drift.
```

## 4. Plan

```text
[$speckit-plan](/home/ai/kalshi-edge-saas/.agents/skills/speckit-plan/SKILL.md) Create the implementation plan for the Kalshi Weather Last Hour Edge SaaS based on the approved spec.

The product is a SaaS website tool with a narrow MVP:
- Weather markets only
- Last-hour opportunity detection only
- Explainable ranking/dashboard only
- Historical outcome tracking
- Optional lightweight alerts if justified

Plan the application as a real SaaS product.

The implementation plan must include:
1. System architecture
2. Frontend architecture
3. Backend architecture
4. Data ingestion architecture
5. Opportunity scoring engine boundary
6. Historical outcome tracking design
7. Persistence/data model
8. API contracts
9. Auth/account/subscription architecture if included in MVP
10. Alerting architecture if included in MVP
11. Admin/ops considerations
12. Logging/observability
13. Deployment strategy
14. Validation/testing strategy
15. Rollout plan
16. Risk register
17. Explicit mapping from each user story to technical components

Technical planning principles:
- Keep the MVP thin and production-oriented
- Avoid overengineering
- Separate concerns cleanly
- Keep all scoring logic transparent and inspectable
- Ensure the dashboard can explain why opportunities were surfaced
- Design for future expansion to additional weather strategies later, but do not build them now
- Treat data ingestion, normalization, scoring, storage, and UI as separate layers
- Do not invent large platform capabilities not required by the spec

The SaaS plan should likely account for pages such as:
- landing page
- pricing/subscription page if in scope
- login/signup
- dashboard
- opportunity detail page
- historical performance page
- settings/alerts page if in scope

Do not generate implementation tasks yet.
Produce a clear plan.md for a narrow, realistic MVP.
```

## 5. Checklist

```text
[$speckit-checklist](/home/ai/kalshi-edge-saas/.agents/skills/speckit-checklist/SKILL.md) Generate a quality checklist for the Kalshi Weather Last Hour Edge SaaS spec and plan.

The checklist should verify:
- the MVP remains narrow
- the product is truly SaaS-oriented and user-facing
- requirements are complete enough for implementation
- last-hour edge is clearly defined
- the scoring/ranking concept is explainable
- user stories are testable
- the dashboard UX is coherent
- outcome tracking is clearly defined
- any auth/subscription features are justified
- any alerting features are justified
- no premature automation/trading execution has crept into MVP
- plan.md remains aligned to spec.md
- there are no vague or unverifiable acceptance criteria
- the product can ship as a useful first release
```

## 6. Tasks

```text
[$speckit-tasks](/home/ai/kalshi-edge-saas/.agents/skills/speckit-tasks/SKILL.md) Generate actionable implementation tasks for the Kalshi Weather Last Hour Edge SaaS from the approved spec.md and plan.md.

Task generation requirements:
- Organize tasks by user story
- Include exact file paths where appropriate
- Keep tasks granular enough for safe AI implementation
- Include frontend, backend, ingestion, scoring, persistence, auth, subscription, alerting, and validation tasks only if justified by the spec
- Mark safe parallel tasks
- Include test/validation tasks
- Include checkpoints after each major vertical slice
- Ensure every task has a verifiable completion condition
- Ensure no task exists without a user-story or plan justification
- Keep MVP tasks narrow; avoid speculative future-platform work

The tasks should favor a thin vertical-slice build order, such as:
1. project skeleton and shared foundations
2. ingestion and normalized market/weather inputs
3. opportunity scoring engine
4. dashboard API
5. SaaS dashboard UI
6. opportunity detail and rationale view
7. historical outcome tracking
8. auth/subscription/alerts only if already approved in scope
9. validation and deployment readiness

The result should be a clean, practical tasks.md for implementation.
```

## 7. Analyze

```text
[$speckit-analyze](/home/ai/kalshi-edge-saas/.agents/skills/speckit-analyze/SKILL.md) Analyze spec.md, plan.md, and tasks.md for consistency and implementation readiness.

Specifically find:
- contradictions between product scope and technical plan
- vague terms that remain unresolved
- tasks that have no user-story justification
- user stories with missing task coverage
- overbuilt architecture relative to MVP scope
- places where SaaS requirements are underspecified
- places where data assumptions are too weak
- parts of the plan that are too broad for the first release
- components that should be postponed to phase 2

Produce a concrete alignment report and recommend exact edits before implementation begins.
```

## 8. Optional Checklist Override To Force `quality.md`

```text
[$speckit-checklist](/home/ai/kalshi-edge-saas/.agents/skills/speckit-checklist/SKILL.md) Generate a general product and implementation quality checklist for the Kalshi Weather Last Hour Edge SaaS.
Create a single checklist file focused on scope control, requirements clarity, plan alignment, explainability, data realism, and MVP readiness.
Name it quality.md if the template allows.
```

## 9. Implement

```text
[$speckit-implement](/home/ai/kalshi-edge-saas/.agents/skills/speckit-implement/SKILL.md) Implement the Kalshi Weather Last Hour Edge SaaS strictly from spec.md, plan.md, and tasks.md.

Rules:
- Do not expand scope beyond the approved MVP
- Do not broaden beyond weather markets
- Do not broaden beyond last-hour opportunity detection
- Do not add large autonomous trading features unless explicitly included in the approved spec
- Keep the implementation modular and production-oriented
- Preserve transparency and explainability in scoring
- Ensure surfaced opportunities include rationale data for the UI
- After each checkpoint, report:
  - what was implemented
  - what was validated
  - what remains
  - any blockers or mismatches discovered

If a task appears underspecified, resolve it by consulting the spec and plan rather than inventing new product scope.
```
