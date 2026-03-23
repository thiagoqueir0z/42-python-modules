"""Module defining the abstract base class for the DataDeck system."""
from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract Base Class representing the universal blueprint for cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract method to define the logic when a card is played."""
        pass

    def get_card_info(self) -> dict:
        """Concrete method that returns a dictionary with basic card data."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Concrete method to check if the player has enough mana to play."""
        return available_mana >= self.cost
