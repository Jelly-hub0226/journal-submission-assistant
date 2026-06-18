"""Calculate weighted article quality score from four dimension scores."""
import sys, json, argparse

WEIGHTS = {
    "novelty": 0.25,
    "method": 0.30,
    "argument": 0.25,
    "writing": 0.20,
}

TIER_LABELS = {
    (1.0, 3.9): "Early-stage; substantial revision needed before submission",
    (4.0, 5.5): "Suitable for general/unranked journals or conferences",
    (5.6, 7.0): "Competitive for mid-tier indexed journals",
    (7.1, 8.5): "Strong candidate for reputable indexed journals (Q2-Q1)",
    (8.6, 10.0): "Potentially suitable for top-tier/high-impact journals",
}

def interpret(score):
    for (lo, hi), label in TIER_LABELS.items():
        if lo <= score <= hi:
            return label
    return "Unknown tier"

def calculate(scores):
    total = sum(scores[d] * WEIGHTS[d] for d in WEIGHTS)
    return round(total, 1)

def main():
    parser = argparse.ArgumentParser(description="Calculate article quality score")
    parser.add_argument("--novelty", type=float, required=True, help="Topic novelty (1-10)")
    parser.add_argument("--method", type=float, required=True, help="Method rigor (1-10)")
    parser.add_argument("--argument", type=float, required=True, help="Argument depth (1-10)")
    parser.add_argument("--writing", type=float, required=True, help="Writing quality (1-10)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    scores = {
        "novelty": args.novelty,
        "method": args.method,
        "argument": args.argument,
        "writing": args.writing,
    }

    for d, s in scores.items():
        if not (1 <= s <= 10):
            print(f"Error: {d} score must be 1-10, got {s}", file=sys.stderr)
            sys.exit(1)

    total = calculate(scores)
    label = interpret(total)

    if args.json:
        result = {
            "scores": scores,
            "weights": WEIGHTS,
            "total": total,
            "interpretation": label,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Article Quality Assessment")
        print(f"=========================")
        print(f"Novelty:    {scores['novelty']:4.1f} x {WEIGHTS['novelty']:.2f} = {scores['novelty'] * WEIGHTS['novelty']:.2f}")
        print(f"Method:     {scores['method']:4.1f} x {WEIGHTS['method']:.2f} = {scores['method'] * WEIGHTS['method']:.2f}")
        print(f"Argument:   {scores['argument']:4.1f} x {WEIGHTS['argument']:.2f} = {scores['argument'] * WEIGHTS['argument']:.2f}")
        print(f"Writing:    {scores['writing']:4.1f} x {WEIGHTS['writing']:.2f} = {scores['writing'] * WEIGHTS['writing']:.2f}")
        print(f"-------------------------")
        print(f"Total:      {total:.1f} / 10.0")
        print(f"Tier:       {label}")

if __name__ == "__main__":
    main()
