"""Manages a collection of cards by randomization and statistical tracking."""
import random
from ex0.Card import Card


class Deck:
    """
    Management class for a collection of DataDeck cards.
    Supports adding, removing, shuffling, and drawing cards.
    """

    def __init__(self) -> None:
        """Initializes an empty deck."""
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the deck.

        Args:
            card (Card): Any object inheriting from the Card base class.
        """
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Removes the first occurrence of a card by its name.

        Args:
            card_name (str): The name of the card to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffles the cards in the deck using the random module."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """
        Draws (removes and returns) the top card of the deck.

        Returns:
            Optional[Card]: The drawn card or None if the deck is empty.
        """
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        """
        Calculates statistics about the current deck composition.

        Returns:
            dict: Statistics including counts by type and average cost.
        """
        total = len(self._cards)
        if total == 0:
            return {"total_cards": 0, "avg_cost": 0.0}

        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard
        from ex0.CreatureCard import CreatureCard

        for card in self._cards:
            total_cost += card.cost

            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

        avg_cost = total_cost / total

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1)
        }
