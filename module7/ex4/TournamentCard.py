"""
TournamentCard implementation using multiple inheritance.
Combines base card properties, combat mechanics, and ranking capabilities.
"""
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Enhanced card class for tournament play.
    Inherits from Card, Combatable, and Rankable.
    """

    def __init__(self, n: str, c: int, r: str, a: int, h: int, br: int = 1200):
        """Initializes a tournament-ready card with ranking stats."""
        super().__init__(n, c, r)
        self.attack_power = a
        self.health = h
        self._wins = 0
        self._losses = 0
        self._rating = br

    def play(self, game_state: dict) -> dict:
        """Processes the card entering a tournament match."""
        return {
            **game_state,
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the battlefield"
        }

    def attack(self, target: str) -> dict:
        """Executes a tournament-style attack."""
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "tournament"
        }

    def defend(self, incoming_damage: int) -> dict:
        """Handles damage mitigation using tournament rules."""
        blocked = min(self.attack_power, incoming_damage)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': blocked,
            'still_alive': self.health > 0
        }

    def calculate_rating(self) -> int:
        """Returns the current ELO rating."""
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Updates wins and adjusts rating (approx. +16 per win)."""
        if wins < 0:
            raise ValueError("Wins must be non-negative")
        self._wins += wins
        self._rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        """Updates losses and adjusts rating (approx. -16 per loss)."""
        if losses < 0:
            raise ValueError("Losses must be non-negative")
        self._losses += losses
        self._rating -= (losses * 16)

    def get_rank_info(self) -> dict:
        """Returns the ranking data structure."""
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses
        }

    def get_combat_stats(self) -> dict:
        """Returns core combat attributes."""
        return {
            'attack': self.attack_power,
            'health': self.health
        }

    def get_tournament_stats(self) -> dict:
        """Consolidates identity, ranking, and combat data."""
        info = self.get_rank_info()
        return {
            "name": self.name,
            "rating": info["rating"],
            "record": f'{info["wins"]}-{info["losses"]}',
            "combat": self.get_combat_stats()
        }
