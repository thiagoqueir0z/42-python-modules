"""Module to integrate all garden management error handling concepts."""


class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class WaterError(GardenError):
    """Exception raised for irrigation-specific problems."""
    pass


def check_plant_health(name: str, water: int, sun: int) -> str:
    """Validate plant health parameters."""
    if not name:
        raise ValueError("Plant name cannot be empty!")
    if water < 1 or water > 10:
        raise ValueError(f"Water level {water} is too high (max 10)")
    if sun < 2 or sun > 12:
        raise ValueError(f"Sunlight hours {sun} is out of range (2-12)")
    return f"{name}: healthy (water: {water}, sun: {sun})"


def water_plants(plants: list) -> None:
    """Simulate watering plants with a finally block for cleanup."""
    print("Opening watering system")
    try:
        for plant in plants:
            print(f"Watering {plant} - success")
    finally:
        print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    """Run the integrated garden management test suite."""
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    plants_to_add = ["tomato", "lettuce", ""]
    valid_plants = []
    for p in plants_to_add:
        try:
            if not p:
                raise ValueError("Plant name cannot be empty!")
            print(f"Added {p} successfully")
            valid_plants.append(p)
        except ValueError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    water_plants(valid_plants)

    print("\nChecking plant health...")
    plant_data = [("tomato", 5, 8), ("lettuce", 15, 8)]
    for name, water, sun in plant_data:
        try:
            print(check_plant_health(name, water, sun))
        except ValueError as e:
            print(f"Error checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
