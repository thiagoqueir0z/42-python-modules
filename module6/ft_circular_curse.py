# ft_circular_curse.py
from alchemy.grimoire import validate_ingredients, record_spell


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    res_v1 = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {res_v1}')

    res_v2 = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {res_v2}')

    print("\nTesting spell recording with validation:")
    res_r1 = record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {res_r1}')

    res_r2 = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {res_r2}')

    print("\nTesting late import technique:")
    res_r3 = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {res_r3}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
