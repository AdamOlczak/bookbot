import sys

from book import report


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    filename = sys.argv[1]
    report(filename)


def usage():
    print(f"Usage: {sys.argv[0]} filename")
    print()
    print("Arguments:")
    print("\tfilename - filename of the book in books/ directory")


if __name__ == "__main__":
    main()
