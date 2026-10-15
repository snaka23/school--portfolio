import sys
import typing


def main() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO[str] = open(sys.argv[1], "r", encoding="utf-8")
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
