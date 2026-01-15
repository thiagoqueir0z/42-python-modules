class Plant:
    """Represents a plant in the garden with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a new plant instance."""
        self.name = name.capitalize()
        self.height = height
        self.age = age


def ft_garden_data_organizer() -> None:
    """Creates plant instances and displays their information."""
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    ft_garden_data_organizer()
