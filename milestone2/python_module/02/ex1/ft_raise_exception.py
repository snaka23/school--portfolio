def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}℃ is too hot for plants (max 40℃)")
    if temperature < 0:
        raise ValueError(f"{temperature}℃ is too cold for plants (min 0℃)")
    return temperature


def test_temperature() -> None:
    values = ["25", "abc", "100", "-50"]
    for value in values:
        print(f"Input data is '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}℃")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
