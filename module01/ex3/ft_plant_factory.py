"""Module to create and manage multiple plant instances."""


class Plant:
    """Represents a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes plant attributes."""
        self.name = name.capitalize()
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    """Creates a list of plants and displays them."""
    print("=== Plant Factory Output ===")

    garden = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]

    for plant in garden:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"Total plants created: {len(garden)}")


if __name__ == "__main__":
    ft_plant_factory()
