import alchemy.transmutation as transmutation
import alchemy


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {transmutation.basic.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    p_stone = transmutation.advanced.philosophers_stone()
    print(f"philosophers_stone(): {p_stone}")
    print(f"elixir_of_life(): {transmutation.advanced.elixir_of_life()}")

    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())

    print("alchemy.transmutation.philosophers_stone(): [same as above]")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
