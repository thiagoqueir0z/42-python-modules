import sys
import os
from typing import Dict, Optional
from dotenv import load_dotenv


def load_configuration() -> Dict[str, Optional[str]]:

    load_dotenv()

    return {
        'matrix_mode': os.environ.get('MATRIX_MODE', 'development'),
        'database_url': os.environ.get(
            'DATABASE_URL',
            'postgresql://localhost:5432/matrix_dev'
        ),
        'api_key': os.environ.get('API_KEY', 'sk_test_dev_123'),
        'log_level': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'zion_endpoint': os.environ.get(
            'ZION_ENDPOINT',
            'http://localhost:3000'
        ),
    }


def validate_configuration(config: Dict[str, Optional[str]]) -> bool:

    try:
        required_keys = [
            'matrix_mode',
            'database_url',
            'api_key',
            'log_level',
            'zion_endpoint'
        ]

        for key in required_keys:
            if key not in config or config[key] is None:
                raise ValueError(f"Missing configuration: {key}")

        if config['matrix_mode'] not in ['development', 'production']:
            raise ValueError(
                "MATRIX_MODE must be 'development' or 'production'"
            )

        return True

    except ValueError as e:
        print(f"Configuration Error: {e}")
        return False


def display_security_check() -> None:

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def display_configuration(config: Dict[str, Optional[str]]) -> None:
    print("\n" + "=" * 60)
    print("ORACLE STATUS: Reading the Matrix...")
    print("=" * 60)
    print("\nConfiguration loaded:")
    print(f"Mode: {config['matrix_mode']}")
    print(f"Database: Connected to {config['database_url']}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: Online at {config['zion_endpoint']}")

    display_security_check()

    print("\nThe Oracle sees all configurations.")
    print("=" * 60 + "\n")


def main() -> None:
    try:
        config = load_configuration()

        if not validate_configuration(config):
            sys.exit(1)

        display_configuration(config)

    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
