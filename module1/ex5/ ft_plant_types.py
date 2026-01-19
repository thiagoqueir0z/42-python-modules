"""Module for specialized plant types using inheritance and polymorphism."""

class SecurePlant:
    """Base class with security validation for plants."""

    def __init__(self, name: str) -> None:
        """Initializes base plant attributes."""
    self.name = name.capitalize()
    self._height = 0
    self._age = 0

    def set_height(self, value: int) -> None:
        """Validates height (must be positive)"""
        if value >= 0:
            self._height = value
        else:
            print(f"Security: Negative height rejected for {self.name}")

    def display_status(self) -> None:
        """Base display method"""
        print(f"Plant: {self.name} | height: {self._height}cm")


class Flower(SecurePlant):
    """Specialized plant that has a color and can bloom"""

    def __init__(self, name: str, color: str) -> None:
        