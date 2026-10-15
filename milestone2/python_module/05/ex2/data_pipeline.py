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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def _escape(self, value: str) -> str:
        needs_quoting = False
        for char in (",", '"', "\n"):
            if char in value:
                needs_quoting = True
                break
        if needs_quoting:
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        escaped_values = []
        for rank, value in data:
            escaped_value = self._escape(value)
            escaped_values.append(escaped_value)
        line = ",".join(escaped_values)
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    def _escape(self, value: str) -> str:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return escaped.replace("\n", "\\n").replace("\t", "\\t")

    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields = []
        for rank, value in data:
            fields.append(f'"item_{rank}": "{self._escape(value)}"')
        print("JSON Output:")
        print("{" + ",".join(fields) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                batch.append(proc.output())
            if batch:
                plugin.process_output(batch)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    data = DataStream()
    data.print_processors_stats()
    print()
    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data.register_processor(numeric)
    data.register_processor(text)
    data.register_processor(log)
    batch1 = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch1}")
    data.process_stream(batch1)
    print()
    data.print_processors_stats()
    print()
    print("Send 3 processor data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data.output_pipeline(3, csv_plugin)
    print()
    data.print_processors_stats()
    print()
    batch2 = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {batch2}")
    print()
    data.process_stream(batch2)
    data.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data.output_pipeline(5, json_plugin)
    print()
    data.print_processors_stats()


if __name__ == "__main__":
    main()
