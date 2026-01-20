import argparse
from load_test.runner import run_load_test

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--clients", type=int, default=10)
    parser.add_argument("--duration", type=int, default=30)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    run_load_test(
        clients=args.clients,
        duration=args.duration,
        timeout=args.timeout
    )

if __name__ == "__main__":
    main()
