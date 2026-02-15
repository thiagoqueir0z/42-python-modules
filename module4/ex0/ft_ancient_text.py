"""Module for recovering ancient texts using manual file handling."""


def recover_text(filename: str) -> None:
    """Read and display file content with manual resource management."""
    file = None
    try:
        file = open(filename, 'r')
        print("--- Recovered Fragment ---")
        print(file.read())
    except FileNotFoundError:
        print(f"Error: Vault '{filename}' not found.")
    except Exception as error_message:
        print(f"An unexpected corruption occurred: {error_message}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    recover_text("ancient_fragment.txt")
