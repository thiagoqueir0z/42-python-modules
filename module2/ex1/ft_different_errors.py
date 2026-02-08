"""Module to demonstrate specific built-in exception handling."""


def garden_operations(task: str) -> None:
    """Execute garden tasks and catch specific errors with formatted output."""
    try:
        if task == "value":
            int("abc")
        elif task == "division":
            _ = 42 / 0
        elif task == "file":
            open("missing.txt", "r")
        elif task == "my_dict":
            garden = {"plant": "rose"}
            _ = garden["missing_plant"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    try:
        if task == "multiple":
            raise TypeError("multiple error test")
    except (IndexError, TypeError, AttributeError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """Test function to match the exact output of the subject."""
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    garden_operations("value")

    print("Testing ZeroDivisionError...")
    garden_operations("division")

    print("Testing FileNotFoundError...")
    garden_operations("file")

    print("Testing KeyError...")
    garden_operations("my_dict")

    print("Testing multiple errors together...")
    garden_operations("multiple")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
