"""Module to demonstrate raising custom error messages for validation."""


def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    """
    Validate plant health parameters and raise errors if limits are exceeded.

    Args:
        plant_name (str): The name of the plant.
        water_level (int): Water level from 1 to 10.
        sunlight_hours (int): Sunlight hours from 2 to 12.

    Returns:
        str: A success message if all validations pass.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(
            f"Water level {water_level} is too high (max 10)"
        )

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Execute test cases for plant health validation."""
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
