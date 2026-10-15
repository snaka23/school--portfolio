def secure_archive(
    filename: str,
    act: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if act == "write":
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        return (True, data)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("master.passwd"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", result[1]))


if __name__ == "__main__":
    main()
