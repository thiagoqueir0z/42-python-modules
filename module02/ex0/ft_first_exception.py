"""Module for validating agricultural temperature data."""


def check_temperature(temp_str: str) -> int | None:
    """Validates if temperature is a number and within a safe range."""
    try:
        temperature = int(temp_str)
        if temperature < 0:
            raise ValueError(
                f"{temperature}°C is too cold for plants (min 0°C)"
            )
        if temperature > 40:
            raise ValueError(
                f"{temperature}°C is too hot for plants (max 40°C)"
            )
        print(f"Temperature {temperature}°C is perfect for plants!")
        return temperature

    except ValueError as error:
        if "invalid literal" in str(error):
            print(f"Error: '{temp_str}' is not a valid number")
        else:
            print(f"Error: {error}")
        return None


def test_temperature_input() -> None:
    """Demonstrates the checker with various input scenarios."""
    print("=== Garden Temperature Checker ===")

    print("Testing temperature: 25")
    check_temperature("25")

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature("100")

    print("Testing temperature: -50")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
