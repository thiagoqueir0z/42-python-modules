"""Module to demonstrate command-line argument processing using sys.argv."""

import sys


def process_commands() -> None:
    """
    Retrieve and display arguments from the command line.

    This function identifies the program name, counts total arguments,
    and iterates through user-provided inputs to display them with indices.
    """
    print("=== Command Quest ===")

    argc: int = len(sys.argv)
    script_name = sys.argv[0]

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")

    print(f"Program name: {script_name}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    process_commands()
