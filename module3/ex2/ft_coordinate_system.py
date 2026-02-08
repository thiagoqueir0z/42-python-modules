"""Module to track 3D positions using immutable tuples."""

import sys


def track_position(args: list[str]) -> None:
    """
    Process 3D coordinates and simulate a movement.

    Args:
        args: List of strings representing X, Y, Z coordinates.
    """
    print("=== Position Tracker ===")

    if len(args) != 3:
        print("Error: Exactly 3 coordinates (X Y Z) are required.")
        return

    try:
        initial_pos = (float(args[0]), float(args[1]), float(args[2]))
    except ValueError:
        print("Error: All coordinates must be numeric values.")
        return

    x, y, z = initial_pos

    offset = 10.0
    new_pos = (x + offset, y + offset, z + offset)

    print(f"Initial Position: {initial_pos}")
    print(f"Movement Offset: +{offset} to all axes")
    print(f"New Position: {new_pos}")


if __name__ == "__main__":
    track_position(sys.argv[1:])
