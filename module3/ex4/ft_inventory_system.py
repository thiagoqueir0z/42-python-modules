"""Module for managing and analyzing game inventory using dictionaries."""

import sys


def analyze_inventory(args: list[str]) -> None:
    """Process inventory data and display detailed analytics."""
    inventory: dict[str, int] = {}

    for arg in args:
        try:
            parts = arg.split(':')
            name = parts[0]
            qty = int(parts[1])
            inventory[name] = qty
        except (ValueError, IndexError):
            continue

    if not inventory:
        print("=== Inventory System Analysis ===")
        print("Inventory is empty.")
        return

    total_items = sum(inventory.values())
    unique_types = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        percentage = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")

    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(
        f"Least abundant: {least_abundant} "
        f"({inventory[least_abundant]} unit)"
    )

    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"].update({item: qty})
        else:
            categories["Scarce"].update({item: qty})

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    restock = [item for item, qty in inventory.items() if qty <= 1]
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_inventory(sys.argv[1:])
    else:
        sample_data = [
                        "sword:1",
                        "potion:5",
                        "shield:2",
                        "armor:3",
                        "helmet:1"
        ]
        analyze_inventory(sample_data)
