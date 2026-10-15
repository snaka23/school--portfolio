import os
import site
import sys


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    venv_name = os.environ.get("VIRTUAL_ENV", sys.prefix)
    return os.path.basename(venv_name)


def get_site_packages_path() -> str:
    return site.getsitepackages()[0]


def print_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def print_inside_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print(f"Package installation path: {get_site_packages_path()}")


def main() -> None:
    try:
        if is_venv():
            print_inside_venv()
        else:
            print_outside_venv()
    except OSError as e:
        print(f"error occurred: {e}")


if __name__ == "__main__":
    main()
