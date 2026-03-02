"""
GameEngine module for DataDeck.
Orchestrates the interaction between card factories and game strategies.
"""
from typing import Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Simulates game turns using a card factory and strategy.
    Tracks turns, damage, and game state.
    """

    def __init__(self) -> None:
        """Initializes the engine with empty state."""
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configures the engine with a specific factory and strategy."""
        self.factory = factory
        self.strategy = strategy
        deck_data = factory.create_themed_deck(3)
        self.hand = deck_data.get('cards', [])
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        """
        Executes a turn using the current strategy.
        Raises RuntimeError if the engine is not configured.
        """
        if self.factory is None or self.strategy is None:
            raise RuntimeError(
                "Engine not configured with factory or strategy"
            )

        self.turns_simulated += 1
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)

        actions = turn_result.get("actions", {})
        damage = actions.get("damage_dealt", 0)
        self.total_damage += damage

        return turn_result

    def get_engine_status(self) -> dict:
        """Returns a summary of the game state and statistics."""
        strategy_name = (
            self.strategy.get_strategy_name() if self.strategy else None
        )
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
