import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length = len(sys.argv)
    if length < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        i = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i = i + 1
    print(f"Total arguments: {len(sys.argv)}")
