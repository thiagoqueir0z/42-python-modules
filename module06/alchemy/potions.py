import alchemy.elements
from .elements import create_fire, create_water
import alchemy.elements as elm


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    earth_result = alchemy.elements.create_earth()
    fire_result = alchemy.elements.create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    air_result = elm.create_air()
    water_result = elm.create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Brew a wisdom potion using all elements."""
    f = create_fire()
    w = create_water()
    e = elm.create_earth()
    a = elm.create_air()

    result = f"{f}, {w}, {e}, {a}"
    return f"Wisdom potion brewed with all elements: {result}"
