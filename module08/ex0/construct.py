import sys
import os
import site
from typing import Optional


def detect_virtual_environment() -> bool:

    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and
             sys.base_prefix != sys.prefix))


def get_venv_name() -> Optional[str]:

    try:
        if detect_virtual_environment():
            return os.path.basename(sys.prefix)
        return None
    except Exception as e:
        print(f"Warning: Could not determine venv name: {e}")
        return None


def get_site_packages_path() -> str:

    try:
        return site.getsitepackages()[0]
    except Exception:
        return "Unknown"


def display_inside_venv() -> None:

    venv_name = get_venv_name()
    site_packages = get_site_packages_path()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print(f"\nPackage installation path:\n{site_packages}\n")


def display_outside_venv() -> None:

    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix/MacOS")
    print("matrix_env")
    print("Scripts")
    print("activate     # On Windows")
    print("\nThen run this program again.\n")


def main() -> None:

    try:
        if detect_virtual_environment():
            display_inside_venv()
        else:
            display_outside_venv()
    except Exception as e:
        print(f"ERROR: Unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
