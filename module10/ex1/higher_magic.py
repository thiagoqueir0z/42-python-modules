from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        try:
            return (spell1(target, power), spell2(target, power))
        except Exception:
            return ("Spell Fizzled", "Spell Fizzled")
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        try:
            return base_spell(target, power * multiplier)
        except Exception:
            return ("Spell fizzled")
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        try:
            if condition(target, power):
                return spell(target, power)
            return "Spell Fizzled"
        except Exception:
            return "Spell Fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        results = []
        for spell in spells:
            try:
                results.append(spell(target, power))
            except Exception:
                results.append("Spell Fizzled")
        return results
    return sequence


def main():
    def fireball(t: str, p: int) -> str:
        return f"Fireball hits {t} for {p} damage"

    def heal(t: str, p: int) -> str:
        return f"Heal restores {t} for {p} HP"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 50)}")

    print("\nTesting power amplifier...")
    amplified_fireball = power_amplifier(fireball, 3)
    print(
            f"Original: 10, Amplified result: "
            f" {amplified_fireball('Dragon', 10)}"
        )

    print("\nTesting conditional caster...")
    strong_only = conditional_caster(lambda t, p: p > 20, fireball)
    print(f"Power 25: {strong_only('Orc', 25)}")
    print(f"Power 15: {strong_only('Orc', 15)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(f"Sequence results: {sequence('Ally', 30)}")


if __name__ == "__main__":
    main()
