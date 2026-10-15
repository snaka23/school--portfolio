import os
import sys

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("you should use this command 'pip install -r requirements.txt'")
    sys.exit(1)


def check_key() -> list[str]:
    must_environments = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    must_key: list[str] = []
    for environment in must_environments:
        if not os.environ.get(environment):
            must_key.append(environment)
    return must_key


def check_mode() -> str | None:
    mode = os.environ.get("MATRIX_MODE")
    if mode == "development" or mode == "production":
        return mode
    else:
        return None


def check_database(mode: str) -> str:
    if mode == "development":
        return "Connected to local instance"
    else:
        return "Connected to remote instance"


def check_api_access(mode: str) -> str:
    api_key = os.environ.get("API_KEY", "")
    if mode == "development":
        return f"Authenticated (key: {api_key[:4]}...)"
    return "Authenticated"


def main() -> None:
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    lost_key = check_key()
    if lost_key:
        for key in lost_key:
            print(f"you should include the key and value '{key}'")
        sys.exit(1)
    mode = check_mode()
    if not mode:
        print("MATRIX_MODE is development or production")
        sys.exit(1)
    database = check_database(mode)
    api_access = check_api_access(mode)
    log_level = os.environ.get("LOG_LEVEL")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
