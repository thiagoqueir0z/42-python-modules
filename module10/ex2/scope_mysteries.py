from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        try:
            count += 1
            return count
        except Exception:
            return 0
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        try:
            total_power += amount
            return total_power
        except Exception:
            return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        try:
            return f"{enchantment_type} {item_name}"
        except Exception:
            return "Unknown enchantment"
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: any) -> None:
        try:
            vault[key] = value
        except Exception:
            pass

    def recall(key: str) -> any:
        try:
            return vault.get(key, "Memory not found")
        except Exception:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")

    print(flame_factory("Sword"))
    print(ice_factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    print("Store 'secret' = 42")
    vault['store']('secret', 42)

    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
