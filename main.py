import sys

from text import report


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    filepath = sys.argv[1]
    report(filepath)


def usage():
    print(
        "Analyzes and proivides text statistics on the given text file.",
        file=sys.stderr,
    )
    print(file=sys.stderr)
    print(f"Usage: {sys.argv[0]} filename", file=sys.stderr)
    print(file=sys.stderr)
    print("Arguments:", file=sys.stderr)
    print("\tfilename - filepath to the document to be analyzed", file=sys.stderr)


if __name__ == "__main__":
    main()
