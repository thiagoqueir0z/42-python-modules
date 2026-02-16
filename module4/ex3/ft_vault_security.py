"""Module for secure vault access using context managers."""


def secure_vault_inspection(filename: str) -> None:
    """
    Open a vault for inspection and ensure automatic closure.

    Args:
        filename (str): The path to the vault file to be inspected.
    """
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")

        with open(filename, 'r') as vault:
            print("Vault connection established with failsafe protocols\n")

            content: str = vault.read()

            print("SECURE EXTRACTION:")
            print(content)
            print("\nSECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")

        print("\nAll vault operations completed with maximum security.")

    except FileNotFoundError:
        print(f"CRISIS: Access failed - Vault '{filename}' not found.")
    except Exception as error_message:
        print(f"CRITICAL: Unexpected security breach: {error_message}")


if __name__ == "__main__":
    secure_vault_inspection("classified_data.txt")
