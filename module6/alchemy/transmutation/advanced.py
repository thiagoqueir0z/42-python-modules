from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Combine results to create the philosopher's stone."""
    result = f"Philosopher's stone created using {lead_to_gold()} and "
    result += f"{healing_potion()}"
    return result


def elixir_of_life() -> str:
    """Return the message for the elixir of life."""
    return "Elixir of life: eternal youth achieved!"
