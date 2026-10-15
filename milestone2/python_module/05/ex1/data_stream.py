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

    def total_processed(self) -> int:
        return self._next_rank

    def remaining(self) -> int:
        return len(self._storage)

    def display_name(self) -> str:
        class_name = type(self).__name__
        chars = [class_name[0]]
        for char in class_name[1:]:
            if char.isupper():
                chars.append(" ")
            chars.append(char)
        return "".join(chars)


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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in "
                    f"stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.display_name()}: total {proc.total_processed()} "
                f"items processed, remaining {proc.remaining()} on "
                "processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)
    data1 = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Talent access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ["hi", "five"]]
    print(f"Send first batch of data on stream: {data1}")
    stream.process_stream(data1)
    stream.print_processors_stats()
    print()
    print("Registering other data processors")
    print("Send the same batch again")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    stream.process_stream(data1)
    stream.print_processors_stats()
    print()
    print("Consume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
