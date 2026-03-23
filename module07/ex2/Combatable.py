"""
Abstract interface defining combat capabilities for the DataDeck system.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class Combatable(ABC):
    """Abstract base class for entities that can engage in combat."""

    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Calculates and returns the result of an attack on a target.

        Args:
            target (Any): The entity being attacked.

        Returns:
            Dict[str, Any]: A dictionary containing attack details.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Processes incoming damage and returns the defensive result.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            Dict[str, Any]: A dictionary containing defense details.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """
        Retrieves the current combat-related statistics of the entity.

        Returns:
            Dict[str, Any]: A dictionary of combat statistics.
        """
        pass
