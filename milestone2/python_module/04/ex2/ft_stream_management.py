import sys
import typing


def main() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO[str] = open(sys.argv[1], "r", encoding="utf-8")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return
    content = f.read()
    print("---")
    print()
    print(content)
    print()
    print("---")
    f.close()
    print(f"File '{sys.argv[1]}' closed.")
    print()
    lines = content.splitlines()
    new_content = ""
    for line in lines:
        new_content += line + "#\n"
    print("Transform data:")
    print("---")
    print()
    print(new_content)
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    line = sys.stdin.readline()
    filename = line.rstrip("\n")
    if filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{filename}'")
    try:
        nf: typing.IO[str] = open(filename, "w", encoding="utf-8")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        print("Data not saved.")
        return
    nf.write(new_content)
    print(f"Data saved in file '{filename}'")
    nf.close()


if __name__ == "__main__":
    main()
