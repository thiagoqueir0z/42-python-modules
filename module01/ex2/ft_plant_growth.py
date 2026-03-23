class Plant:
    """Represents a plant in the garden with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a new plant instance."""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow(self, cm: int = 1) -> None:
        """Increases the plant's height by a given amount."""
        self.height += cm

    def age_plant(self) -> None:
        """Increases the plant's age by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Returns a string with the current plant status."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth() -> None:
    """Simulates a week of growth for a Rose."""
    rose = Plant("rose", 25, 30)
    initial_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(6):
        rose.grow(1)
        rose.age_plant()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
