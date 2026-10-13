# Copy-paste goal prompt: project-independent visual design studio

Use as a starting point for a **future** project. Replace only the text in square brackets with its actual brief; other instructions are self-contained. When the objective and boundaries are known, this is a goal prompt. When human decisions genuinely block progress, produce bounded concepts and stop at the approval gate.

```text
TITLE: VISUAL DESIGN STUDIO — ORIGINAL CONCEPTS AND CLICKABLE PROTOTYPES

Use the visual-design-intelligence skill (SKILL.md and supporting resources).

MISSION
Design an original, high-quality experience for: [PRODUCT / IDEA + TARGET USERS + TOP TASKS].
Primary platforms/devices: [WEB / MOBILE / BOTH].
The required deliverable is: [2–3 CLICKABLE DESIGN DIRECTIONS IN HTML + DESIGN.md, OR OTHER SPECIFIED OUTPUT].
Relevant constraints and branding: [CONSTRAINTS OR "NONE — CHOOSE REASONABLE CREATIVE DEFAULTS"].

WORK BOUNDARY
Work only in an isolated design-output directory approved for this task. No production code changes, deployment, purchases, service setup, external data submission, or modifications to existing repositories. Use fictional sample records. Do not start any follow-on implementation task.

PROCESS
1. Parse the brief and state reversible assumptions. If there is no repository, treat this as greenfield; do not invent one.
2. Research publicly available design/interaction ideas if access permits, recording source URLs, dates, and rights. If offline, use the bundled original style catalog and pattern library. Do not copy third-party site art, layout wholesale, source code, or restricted assets.
3. Define a design thesis and practical task flows.
4. Generate two or three **structurally and aesthetically distinct** directions that preserve identical core requirements. Document the design differences and make a recommendation.
5. Create a real, self-contained, responsive interactive prototype with working navigation, controls, validation and representative states. Prefer one HTML file with concept switching when reasonable; otherwise use clearly named standalone files. No external network dependencies by default.
6. Create DESIGN.md with coherent type, color, layout, components, states, responsive behavior and handoff notes.
7. Independently inspect rendered desktop and phone behavior if tool support exists. Run appropriate non-destructive automated checks. Mark unperformed checks NOT RUN; never claim tests ran when they did not.
8. Report the finished file paths, what works, rights/provenance, verified behavior, limitations and recommendation.

ORCHESTRATION
Use the strongest appropriate available model for creative direction, synthesis and tradeoffs. Parallelize only bounded read-only research (reference discovery, interaction-pattern review, accessibility expectations) when subagents are available and worthwhile. Use one writer per prototype/surface and a separate verifier when practical. Do not claim delegation when unsupported.

STOPPING RULES
Stop when the design deliverables and report are complete. Do not treat completion as authority to implement in a live application. Ask for human approval only for consequential/live edits, paid services, or unresolved choices that materially change the product direction. Do not expand scope.
```

## Prompt routing

- For an *idea with no project yet*, use `DIRECTIONS` + `PROTOTYPE` by default.
- For an existing product requiring new styling, begin with evidence gathering, then `DIRECTIONS` or `SYSTEM`.
- For an approved concept, skip variants and output `HANDOFF` or `PROTOTYPE` exactly as requested.
- For a simple new component, one coherent design may be better than three full pages.
