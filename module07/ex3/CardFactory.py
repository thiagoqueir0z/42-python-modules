"""Abstract factory interface for the DataDeck card creation system."""
from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract factory defining methods to create cards and
    themed decks for different card types.
    """

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates a creature card based on name or power level."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates a spell card based on name or power level."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates an artifact card based on name or power level."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Generates a complete deck of cards with a specific theme."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Returns the types of cards this factory can produce."""
        pass
