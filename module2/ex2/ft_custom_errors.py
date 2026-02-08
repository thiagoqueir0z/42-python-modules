"""Module to demonstrate custom exception hierarchies in a garden system."""


class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised for irrigation-specific problems."""
    pass


def action_with_plant():
    """Simulates a plant failure."""
    raise PlantError("The tomato plant is wilting!")


def action_with_water():
    """Simulates a water system failure."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrates raising and catching custom exceptions."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        action_with_plant()
    except PlantError as error_message:
        print(f"Caught PlantError: {error_message}")

    print("Testing WaterError...")
    try:
        action_with_water()
    except WaterError as error_message:
        print(f"Caught WaterError: {error_message}")

    print("Testing catching all garden errors...")
    for action in [action_with_plant, action_with_water]:
        try:
            action()
        except GardenError as error_message:
            print(f"Caught a garden error: {error_message}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
