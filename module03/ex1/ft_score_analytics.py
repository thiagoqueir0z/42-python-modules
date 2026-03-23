"""Module for analyzing player scores with list-based statistics."""

import sys


def process_scores(args: list[str]) -> None:
    """
    Convert command-line arguments to integers and display analytics.

    Args:
        args: A list of string arguments from the command line.
    """
    print("=== Player Score Analytics ===")

    if not args:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            continue

    if not scores:
        print("No valid numeric scores to process.")
        return

    count = len(scores)
    total = sum(scores)
    average = total / count
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    process_scores(sys.argv[1:])
