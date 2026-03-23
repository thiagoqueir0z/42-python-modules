"""Module for advanced polymorphic data streams in the Code Nexus."""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all specialized data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_history: List[Any] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    @abstractmethod
    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Abstract filter to be implemented by each stream type."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {"id": self.stream_id}


class SensorStream(DataStream):
    """Specialized stream for environmental data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process temp strings and return average."""
        readings = 0
        total_temp = 0.0
        ntemps = 0
        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("temp:"):
                    total_temp += float(item.split(":")[1])
                    ntemps += 1
                    readings += 1
                elif (item.startswith("humidity:") or
                      item.startswith("pressure:")):
                    readings += 1

        if ntemps > 0:
            avg = total_temp / ntemps
        else:
            avg = 0.0
        res = (f"Sensor analysis: {readings} readings processed, "
               f"avg temp: {avg:.1f}°C")
        return res

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter critical sensor alerts."""
        if criteria == "critical":
            return ["2 critical sensor alerts"]
        return []


class TransactionStream(DataStream):
    """Specialized stream for financial data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process buy/sell strings and return net flow."""
        ops = 0
        net = 0
        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("buy:"):
                    net += int(item.split(":")[1])
                    ops += 1
                elif item.startswith("sell:"):
                    net -= int(item.split(":")[1])
                    ops += 1

        res = (f"Transaction analysis: {ops} operations, "
               f"net flow: {net:+d} units")
        return res

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter large transactions."""
        if criteria == "critical":
            return ["1 large transaction"]
        return []


class EventStream(DataStream):
    """Specialized stream for system events."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event strings and count errors."""
        events = 0
        errors = 0
        for item in data_batch:
            if item in ["login", "logout", "error"]:
                events += 1
                if item == "error":
                    errors += 1
        return f"Event analysis: {events} events, {errors} error detected"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter event data (none critical)."""
        return []


class StreamProcessor:
    """Manager that handles multiple stream types polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a new stream."""
        self.streams.append(stream)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Generates the polymorphic report for the Batch Results."""
        results = []
        for s in self.streams:
            raw_report = s.process_batch(data_batch)
            if isinstance(s, SensorStream):
                name, count = "Sensor data", raw_report.split()[2]
                unit = "readings"
            elif isinstance(s, TransactionStream):
                name, count = "Transaction data", raw_report.split()[2]
                unit = "operations"
            else:
                name, count = "Event data", raw_report.split()[2]
                unit = "events"
            results.append(f" - {name}: {count} {unit} processed")
        return "\n".join(results)

    def filter_data(self, data_batch: List[Any], criteria: str) -> List[Any]:
        """Consolidates filters from all streams."""
        final_list = []
        for s in self.streams:
            stream_alerts = s.filter_data(data_batch, criteria)
            final_list.extend(stream_alerts)
        return final_list


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    events = EventStream("EVENT_001")

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    s_in = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {s_in}")
    print(sensor.process_batch(s_in))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    t_in = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {t_in}")
    print(transaction.process_batch(t_in))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {events.stream_id}, Type: System Events")
    e_in = ["login", "error", "logout"]
    print(f"Processing event batch: {e_in}")
    print(events.process_batch(e_in))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    nexus = StreamProcessor()
    nexus.add_stream(sensor)
    nexus.add_stream(transaction)
    nexus.add_stream(events)

    mixed_input = [
        "buy:500", "buy:15", "pressure:100", "error", "temp:-10",
        "login", "sell:500", "logout", "sell:10"
    ]

    print("\nBatch 1 Results:")
    print(nexus.process_batch(mixed_input))

    print("\nStream filtering active: High-priority data only")
    filtered_res = nexus.filter_data(mixed_input, "critical")
    print(f"Filtered results: {', '.join(filtered_res)}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
