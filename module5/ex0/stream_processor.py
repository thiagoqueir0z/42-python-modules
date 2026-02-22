"""Module for foundational data processing in the Code Nexus."""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    def __init__(self, name: str) -> None:
        """Initialize the processor with a name."""
        self.name: str = name

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method to be implemented by subclasses."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstract method for data validation."""
        pass

    def format_output(self, result: str) -> str:
        """Standard formatting for the output string."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized in numerical data streams."""

    def validate(self, data: Any) -> bool:
        """Check if data is a list of numbers."""
        if not isinstance(data, list):
            return False

        for x in data:
            if not isinstance(x, (int, float)):
                return False

        print("Validation: Numeric data verified")
        return True

    def process(self, data: Any) -> str:
        """Process numbers using a classic average calculation."""
        if not self.validate(data):
            raise ValueError("Numeric data verification failed")

        count = len(data)
        total = sum(data)
        if count > 0:
            avg = total / count
        else:
            avg = 0.0

        res_str = f"Processed {count} numeric values, sum={total}, avg={avg}"
        return self.format_output(res_str)


class TextProcessor(DataProcessor):
    """Processor specialized in text data streams."""

    def validate(self, data: Any) -> bool:
        """Check if data is a string."""
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def process(self, data: Any) -> str:
        """Process text and return formatted result."""
        if not self.validate(data):
            raise ValueError("Text data verification failed")

        chars = len(data)
        words = len(data.split())
        res_str = f"Processed text: {chars} characters, {words} words"
        return self.format_output(res_str)


class LogProcessor(DataProcessor):
    """Processor specialized in log entries with dynamic severity detection."""

    def validate(self, data: Any) -> bool:
        """Check for log format (Level: Message)."""
        if isinstance(data, str):
            if ":" in data:
                print("Validation: Log entry verified")
                return True
        return False

    def format_output(self, result: str) -> str:
        """Override to add smart tags using classic conditional logic."""
        if "ERROR" in result:
            tag = "[ALERT]"
        else:
            tag = "[INFO]"

        return f"Output: {tag} {result}"

    def process(self, data: Any) -> str:
        """Process logs and delegate tag logic to format_output."""
        if not self.validate(data):
            raise ValueError("Log entry verification failed")

        level_raw, content = data.split(':', 1)
        level = level_raw.strip().upper()

        res_str = f"{level} level detected: {content.strip()}"
        return self.format_output(res_str)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    p_num = NumericProcessor("Numeric Processor")
    p_text = TextProcessor("Text Processor")
    p_log = LogProcessor("Log Processor")

    initial_tasks = [
        (p_num, [1, 2, 3, 4, 5]),
        (p_text, "Hello Nexus World"),
        (p_log, "ERROR: Connection timeout")
    ]

    for proc, data in initial_tasks:
        print(f"\nInitializing {proc.name}...")

        if isinstance(data, str):
            d_view = f'"{data}"'
        else:
            d_view = data

        print(f"Processing data: {d_view}")

        try:
            print(proc.process(data))
        except Exception as e:
            print(f"Status: Breach detected. Error: {e}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    demo_tasks = [
        (p_num, [2, 2, 2]),
        (p_text, "Hello World!"),
        (p_log, "INFO: System ready")
    ]

    for i, (proc, data) in enumerate(demo_tasks, 1):
        try:
            raw_result = proc.process(data)

            clean_res = raw_result.replace("Output: ", "")
            print(f"Result {i}: {clean_res}")
        except Exception as e:
            print(f"Result {i}: Failed. Error: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
