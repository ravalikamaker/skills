"""Synthetic local-only delivery API and CLI; no network access."""
import argparse


def deliver(sender, attempts=3):
    """Stop on success, or return False when the attempt limit is exhausted."""
    for _ in range(max(1, attempts)):
        if sender():
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, default=3,
                        help="maximum calls (default: 3)")
    args = parser.parse_args()
    print(deliver(lambda: True, args.attempts))


if __name__ == "__main__":
    main()
