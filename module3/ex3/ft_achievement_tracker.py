"""Module for tracking and analyzing unique player achievements using sets."""


def analyze_achievements() -> None:
    """
    Perform set operations to analyze and compare player achievements.

    Demonstrates union, intersection, and difference to generate analytics
    matching the PixelMetrics 3000 requirements.
    """
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }

    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    # Union: All unique achievements in the system
    all_unique = alice | bob | charlie
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    # Intersection: Common to all three players
    common_to_all = alice & bob & charlie
    print(f"Common to all players: {common_to_all}")

    # Rare achievements: Finding tags that appear in exactly one set
    # Logic: (A-B-C) | (B-A-C) | (C-A-B)
    rare = (alice - bob - charlie) | (bob - alice - charlie) | (charlie - alice - bob)
    print(f"Rare achievements (1 player): {rare}")

    # Comparison: Alice and Bob
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    analyze_achievements()
