"""Abstract interface defining magical capabilities for the DataDeck system."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class Magical(ABC):
    """Abstract base class for entities with magical abilities."""

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[str, Any]:
        """
        Executes a magical spell on specified targets.

        Args:
            spell_name (str): The name of the spell to cast.
            targets (List[Any]): A list of entities targeted by the spell.

        Returns:
            Dict[str, Any]: A dictionary containing spell resolution details.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """
        Increases the entity's mana pool or processes mana gathering.

        Args:
            amount (int): The amount of mana to channel.

        Returns:
            Dict[str, Any]: A dictionary containing the result.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """
        Retrieves the current magical statistics of the entity.

        Returns:
            Dict[str, Any]: A dictionary of magical statistics.
        """
        pass
