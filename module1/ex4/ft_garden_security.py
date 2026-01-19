"""Module for a secure garden system that validates plant data."""


class SecurePlant:
    """A plant class that protects its data from invalid values."""

    def __init__(self, name: str) -> None:
        """Initializes the plant with a name and default values."""
        self.name = name.capitalize()
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, value: int) -> None:
        """Validates and sets the plant height."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """Validates and sets the plant age."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        """Returns the protected height value."""
        return self._height

    def get_age(self) -> int:
        """Returns the protected age value."""
        return self._age

    def display_status(self) -> None:
        """Displays the current validated plant information."""
        status = (
            f"Current plant: {self.name} "
            f"({self._height}cm, {self._age} days)"
        )
        print(status)


def ft_garden_security() -> None:
    """Demonstrates the security system by attempting valid and invalid ops."""
    print("=== Garden Security System ===")
    rose = SecurePlant("rose")
    # Operações válidas
    rose.set_height(25)
    rose.set_age(30)
    # Operação inválida (Tentativa de corromper dados)
    rose.set_height(-5)
    # Mostrar status final
    rose.display_status()


if __name__ == "__main__":
    ft_garden_security()
