def record_spell(name: str, ingredients: str) -> str:
    """Record a spell using a Late Import to avoid circularity."""
    from .validator import validate_ingredients

    status = validate_ingredients(ingredients)
    if "VALID" in status:
        return f"Spell recorded: {name} ({status})"
    return f"Spell rejected: {name} ({status})"
