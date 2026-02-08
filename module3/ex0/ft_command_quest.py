"""Module to demonstrate command-line argument processing using sys.argv."""

import sys


def process_commands() -> None:
    """
    Retrieve and display arguments from the command line.

    This function identifies the program name, counts total arguments,
    and iterates through user-provided inputs to display them with indices.
    """
    print("=== Command Quest ===")

    arguments = sys.argv
    total_args = len(arguments)
    script_name = arguments[0]

    if total_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")
        for i, arg in enumerate(arguments[1:], start=1):
            print(f"Argument {i}: {arg}")

    print(f"Program name: {script_name}")
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    process_commands()
