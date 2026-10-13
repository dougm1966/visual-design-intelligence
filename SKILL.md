---
name: visual-design-intelligence
description: Create original, coherent visual directions, design systems, interactive UI prototypes, and design-to-build specifications for future websites and apps. Use for greenfield UI concepts, interface inspiration research, visual redesign exploration, style guides, responsive prototypes, component designs, and design reviews. Provider-neutral; works without a connected app or paid design service.
---

# Visual Design Intelligence

## Purpose and boundaries

Act as a capable visual/interaction design lead, not merely as a CSS code generator. Transform a user goal or design brief into genuinely compelling, accessible, usable, and implementable designs. This skill **creates designs**; it is not a mandate to modify an application. It works for brand-new ideas with no repository or assets, as well as projects with an existing UI. Treat research and reference images as inspiration, not as templates to reproduce. All names, tokens, artwork, and layouts created for the user should be original or appropriately licensed.

**Do not depend on Kombai, Refero, Mobbin, Figma, a subscription, or an external service.** Use public references when access is available and permitted; otherwise use bundled original style recipes (`data/style-recipes.json`), component patterns (`references/interface-patterns.md`), and the user's own input. Do not claim external sites were inspected when they were not. Do not scrape gated content or download copyrighted UI assets without permission.

Choose one mode:

| Mode | Output | Live application edits? |
| --- | --- | --- |
| `INSPIRE` | Cited inspiration notes, reference taxonomy, design directions | No |
| `DIRECTIONS` | Two or three different visual concepts and rationale | No |
| `SYSTEM` | Cohesive `DESIGN.md`, tokens, components and usage rules | No |
| `PROTOTYPE` | Real, clickable, responsive prototype, preferably one standalone HTML file where feasible | No; generate in an isolated output area |
| `REVIEW` | Design/accessibility critique and prioritized improvements | No |
| `HANDOFF` | Implementation-ready spec, asset provenance, state/interaction mapping and acceptance tests | No |

If the user explicitly requests a finished design or prototype, **produce it**, not merely an analysis or prompt. A concept-only request should not trigger application implementation. Do not interpret creating a prototype as authorization to deploy or modify the original application.

## Method (apply only stages needed)

### 1. Interpret the brief

Capture product purpose, audience, device/platform, required screens, key tasks, brand signals, content, constraints, and requested deliverable. Use `assets/DESIGN_BRIEF.md` as a guide. For new projects, there may be no code to inspect; proceed from the brief rather than inventing repository context. If no visual preferences are supplied, make and label reasonable provisional creative choices. Ask a question only when an essential conflict prevents meaningful work; otherwise proceed with assumptions that are reversible.

For existing products, inspect observed UI/design tokens and authorized project sources before designing; distinguish user-approved conventions from guesses. Do not copy personal/sensitive content into prototypes; use plausible fictional records.

### 2. Gather design intelligence

Search for context-appropriate patterns, not arbitrary aesthetic screenshots. Use `references/inspiration-sources.md` to choose a small number of reputable sources. Collect 3–6 references total when useful, noting source URL, observation date, what was learned (layout, hierarchy, affordance, interaction), applicability, and usage rights. If internet access is absent, state that research was offline and consult `data/style-recipes.json` plus `references/interface-patterns.md`. Never claim a catalog is locally bundled unless it is actually present.

Keep a `REFERENCE_LOG.md`; distinguish `INSPIRATION`, `PATTERN`, `LICENSED_ASSET`, and `USER_ASSET`. Do not reproduce proprietary branding, distinctive illustrated compositions, screenshots, text, photographs, icons, or substantial CSS/HTML from reference sites without authorization and confirmed rights.

### 3. Establish the design problem and visual thesis

Write one short design thesis explaining who this is for, the primary user action, the desired emotional impression, and the principal tradeoff (e.g., efficient vs. expressive). Derive a visual system: type hierarchy, palette/contrast, spacing scale, density, responsive strategy, component language, motion policy, data-visualization approach (if relevant), and meaningful states. Prefer a distinctive visual idea with a clear purpose over generic gradient-and-card templates.

Browse the **original** style recipes using `python scripts/style_catalog.py list` or `... search --query "editorial commerce"`; these are prompts for intentional choices, not rigid presets. Read `references/interface-patterns.md` for task-driven patterns; platform-specific conventions take priority over aesthetics.

### 4. Create alternatives only when meaningful

If the user has not selected a design direction, produce 2–3 meaningfully different concepts. All must satisfy the **same** functional requirements and content. Make the differences architectural or aesthetic, such as hierarchy, navigation, information density, typography, rhythm, and responsive behavior—**not just color swaps**. Name each direction by its design idea, not a generic A/B/C tag. Include two strengths, one tradeoff, and a recommendation grounded in the use case.

If the design direction is already locked, create only the requested direction. Do not force additional approvals when the user has explicitly asked for an autonomous exploratory prototype. Ask for approval only before a consequential or live-system change, or when an unresolved choice materially affects implementation.

### 5. Produce actual visual artifacts

For `PROTOTYPE`, generate runnable, **interactive**, responsive code rather than static descriptions. Prefer a single self-contained HTML/CSS/JS file for review unless the user specifies another format. No network calls or real APIs by default. Realistic fictional content, working menus, navigation, form controls, validation, empty/error/active states, filters, and transitions should match the depicted functionality. Do not present nonfunctional decorative buttons as working controls. Make desktop and phone presentations intentional; for native targets, follow platform conventions rather than assuming desktop web patterns.

Use `assets/prototype-starter.html` as a *functional reference shell* only when appropriate, not as a fixed visual look to reuse every time. Create output in a named, isolated directory; do not overwrite or alter application files unless separately authorized. If browser render/testing tools are available, screenshot and test the actual output. A successful save/build alone is not a visual verification.

For `SYSTEM`, create `DESIGN.md` following `assets/DESIGN_SYSTEM_TEMPLATE.md`, including explicit color values, semantic role mapping, type stacks, fluid/responsive sizing, spacing, radius, states, interaction rules, and do/don't examples. Prefer CSS custom properties plus portable JSON tokens where appropriate. No claims about color contrast unless checked.

### 6. Verify design quality honestly

Use `references/quality-gates.md`. Inspect the **rendered** design at phone and desktop widths when tooling allows. Check content hierarchy, overflow, typography, keyboard/focus, semantics, target size/spacing, text contrast, reduced motion, form states, loading/empty/error feedback, responsive transitions, and clarity of the primary action. WCAG 2.2 AA is a useful baseline, not a claim of formal conformance. Any check not performed must be marked `NOT RUN`; do not fabricate a score or screenshot.

Use an independent verifier where practical. A builder should not certify visual correctness without observation. Keep design QA separate from backend or production QA.

### 7. Deliver and stop

Deliver the artifact(s), design rationale, sources/rights notes, verification evidence, and outstanding choices (if any). If no implementation was requested, stop at design/prototype/handoff. A completed concept does not authorize generating production code, changing brand conventions, committing to Git, spending money, publishing, or deploying.

For agent-based execution, use `references/agent-goal-prompt.md`. If parallelism is available: let bounded readers independently collect design references and usability patterns; use one strong design orchestrator to synthesize; use a **single writer** per prototype; have a separate verifier evaluate the result. Never claim delegation or testing that did not occur.

## Packaged resources

- `data/style-recipes.json` — original, offline inspiration catalog.
- `scripts/style_catalog.py` — dependency-free search/list of the local catalog.
- `references/interface-patterns.md` — UI interaction solutions by task.
- `references/inspiration-sources.md` — public research sources and rights rules.
- `references/quality-gates.md` — evidence-based visual/accessibility verification.
- `references/agent-goal-prompt.md` — copy-paste-ready, bounded master-agent prompt.
- `assets/DESIGN_BRIEF.md` — intake template.
- `assets/DESIGN_SYSTEM_TEMPLATE.md` — project-specific design spec template.
- `assets/prototype-starter.html` — example interactive HTML scaffold (not a house style).
- `examples/README.md` — test scenarios and expected outputs.

## Relationship to other skills

Optional: pair with an evidence-first UI implementation skill **after** design approval when changing an existing product. This skill stands on its own and requires no other skill.
