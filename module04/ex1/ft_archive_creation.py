"""Module for creating and updating archives in the Cyber Archives."""


def create_archive(filename: str, content: str) -> None:
    """
    Create or overwrite a file with the provided content.

    Args:
        filename (str): The name of the file to be created.
        content (str): The data to be persisted in the archive.
    """
    file = None
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print(f"Initializing new storage unit: {filename}")

        file: str = open(filename, 'w')
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        file.write(content)

        print(content)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except PermissionError:
        print(f"ERROR: Security protocols deny write access to '{filename}'.")
    except Exception as erro_message:
        print(f"CRITICAL ERROR: Failed to create archive: {erro_message}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    archive_name: str = "new_discovery.txt"
    preservation_data: str = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )

    create_archive(archive_name, preservation_data)
