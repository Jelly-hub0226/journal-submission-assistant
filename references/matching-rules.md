# Journal Matching & Acceptance Probability Rules

## Journal Threshold Defaults

These are heuristic starting points. Adjust based on actual journal metrics when available.

| Journal Tier | Implicit Quality Threshold | Typical Acceptance Rate |
|---|---|---|
| Top-tier (Q1, IF > 10) | 9.0+ | 5-15% |
| Strong Q1 (IF 5-10) | 8.0+ | 10-20% |
| Solid Q2 (IF 2-5) | 7.0+ | 15-30% |
| Q3-Q4 / Unranked | 5.5+ | 25-50% |
| General Chinese core (北大核心, CSSCI) | 6.5+ | 10-25% |
| Chinese non-core / general | 5.0+ | 30-60% |

## Tier Assignment Rules

Given an article quality score `S`:

- **Reach tier**: Journals where threshold T satisfies `S >= T - 1.5`
  (Article is within striking distance; acceptance possible with luck or minor revision)
- **Match tier**: Journals where `abs(S - T) <= 0.5`
  (Strong fit; realistic chance of acceptance)
- **Safety tier**: Journals where `S >= T + 1.0`
  (Article quality comfortably exceeds journal threshold; high probability)

## Scope Match Adjustment

Journals have subject-area preferences. Before recommending, verify:
1. Does the journal publish in the article's field? (Check recent issues)
2. Has the journal recently published on similar topics? (Check last 1-2 years)
3. Is the article's methodology type accepted by this journal?

Scope mismatch overrides tier assignment: if a journal never publishes in the article's field, do not recommend it regardless of quality match.

## Acceptance Probability Calculation

```
P = Base_acceptance_rate x Scope_multiplier x Quality_multiplier
```

Where:
- `Base_acceptance_rate`: the journal's reported acceptance rate (or tier default if unknown)
- `Scope_multiplier`:
  - 1.2: perfect scope fit (journal actively publishes on this topic)
  - 1.0: good scope fit (journal covers this field)
  - 0.7: marginal scope fit (tangentially related)
  - 0.3: poor scope fit (rarely publishes in this area)
- `Quality_multiplier`:
  - 1.5: article score exceeds journal threshold by 2+ points
  - 1.2: article score exceeds threshold by 1-2 points
  - 1.0: article score within 1 point of threshold
  - 0.7: article score below threshold by 1-2 points
  - 0.4: article score below threshold by 2+ points

Cap final probability at 95% and floor at 2%.

## Output Format for Probability

Report as a range: `[P - 10%, P + 10%]`, bounded by [floor, cap].
Example: calculated P = 42% -> report "35-50%"

## Chinese Journal Special Rules

For Chinese journals, also consider:
- **Institutional affiliation**: top Chinese universities have higher acceptance at elite Chinese journals
- **Fund acknowledgments**: papers with national/provincial fund support have higher acceptance in CSSCI journals
- **Author seniority**: Chinese core journals may prefer established scholars; note this for early-career authors

These factors are soft adjustments (add/subtract ~5 percentage points) and should be mentioned in the recommendation narrative.
