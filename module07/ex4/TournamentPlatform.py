"""
TournamentPlatform module for DataDeck.
Manages the registration, matches, and rankings of TournamentCards.
"""
import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Manages tournament cards, matches, and leaderboards,
    tracking ratings and match outcomes.
    """

    def __init__(self) -> None:
        """Initializes the platform with an empty registry."""
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Registers a card and generates a unique tournament ID."""
        name_slug = card.name.lower().replace(' ', '_')
        card_id = f"{name_slug}_{len(self._cards) + 1:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulates a match between two cards and updates their rankings."""
        if card1_id not in self._cards or card2_id not in self._cards:
            raise KeyError("Card ID not found in platform")
        if card1_id == card2_id:
            raise ValueError("A card cannot match against itself")

        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]
        self._matches_played += 1

        # Lógica de combate baseada em rating, poder e um fator aleatório
        p1_score = c1.calculate_rating() + (c1.attack_power * 10)
        p1_score += random.randint(-25, 25)
        p2_score = c2.calculate_rating() + (c2.attack_power * 10)
        p2_score += random.randint(-25, 25)

        if p1_score >= p2_score:
            winner, loser = c1, c2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = c2, c1
            winner_id, loser_id = card2_id, card1_id

        # Atualiza estatísticas (os métodos update já ajustam o rating)
        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        """Returns a list of cards sorted by rating (descending)."""
        board = []
        for card_id, card in self._cards.items():
            info = card.get_rank_info()
            board.append({
                "id": card_id,
                "name": card.name,
                "rating": info["rating"],
                "record": f"{info['wins']}-{info['losses']}"
            })
        # Ordena pelo rating de forma decrescente
        return sorted(board, key=lambda x: x["rating"], reverse=True)

    def generate_tournament_report(self) -> dict:
        """Generates a summary report of the platform activity."""
        total = len(self._cards)
        avg_rating = 0

        if total > 0:
            total_rating = 0
            for card in self._cards.values():
                total_rating += card.calculate_rating()
            avg_rating = int(total_rating / total)

        return {
            "total_cards": total,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active" if total > 0 else "empty"
        }
