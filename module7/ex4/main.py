"""
Main demonstration script for Exercise 4.
Integrates Multiple Inheritance, Tournament Management, and Ranking.
"""
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """
    Demonstrates registering TournamentCards, running matches,
    and viewing leaderboard and platform reports.
    """
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()
    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", a=7, h=5, br=1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", a=5, h=6, br=1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    d_info = dragon.get_rank_info()
    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {d_info['rating']}")
    print(f"- Record: {d_info['wins']}-{d_info['losses']}")

    w_info = wizard.get_rank_info()
    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {w_info['rating']}")
    print(f"- Record: {w_info['wins']}-{w_info['losses']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} - Rating: {entry['rating']} "
              f"({entry['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("\nAll abstract patterns working together harmoniously!")


if __name__ == '__main__':
    main()
