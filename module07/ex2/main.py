"""
Demonstration script for Exercise 2: Ability Layer.
Showcases multiple inheritance and interface introspection.
"""
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main() -> None:
    """
    Main execution function to demonstrate EliteCard capabilities.
    """
    print("=== DataDeck Ability System ===")

    card_methods = ['play', 'get_card_info', 'is_playable']

    combat_methods = []
    for method in dir(Combatable):
        if not method.startswith('_'):
            combat_methods.append(method)

    magic_methods = []
    for method in dir(Magical):
        if not method.startswith('_'):
            magic_methods.append(method)

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    warrior = EliteCard("Arcane Warrior", 5, "Legendary")
    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("Combat phase:")
    attack_res = warrior.attack("Enemy")
    print(f"Attack result: {attack_res}")

    defend_res = warrior.defend(5)
    print(f"Defense result: {defend_res}")

    print("Magic phase:")
    spell_res = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")

    mana_res = warrior.channel_mana(3)
    print(f"Mana channel: {mana_res}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
