"""Module for advanced data transformation using Python comprehensions."""


def transform_data() -> None:
    """
    Apply list, set, and dictionary comprehensions to player data.

    Demonstrates the power of concise data transformation as a Data Alchemist.
    """
    players = ["alice", "bob", "charlie", "diana", "eve"]
    scores = [1200, 450, 3000, 800, 1500]
    inventory = [
        {"item": "sword", "rarity": "common"},
        {"item": "potion", "rarity": "rare"},
        {"item": "shield", "rarity": "common"},
        {"item": "gem", "rarity": "legendary"},
        {"item": "herb", "rarity": "rare"}
    ]

    print("=== Data Alchemist Transformation ===")

    high_tier = [p.upper() for p, s in zip(players, scores) if s > 1000]
    print(f"High-tier players (uppercase): {high_tier}")

    rarities = {item["rarity"] for item in inventory}
    print(f"Unique item rarities: {rarities}")

    player_stats = {p: s for p, s in zip(players, scores)}
    print(f"Player stats map: {player_stats}")

    boosted_stats = {p: int(s * 1.1) for p, s in player_stats.items() if s < 1000}
    print(f"Boosted stats (<1000 points + 10%): {boosted_stats}")

    labels = ["Pro" if s >= 1000 else "Noob" for s in scores]
    player_labels = {name: label for name, label in zip(players, labels)}
    print(f"Player classifications: {player_labels}")


if __name__ == "__main__":
    transform_data()
