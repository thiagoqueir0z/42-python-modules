"""Module defining the SpellCard class."""
from ex0.Card import Card


class SpellCard(Card):
    """Concrete class representing a spell card."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """
        Initializes a spell card.

        Args:
            effect_type (str): damage, heal, buff, or debuff.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Implementation of the play method."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect([])
        }

    def resolve_effect(self, targets: list) -> dict:
        """
        Processes instant magical effects on specified targets.

        Args:
            targets (list): List of targets affected by the spell.

        Returns:
            dict: Results of the spell resolution.
        """
        if self.name == "Lightning Bolt":
            return "Deal 3 damage to target"
        return f"Spell effect: {self.effect_type}"
