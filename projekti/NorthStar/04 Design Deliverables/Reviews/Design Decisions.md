# NorthStar — Design Decisions

Source: NorthStar Brand Exploration.dc.html (Foundation + Brand Exploration sprint)

## Foundation

- **Design Tokens**: no tokens architecture existed in source docs; per the Approved Design Constraints, none was invented — tokens are named aliases of the already-approved Color/Type/Spacing/Radius/Elevation values only.
- **Color**: warm-neutral base + one muted, low-chroma primary (calm/trustworthy/approachable). Semantic colors (success/warning/danger) share the primary's chroma and lightness so no single color dominates or signals urgency alone.
- **Typography**: one family (Helvetica Neue-style sans), readability over expressiveness. Financial figures get weight/size emphasis via tabular numerals, never color-only emphasis.
- **Spacing**: 4px base unit; generous upper values so whitespace does grouping/separation work.
- **Grid**: 12-column desktop / 4-column mobile, rarely broken.
- **Radius**: moderate scale (6/10/16px) — soft enough to feel approachable, not sharp (intimidating) or fully rounded (playful).
- **Elevation**: minimal — borders and a single soft shadow tier over heavy multi-layer shadows; depth never competes with content.
- **Components**: one problem per component, identical behaviour across all modules (Housing Loans, Leasing, Document Analysis, Financial Terms, future modules).

## Brand Exploration — Three Directions

- **1a Calm Intelligence** — quiet, minimal, cool-neutral, single desaturated blue accent, no illustration/photography, slow linear motion.
- **1b Human Finance** — warm, rounder shapes, flat line illustrations of everyday moments, gentle spring motion.
- **1c Premium Guidance** — dark ink + brass accent, serif headlines, editorial black-and-white imagery, precise minimal motion.

**Selected: 1a — Calm Intelligence.** Rationale in Recommendation.md.

## Direction A+ (evolution of 1a)

~95% of 1a preserved unchanged (philosophy, hierarchy, calm mood, type scale, layout, spacing, accessibility, component philosophy). Signature additions:

1. Primary hue nudged to a specific desaturated teal-blue ("Northlight") instead of a generic fintech blue.
2. One sharp corner per container (others soft) — an ownable geometric mark.
3. **Certainty Arc** — a thin arc beside AI statements/figures whose length shows the AI's actual confidence; drawn once, slowly, never a spinner.
4. Financial figures underline only the decimal portion.
5. Loading states use a plain 2px linear-speed line — no spinner, no percentage.
6. Confirmation feedback is an underline sweep beneath the label, not a toast/checkmark.
