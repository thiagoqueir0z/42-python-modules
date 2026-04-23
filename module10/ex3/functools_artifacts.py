import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "min": min,
        "max": max
    }

    try:
        op_func = ops.get(operation)
        if op_func is None:
            raise ValueError(f"Unknown operatiuon {operation}")
        return functools.reduce(op_func, spells)
    except Exception:
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    try:
        if n <= 1:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except Exception:
        return 0


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def main():
    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element} {target} (Power: {power})"

    # Test 1: Reducer
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    # Test 2: Fibonacci
    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    # Test 3: Dispatcher
    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
