# Interface pattern intelligence — original quick reference

Use patterns because they solve a *user task*, not because they are fashionable. Distinguish mobile-native, responsive web, and desktop desktop-first conventions. Validate the pattern against real use cases, not just aesthetic screenshots.

| User problem | Candidate patterns | Avoid / question | Important states |
| --- | --- | --- | --- |
| First-time orientation | short progressive onboarding; contextual hints; example state | multi-step tour before any value | skipped, resumed, dismissed |
| Frequent daily action | dominant quick-action area; persistent action bar | burying action in mega-menu | ready, active, completed, error |
| Complex data entry | grouped form; stepper; inline summary | showing 50 fields without structure | optional, invalid, saved, resumed |
| Search large catalog | query + refinements; filters with visible chips | hidden filter state or zero-result dead end | loading, no results, cleared |
| Compare options | aligned comparison matrix; feature highlights | cards with incomparable details | selected, disabled, unknown |
| Show live status | severity-coded status summary; recent events | color-only meaning | idle, pending, success, warning |
| Navigation in small app | bottom nav for few top destinations; clear active state | 7+ tiny tabs | active, deep link, overflow |
| Navigation in large app | adaptive sidebar; grouped sections; search | identical nav at all widths | collapsed, expanded, mobile drawer |
| Learn from a dashboard | key metrics + trend + explanation | chart overload and misleading scales | empty, stale, partial data |
| Long chronological record | timeline; date grouping; anchors | endless ungrouped table | current, past, edited |
| Edit an entity | detail panel with explicit save/cancel | accidental autosave with no feedback | dirty, saving, saved, conflict |
| Work offline | offline banner + queued sync + conflict states | pretending data synced | offline, queued, retry, conflict |
| Sensitive action | double-check critical facts; explicit confirmation | vague destructive controls | preview, confirmed, canceled |
| Primary + secondary CTAs | clear priority by prominence | equal-weight action clutter | hover, focus, disabled, busy |
| Dense expert workspace | adjustable density, keyboard shortcuts | making a mobile-only large-card UI | compact, standard, personalized |
| Data table for mobile | stacked summary rows + drill-in | 12-column table squashed onto phone | expanded, sorted, filtered |
| Trust and verification | provenance, timestamps, audit trail | unsupported "verified" badges | known, unknown, outdated |
| Media-heavy presentation | purposeful image hierarchy and captions | stock imagery as decoration | loaded, error, alt text |
| Pricing/commerce | transparent total cost and terms | late fees or confusing CTAs | selection, tax, fulfillment |
| Accessibility-critical flow | explicit text labels, semantic grouping, focus return | icons alone carrying meaning | focus, errors, zoom, reduced motion |

## Distinct design concepts

Each concept must intentionally differ along *at least two* independent axes while preserving identical requirements:

- Information architecture: task-first / narrative-first / overview-first.
- Density: spacious / balanced / compact.
- Navigation: single-page / tabs / sidebar / search-led.
- Typography: expressive editorial / geometric sans / utilitarian.
- Shape and surfaces: flat rules / layered surfaces / soft cards / high-contrast panels.
- Color logic: monochrome-with-accent / tonal / warm material / cool precision.
- Motion: quiet functional / editorial transitions / static by preference.
- Responsive adaptation: reflow / priority-based disclosure / mode switching.

Different colors on identical components **do not** constitute distinct concepts.

## Content-first design test

Before polishing a screen, replace placeholder headline and fake metrics with realistic, task-representative sample content. Check overflow, truncation, localization potential, zero states, warnings, and ambiguous labels. Design only counts as successful when actual user information is understandable.
