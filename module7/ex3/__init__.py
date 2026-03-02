"""
Package initialization for Exercise 3.
Exposes the GameEngine, FantasyCardFactory, and AggressiveStrategy.
"""
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

__all__ = [
    'GameEngine',
    'FantasyCardFactory',
    'AggressiveStrategy'
]
