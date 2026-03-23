"""Module for multi-vault crisis response and recovery."""


def crisis_response(vaults: list[str]) -> None:
    """
    Iterate through multiple vaults, handling specific failures for each.

    Args:
        vaults (list[str]): A list of file paths to be inspected.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    for vault_path in vaults:
        try:
            if vault_path == "standard_archive.txt":
                print(
                    f"ROUTINE ACCESS: Attempting access to '{vault_path}'..."
                )
            else:
                print(f"CRISIS ALERT: Attempting access to '{vault_path}'...")

            with open(vault_path, 'r') as vault:
                content = vault.read().strip()
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed\n")

        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")

        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")

        except Exception as error_message:
            print(f"RESPONSE: Unexpected error: {error_message}")
            print("STATUS: System unstable, check protocols\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    target_vaults = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    crisis_response(target_vaults)
