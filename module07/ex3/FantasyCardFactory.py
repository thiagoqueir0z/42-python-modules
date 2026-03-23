"""
Fantasy-themed concrete factory implementation for DataDeck.
Handles the creation of dragons, goblins, and elemental spells.
"""
import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """
    Concrete factory to create fantasy-themed cards.
    Supports dragons, elemental spells, and magical artifacts.
    """

    def __init__(self) -> None:
        """Initializes the factory with theme-specific card data."""
        self._creatures = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 2, 2),
        ]
        self._spells = [
            ("Fireball", 4, "Rare", "damage"),
            ("Lightning Bolt", 3, "Common", "damage"),
        ]
        self._artifacts = [
            ("Mana Ring", 2, "Rare", 6, "+1 mana per turn"),
            ("Mana Crystal", 2, "Rare", 5, "+1 mana per turn"),
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates a fantasy creature by name or random power level."""
        if isinstance(name_or_power, str):
            for name, cost, rarity, atk, hp in self._creatures:
                if name == name_or_power:
                    return CreatureCard(name, cost, rarity, atk, hp)

        name, cost, rarity, atk, hp = random.choice(self._creatures)
        if isinstance(name_or_power, int):
            atk = name_or_power  # Override power if int is provided
        return CreatureCard(name, cost, rarity, atk, hp)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates an elemental spell by name or random choice."""
        if isinstance(name_or_power, str):
            for name, cost, rarity, et in self._spells:
                if name == name_or_power:
                    return SpellCard(name, cost, rarity, et)

        name, cost, rarity, et = random.choice(self._spells)
        return SpellCard(name, cost, rarity, et)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates a magical artifact by name or random durability."""
        if isinstance(name_or_power, str):
            for name, cost, rarity, dur, eff in self._artifacts:
                if name == name_or_power:
                    return ArtifactCard(name, cost, rarity, dur, eff)

        name, cost, rarity, dur, eff = random.choice(self._artifacts)
        if isinstance(name_or_power, int):
            dur = name_or_power
        return ArtifactCard(name, cost, rarity, dur, eff)

    def create_themed_deck(self, size: int) -> dict:
        """Generates a collection of random fantasy cards."""
        deck = []
        for _ in range(size):
            pick = random.choice(['creature', 'spell', 'artifact'])
            if pick == 'creature':
                deck.append(self.create_creature())
            elif pick == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {'size': size, 'cards': deck}

    def get_supported_types(self) -> dict:
        """Returns the dictionary of supported types as per PDF example."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
