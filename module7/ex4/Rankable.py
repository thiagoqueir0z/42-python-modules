"""
Abstract interface for ranking capabilities in the DataDeck Platform.
Defines the contract for tracking competitive performance and ratings.
"""
from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract base class for objects that track wins, losses,
    and rating, with a customizable ranking calculation.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculates the current rating (ELO) based on performance."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Updates the total count of wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Updates the total count of losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Returns a summary of the ranking statistics."""
        pass
