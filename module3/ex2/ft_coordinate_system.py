"""Module to track game positions using 3D coordinate tuples."""

import math


def track_position() -> None:
    """Execute coordinate tracking and distance calculations."""
    print("=== Game Coordinate System ===")

    checkpoint: tuple[int, int, int] = (0, 0, 0)
    point: tuple[int, int, int] = (10, 20, 5)

    print(f"\nPosition created: {point}")

    distance = math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
    print(f"Distance between {checkpoint} and {point}: {distance:.2f}")

    raw_coords = "3,4,0"
    print(f"\nParsing coordinates: \"{raw_coords}\"")

    try:
        parsed_list = [int(n) for n in raw_coords.split(",")]
        parsed_point = tuple(parsed_list)

        print(f"Parsed position: {parsed_point}")

        dist_parsed = math.sqrt(sum(coord**2 for coord in parsed_point))
        print(
            f"Distance between {checkpoint} and {parsed_point}: "
            f"{dist_parsed:.1f}"
        )

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    invalid_coords = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_coords}\"")

    try:
        [int(n) for n in invalid_coords.split(",")]
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed_point
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    track_position()
