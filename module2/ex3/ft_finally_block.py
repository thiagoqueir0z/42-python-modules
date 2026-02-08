"""Module to demonstrate the use of finally blocks for resource cleanup."""


def water_plants(plant_list: list) -> None:
    """
    Simulate watering plants and ensure the system closes properly.

    Args:
        plant_list (list): A list of plant names to be watered.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        # This block must always run to simulate closing a real valve
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrate system behavior with normal and erroneous inputs."""
    print("=== Garden Watering System ===")

    # Scenario 1: Normal watering
    print("\nTesting normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)

    # Scenario 2: Error in the list
    print("\nTesting with error...")
    bad_plants = ["tomato", None]
    water_plants(bad_plants)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
