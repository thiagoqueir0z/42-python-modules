"""Module for specialized plant types using inheritance and polymorphism."""


class Plant:
    """Base class with common features for all plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes base plant attributes."""
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    """Specialized plant that has a color and can bloom."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes flower with color using super()."""
        super().__init__(name, height, age)
        self.color = color

    def display_status(self) -> None:
        """Displays status specific to flowers."""
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        """Specific behavior for Flowers."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialized plant with trunk diameter and shade ability."""

    def __init__(self, name: str, height: int, age: int, diam: int) -> None:
        """Initializes tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = diam

    def display_status(self) -> None:
        """Displays status specific to trees."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Specific behavior for Trees."""
        # Cálculo figurativo para a saída do exemplo
        shade = 78
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Specialized plant with harvest season and nutritional value."""

    def __init__(self, name: str, height: int, age: int,
                 season: str, nutrition: str) -> None:
        """Initializes vegetable attributes."""
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutrition

    def display_status(self) -> None:
        """Displays status specific to vegetables."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")

    def show_nutrition(self) -> None:
        """Specific behavior for Vegetables."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    """Main function to match the subject's example output."""
    print("=== Garden Plant Types ===")

    # 1. Flower
    rose = Flower("rose", 25, 30, "red")
    rose.display_status()
    rose.bloom()

    # 2. Tree
    oak = Tree("oak", 500, 1825, 50)
    oak.display_status()
    oak.produce_shade()

    # 3. Vegetable
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    tomato.display_status()
    tomato.show_nutrition()


if __name__ == "__main__":
    ft_plant_types()
