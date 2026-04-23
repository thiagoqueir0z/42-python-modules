def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(artifacts, key=lambda x: x['power'], reverse=True)
    except (KeyError, TypeError):
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda m: m['power'] >= min_power, mages))
    except (KeyError, TypeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda s: f"* {s} *", spells))
    except Exception:
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        if not mages:
            return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
        powers = list(map(lambda x: x['power'], mages))
        return {
            'max_power': max(powers),
            'min_power': min(powers),
            'avg_power': round(sum(powers) / len(powers), 2)
        }
    except (KeyError, TypeError, ZeroDivisionError):
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


def main():
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}
    ]

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    if len(sorted_arts) >= 2:
        print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
              f"comes before {sorted_arts[1]['name']} "
              f"({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
