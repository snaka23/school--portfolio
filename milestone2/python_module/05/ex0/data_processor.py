import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for x in data:
                is_valid_number = (
                    isinstance(x, (int, float)) and not isinstance(x, bool))
                if not is_valid_number:
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            values = data
        else:
            values = [data]
        for value in values:
            self._storage.append((self._next_rank, str(value)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            values = data
        else:
            values = [data]
        for value in values:
            self._storage.append((self._next_rank, value))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not (isinstance(key, str) and isinstance(value, str)):
                    return False
            return True
        if isinstance(data, list):
            for entry in data:
                if not isinstance(entry, dict):
                    return False
                for key, value in entry.items():
                    if not (isinstance(key, str) and isinstance(value, str)):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            entries = data
        else:
            entries = [data]
        for entry in entries:
            value = f"{entry['log_level']}: {entry['log_message']}"
            self._storage.append((self._next_rank, value))
            self._next_rank += 1


def main() -> None:
    print("=== code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    numeric.ingest(data)
    count = 3
    print(f"Extracting {count} values...")
    for _ in range(count):
        key, value = numeric.output()
        print(f"Numeric value {key}: {value}")
    print()
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"trying  to validate input '42': {text.validate(42)}")
    text_data: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    count = 1
    text.ingest(text_data)
    print(f"Extracting {count} value...")
    for _ in range(count):
        key, value = text.output()
        print(f"Text value {key}: {value}")
    print()
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying tp validate input 'Hello': {log.validate('Hello')}")
    log_data: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]
    print(f"Processing data: {log_data}")
    count = 2
    print(f"Extracting {count} values...")
    log.ingest(log_data)
    for _ in range(count):
        key, value = log.output()
        print(f"Log entry {key}: {value}")


if __name__ == "__main__":
    main()
