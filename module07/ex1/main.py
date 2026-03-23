"""Main demonstration script for Exercise 1: Deck Builder."""
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """Demonstrates the DataDeck Deck Builder functionality."""
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    bolt = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="damage"
    )

    crystal = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=5,
        effect="+1 mana per turn"
    )

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    deck = Deck()
    deck.add_card(bolt)
    deck.add_card(crystal)
    deck.add_card(dragon)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:\n")
    game_state = {"mana": 10, "active_creatures": [], "active_artifacts": []}

    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")

            result = card.play(game_state)
            print(f"Play result: {result}\n")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
