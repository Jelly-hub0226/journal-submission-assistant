"""Calculate acceptance probability for a journal given article score and journal profile."""
import sys, argparse, json

JOURNAL_TIER_DEFAULTS = {
    "top_q1":   {"threshold": 9.0, "acceptance_rate": 0.10},
    "strong_q1": {"threshold": 8.0, "acceptance_rate": 0.15},
    "solid_q2":  {"threshold": 7.0, "acceptance_rate": 0.22},
    "q3_q4":     {"threshold": 5.5, "acceptance_rate": 0.35},
    "cn_core":   {"threshold": 6.5, "acceptance_rate": 0.18},
    "cn_general":{"threshold": 5.0, "acceptance_rate": 0.45},
}

SCOPE_MAP = {"perfect": 1.2, "good": 1.0, "marginal": 0.7, "poor": 0.3}

def quality_multiplier(article_score, threshold):
    gap = article_score - threshold
    if gap >= 2.0:
        return 1.5
    elif gap >= 1.0:
        return 1.2
    elif gap >= -1.0:
        return 1.0
    elif gap >= -2.0:
        return 0.7
    else:
        return 0.4

def calc(article_score, tier=None, threshold=None, acceptance_rate=None, scope="good", cn_factors=None):
    if tier and tier in JOURNAL_TIER_DEFAULTS:
        defaults = JOURNAL_TIER_DEFAULTS[tier]
        if threshold is None:
            threshold = defaults["threshold"]
        if acceptance_rate is None:
            acceptance_rate = defaults["acceptance_rate"]

    if threshold is None or acceptance_rate is None:
        raise ValueError("Must provide tier or both threshold and acceptance_rate")

    scope_mult = SCOPE_MAP.get(scope, 1.0)
    qual_mult = quality_multiplier(article_score, threshold)
    p = acceptance_rate * scope_mult * qual_mult

    # Apply Chinese journal adjustments
    adjustment_note = ""
    if cn_factors:
        for factor, val in cn_factors.items():
            if factor == "top_institution" and val:
                p += 0.05
                adjustment_note += "; +5% top institution"
            if factor == "funded" and val:
                p += 0.05
                adjustment_note += "; +5% funded"
            if factor == "early_career" and val:
                p -= 0.05
                adjustment_note += "; -5% early career"

    p = max(0.02, min(0.95, p))
    p_low = max(0.02, p - 0.10)
    p_high = min(0.95, p + 0.10)

    return {
        "article_score": article_score,
        "journal_threshold": threshold,
        "base_acceptance_rate": round(acceptance_rate, 2),
        "scope_multiplier": scope_mult,
        "quality_multiplier": round(qual_mult, 2),
        "calculated_p": round(p, 3),
        "range": f"{int(p_low*100)}-{int(p_high*100)}%",
        "tier": "reach" if article_score >= threshold - 1.5 and article_score < threshold - 0.5
                else "match" if abs(article_score - threshold) <= 0.5
                else "safety" if article_score >= threshold + 1.0
                else "below_reach",
        "adjustments": adjustment_note if adjustment_note else None,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--score", type=float, required=True, help="Article quality score (1-10)")
    parser.add_argument("--tier", choices=list(JOURNAL_TIER_DEFAULTS.keys()), help="Journal tier")
    parser.add_argument("--threshold", type=float, help="Explicit journal quality threshold")
    parser.add_argument("--acceptance", type=float, help="Explicit journal acceptance rate (0-1)")
    parser.add_argument("--scope", choices=list(SCOPE_MAP.keys()), default="good")
    parser.add_argument("--cn-top-institution", action="store_true")
    parser.add_argument("--cn-funded", action="store_true")
    parser.add_argument("--cn-early-career", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    cn = {
        "top_institution": args.cn_top_institution,
        "funded": args.cn_funded,
        "early_career": args.cn_early_career,
    } if any([args.cn_top_institution, args.cn_funded, args.cn_early_career]) else None

    result = calc(
        article_score=args.score,
        tier=args.tier,
        threshold=args.threshold,
        acceptance_rate=args.acceptance,
        scope=args.scope,
        cn_factors=cn,
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Article Score: {result['article_score']}")
        print(f"Journal Threshold: {result['journal_threshold']}")
        print(f"Base Acceptance: {result['base_acceptance_rate']}")
        print(f"Scope Multiplier: {result['scope_multiplier']}")
        print(f"Quality Multiplier: {result['quality_multiplier']}")
        print(f"Estimated Probability: {result['range']}")
        print(f"Tier: {result['tier']}")
        if result['adjustments']:
            print(f"Adjustments: {result['adjustments']}")

if __name__ == "__main__":
    main()
