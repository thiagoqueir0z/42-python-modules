"""Module for managing real-time data streams and error logging."""
import sys


def manage_streams() -> None:
    """Read from stdin and route messages to stdout or stderr."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    try:
        arch_id: str = input("\nInput Stream active. Enter archivist ID: ")
        stats: str = input("Input Stream active. Enter status report: ")
    except (KeyboardInterrupt, EOFError):
        print("\n[System] Manual shutdown initiated.", file=sys.stderr)
    else:
        print(f"\n[STANDARD] Archive status from {arch_id}: {stats}")

        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr
        )

        print("[STANDARD] Data transmission complete")
        print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()
