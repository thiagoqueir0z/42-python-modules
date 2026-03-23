"""
Abstract interface for the Strategy Pattern in the DataDeck Engine.
Defines the protocol for turn execution and target prioritization.
"""
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract base class defining a game strategy.
    Encapsulates the decision-making logic for turn execution.
    """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Processes a full game turn based on current hand and battlefield state.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Returns the identifiable name of the strategy.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        Determines the order of targets to attack or affect.
        """
        pass
