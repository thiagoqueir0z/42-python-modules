"""
Demonstrates multiple inheritance by combining Card, Combatable, and Magical.
"""
from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Implements all abstract methods from multiple interfaces."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initializes an EliteCard with hybrid stats."""
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.health = 10
        self.mana_pool = 7
        self.effect = "Elite card enters the battlefield"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implements the mandatory play method from Card."""
        return {
            **game_state,
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        """Implements combat attack."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Implements combat defense with damage reduction."""
        taken = int(incoming_damage * 0.4)
        blocked = incoming_damage - taken
        self.health -= taken
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """Returns current combat health and power."""
        return {'attack': self.attack_power, 'health': self.health}

    def cast_spell(
            self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        """Implements magical spellcasting."""
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Implements mana recovery logic."""
        return {
            'channeled': amount,
            'total_mana': self.mana_pool
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        """Returns current magical mana pool."""
        return {'mana': self.mana_pool}
