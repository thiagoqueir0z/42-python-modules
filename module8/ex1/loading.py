import sys
import importlib
from typing import Dict, Tuple, Optional


REQUIRED_PACKAGES: Dict[str, str] = {
    "pandas": "2.0.0",
    "numpy": "1.24.0",
    "matplotlib": "3.7.0",
    "requests": "2.31.0",
}


def check_import(package_name: str) -> Tuple[bool, Optional[str]]:
    """
    Check if a package is installed and get its version.

    Args:
        package_name: Name of the package to check.

    Returns:
        Tuple[bool, Optional[str]]: (is_installed, version)
    """
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'Unknown')
        return (True, version)
    except ImportError:
        return (False, None)


def check_all_dependencies() -> Dict[str, Tuple[bool, Optional[str]]]:
    """
    Check all required packages and their versions.

    Returns:
        Dict[str, Tuple[bool, Optional[str]]]: Status of each package.
    """
    return {
        package: check_import(package)
        for package in REQUIRED_PACKAGES.keys()
    }


def display_loading_status(
    dependency_status: Dict[str, Tuple[bool, Optional[str]]]
) -> None:
    """
    Display the current status of all dependencies.

    Args:
        dependency_status: Result from check_all_dependencies().
    """
    print("\n" + "=" * 60)
    print("LOADING STATUS: Loading programs...")
    print("=" * 60)
    print("Checking dependencies:\n")

    for package, (is_installed, version) in dependency_status.items():
        status_icon = "[OK]" if is_installed else "[MISSING]"
        version_info = version if version else "Not installed"
        print(f"{status_icon} {package:15} ({version_info})")

    print("=" * 60 + "\n")


def load_matrix_data() -> Tuple[Optional[object], Optional[object]]:
    """
    Load or simulate Matrix data for analysis.

    Returns:
        Tuple[Optional[object], Optional[object]]: (DataFrame, threat_array)
    """
    try:
        import pandas as pd
        import numpy as np

        np.random.seed(42)

        data = {
            'agent_id': np.arange(1, 101),
            'threat_level': np.random.randint(1, 10, 100),
        }
        df = pd.DataFrame(data)

        return df, np.array(data['threat_level'])
    except Exception as e:
        print(f"Warning: Could not load data: {e}")
        return None, None


def analyze_data(df: Optional[object], threats: Optional[object]) -> None:
    """
    Analyze and visualize Matrix data.

    Args:
        df: DataFrame with data.
        threats: Array with threat levels.
    """
    try:
        if df is None or threats is None:
            print("WARNING: Cannot analyze without pandas/numpy\n")
            return

        print("Analyzing Matrix data...")
        print(f"Processing {len(df)} data points...")
        print(f"Average threat level: {threats.mean():.2f}")
        print(f"Maximum threat level: {threats.max()}\n")

        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.plot(df['agent_id'], threats, marker='o')
        plt.xlabel('Agent ID')
        plt.ylabel('Threat Level')
        plt.title('Matrix Threat Assessment')
        plt.grid(True, alpha=0.3)
        plt.savefig('matrix_analysis.png')
        print("Visualization saved to: matrix_analysis.png\n")
        plt.close()

    except Exception as e:
        print(f"Error during analysis: {e}\n")


def main() -> None:
    """
    Main function to execute the program.
    """
    print("\n" + "=" * 60)
    print("MATRIX: LOADING PROGRAMS")
    print("=" * 60 + "\n")

    dependencies = check_all_dependencies()
    display_loading_status(dependencies)

    df, threats = load_matrix_data()
    analyze_data(df, threats)

    print("=" * 60)
    print("Loading complete!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
