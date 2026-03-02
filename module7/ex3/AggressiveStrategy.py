"""Implementation of the Aggressive Strategy for the DataDeck Engine."""
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete strategy that prioritizes attacking and dealing damage."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Executes an aggressive turn.
        Plays multiple cards if possible and calculates total damage.
        """
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in list(hand):
            if card.name in ["Goblin Warrior", "Lightning Bolt"]:
                res = card.play({})
                cards_played.append(card.name)
                mana_used += res.get("mana_used", 0)

                if hasattr(card, "attack_power"):
                    battlefield.append(card)
                if "damage" in str(res.get("effect", "")):
                    damage_dealt += 3

        for creature in battlefield:
            if hasattr(creature, "attack_power"):
                damage_dealt += creature.attack_power

        targets = self.prioritize_targets(["Enemy Player", "Enemy Creature"])

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": [targets[0]],
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        """Returns the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioritizes targets based on aggressive logic.
        Enemy Player is always the top priority.
        """
        priority_list = sorted(
            available_targets,
            key=lambda x: 0 if x == "Enemy Player" else 1
        )
        return priority_list
