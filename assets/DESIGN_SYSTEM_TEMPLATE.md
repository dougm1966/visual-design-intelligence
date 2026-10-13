# DESIGN.md — [product or concept]

**Status:** PROPOSED / APPROVED
**Version/date:**
**Design thesis:** One sentence describing user, primary task and visual intent.
**Audience and device hierarchy:**
**Source-of-truth and references:**

## 1. Design principles

Write 3–5 testable principles. Example: "Critical tasks are available within one visible action from the home screen."

## 2. Semantic tokens

| Role | Value | Usage | Evidence/decision |
| --- | --- | --- | --- |
| `--color-bg` | #... | page background | proposed |
| `--color-surface` | #... | cards/panels | proposed |
| `--color-text` | #... | primary copy | proposed |
| `--color-muted` | #... | secondary copy | proposed |
| `--color-accent` | #... | primary actions | proposed |
| `--color-border` | #... | separators | proposed |
| `--color-danger` | #... | destructive warnings | proposed |

Specify contrast pairs checked and tool/measurement. Do not label them AA without checking.

## 3. Typography

Specify heading, UI, body, code/numeric stacks; weights; size scale; line heights; letter spacing; font loading/fallback/offline behavior. Avoid inaccessible ultra-light body text.

## 4. Layout and spacing

Specify content width, grids, margin rhythm, spacing tokens, density options, breakpoints and how navigation/forms/tables transform on mobile.

## 5. Component anatomy and states

For each reusable component: purpose, structure, variants, states (default/hover/focus/active/disabled/busy/error/empty), responsive behavior and accessibility notes.

## 6. Interaction and motion

Describe gestures, keyboard, validation, feedback, reduced-motion alternatives, error recovery, saving and navigation behavior.

## 7. Visual examples and anti-patterns

Include do/don't comparisons tied to this specific product. Note which references are inspiration only.

## 8. Implementation handoff

Target platform/stack; files or resources in scope only after approval; screen list; interaction/state contract; assets and licenses; test matrix; release gates; non-goals. No production write/deploy authority is implicit.
