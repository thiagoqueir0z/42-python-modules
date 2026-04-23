import functools
import time
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = next((a for a in args if isinstance(a, int)), None)
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    return (f"Spell casting failed after "
                            f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    # Test 1: Spell Timer
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    # Test 2: Retry Spell
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise Exception("Mana leak!")

    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    # Test 3: MageGuild
    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire Blast", 5))


if __name__ == "__main__":
    main()
