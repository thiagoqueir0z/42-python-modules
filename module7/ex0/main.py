"""Tests the Abstract Base Class design and the CreatureCard implementation."""
from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrates the functionality of the DataDeck Card Foundation."""
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    card_info = dragon.get_card_info()
    card_info.update({"type": "Creature", "attack": dragon.attack,
                      "health": dragon.health})
    print(card_info)

    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")

    game_state: dict = {"active_creatures": []}
    play_result = dragon.play(game_state)
    print(f"Play result: {play_result}")

    print(f"\n{dragon.name} attacks Goblin Warrior:")
    attack_result = dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
