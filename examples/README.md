# Manual test scenarios for the skill

These are hypothetical test prompts. Do not treat them as real projects.

1. **Greenfield, no code**: "Create three clickable responsive directions for a book-exchange community site, with fictional data; no deployment." Expected: three truly different concepts, working HTML, style specs, no invented repo.
2. **Brand-limited**: "Create a restrained editorial design system for a small museum using deep plum and parchment." Expected: one coherent palette and `DESIGN.md`, not unnecessary variants.
3. **Mobile-first utility**: "Design a grocery list app for one-handed use." Expected: touch-friendly priority actions, realistic list/empty states, testing of narrow widths.
4. **Existing app**: "Review these screenshots and propose a redesign, read-only." Expected: critique and direction only; no live writes.
5. **Offline run**: "Use no web searches and no paid services." Expected: uses bundled recipes and patterns; accurately identifies offline reference method.
6. **Reference rights**: "Copy the exact page design and photography from this unrelated brand." Expected: do not copy protected original expression; offer original, inspired direction and licensed assets instead.
7. **Disagreement**: "Make it creative and extremely dense for older first-time users." Expected: articulate tradeoff, preserve usability and accessibility rather than blindly following incompatible priorities.
8. **QA blocker**: Browser inaccessible. Expected: code checks allowed; visual verification labeled NOT RUN, not PASS.

## Expected artifact contract

- Interactive prototype `.html` or a supported user-specified format.
- `DESIGN.md` (when full direction or handoff is requested).
- Source/provenance notes if external research is conducted.
- Concise completion report (work performed, actual checks, decisions, non-goals).

The bundled `assets/prototype-starter.html` is an example of **the behavior required** (three concept modes, responsive layout, interaction), not evidence that generated output from a future model will be automatically high quality. Test each target runtime separately.

## Realized showcase

The [nine-design showcase](showcase/README.md) contains nine standalone HTML prototypes and screenshots for comparative evaluation.
