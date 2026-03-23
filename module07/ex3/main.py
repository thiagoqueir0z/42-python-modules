"""
Main demonstration script for Exercise 3.
Integrates CardFactory, GameStrategy, and GameEngine patterns.
"""
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    """
    Demonstrates the GameEngine using a FantasyCardFactory
    and AggressiveStrategy to simulate a game turn.
    """
    print("\n=== DataDeck Game Engine ===")

    engine = GameEngine()
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")

    engine.configure_engine(factory, strategy)
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_display = [f"{c.name} ({c.cost})" for c in engine.hand]
    print(f"Hand: {hand_display}")

    print("\nTurn execution:")
    try:
        turn = engine.simulate_turn()
        print(f"Strategy: {turn['strategy']}")
        print(f"Actions: {turn['actions']}")
    except RuntimeError as e:
        print(f"Error: {e}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
