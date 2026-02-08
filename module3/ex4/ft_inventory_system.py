"""Module for managing and analyzing game inventory using dictionaries."""

import sys


def analyze_inventory(args: list[str]) -> None:
    """
    Process inventory data and display detailed analytics.

    Args:
        args: List of strings in 'item:quantity' format.
    """
    inventory: dict[str, int] = {}

    for arg in args:
        try:
            name, qty = arg.split(':')
            inventory[name] = int(qty)
        except ValueError:
            continue

    if not inventory:
        print("Inventory is empty.")
        return

    total_items = sum(inventory.values())
    unique_types = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("=== Current Inventory ===")
    for item, quantity in inventory.items():
        percentage = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")

    most_abundant = max(inventory.items(), key=lambda x: x[1])
    least_abundant = min(inventory.items(), key=lambda x: x[1])

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} unit)")

    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"].update({item: qty})
        else:
            categories["Scarce"].update({item: qty})

    print("=== Item Categories ===")
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    restock = [item for item, qty in inventory.items() if qty <= 1]
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_inventory(sys.argv[1:])
    else:
        # Default example matching the PDF if no arguments are provided
        sample = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1"]
        analyze_inventory(sample)