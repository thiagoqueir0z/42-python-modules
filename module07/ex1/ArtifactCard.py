"""Module defining the ArtifactCard class."""
from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete class representing an artifact card."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """
        Initializes an artifact card.

        Args:
            durability (int): How long it lasts.
            effect (str): Description of the permanent ability.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Implementation of the abstract play method for artifacts."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        """
        Implements activate_ability for ongoing effects.

        Returns:
            dict: Results of the ability activation.
        """
        return {
            "artifact": self.name,
            "status": "activated",
            "durability": self.durability
        }
