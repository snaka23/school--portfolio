def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    value = "25"
    print(f"Input data is '{value}'")
    try:
        temperature = input_temperature(value)
        print(f"Temperature is now {temperature}℃")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    value = "abc"
    print(f"Input data is '{value}'")
    try:
        temperature = input_temperature(value)
        print(f"Temperature is now {temperature}℃")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
