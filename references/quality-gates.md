# Visual design and prototype quality gates

A statement of `PASS` requires performed, observed checks. When no browser or testing environment exists, use `NOT RUN` and describe the limitation; do not self-award visual verification based on code appearance.

## Gate 1 — Concept quality

- [ ] Has one clear visual thesis related to user/audience, not trend-chasing.
- [ ] Gives the primary action obvious visual priority.
- [ ] Distinct concepts differ in structure/hierarchy as well as surface styling.
- [ ] Matches requested content, platform, and functional scope.
- [ ] Demonstrates meaningful typography, intentional spacing, and sufficient visual contrast.
- [ ] Avoids generic repetitive cards, decorative gradients, invisible labels, and indiscriminate animation.

## Gate 2 — Functional proof

- [ ] Buttons, tabs, filters, menus, and dialogs depicted as active genuinely work.
- [ ] Navigation is coherent; focused state is visible; keyboard path is possible.
- [ ] Forms provide labels, validation, submission feedback, and recovery.
- [ ] Empty, loading, error, disabled, active, and success states are present when applicable.
- [ ] Fictional sample content is credible and contains varied data lengths.
- [ ] No external APIs, production accounts, trackers, or real personal data by default.

## Gate 3 — Accessibility

- [ ] Semantic headings, labels and interactive controls are used.
- [ ] Visible keyboard focus; logical traversal and focus return for overlays.
- [ ] Information is not communicated by color alone.
- [ ] Text and meaningful control contrast checked against WCAG criteria as applicable.
- [ ] Pointer targets meet WCAG 2.2 SC 2.5.8 or a valid exception; where possible prefer larger targets for touch.
- [ ] Reduced motion respected for nonessential animation.
- [ ] Text enlargement and reflow do not truncate critical content.
- [ ] Images use appropriate alt text or decorative exclusion.

## Gate 4 — Responsive verification

- [ ] Render and inspect a narrow phone (~360px), broad phone (~430px), tablet (~768px), and desktop (~1280px) when tools permit.
- [ ] No horizontal scrolling of the whole viewport without a defensible reason.
- [ ] Tables and navigation adapt intentionally, not merely shrink.
- [ ] Text size, line length and density stay usable.
- [ ] Touch/click controls retain readable affordances.

## Gate 5 — Handoff and evidence

- [ ] Final design specifies tokens, type, layout constraints, components and interactions.
- [ ] Reference log labels inspiration vs user-provided and licensed assets.
- [ ] Prototype location is real; runnable instructions given.
- [ ] Verification shows `PASS`/`FAIL`/`NOT RUN` per test category.
- [ ] Unresolved choices, known limitations and exact stopping point stated.
- [ ] No deployment or production edits occurred without user authorization.

## Suggested evaluation matrix

Score each dimension 0–5 **only if evidence supports it**. Compare alternatives without pretending the score is objective:

| Dimension | Relative importance | Observable criteria |
| --- | --- | --- |
| Task clarity & usability | High | primary action, comprehension, efficient flow |
| Visual identity | High | coherent style, purpose-led typography/composition |
| Responsive design | High | real layouts at relevant widths |
| Functional fidelity | High | interactions, states, realistic sample data |
| Accessibility | High | semantics, keyboard, contrast, motion, controls |
| Implementation portability | Medium | simple structure, documented assets, reusable tokens |

Do not average away a critical accessibility failure or missing core function.
