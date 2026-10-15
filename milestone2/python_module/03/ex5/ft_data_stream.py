import typing
import random


def gen_event(
    PLAYERS: list[str],
    ACTIONS: list[str]
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events[index]
        del events[index]
        yield event


def main() -> None:
    PLAYERS = ["alice", "bob", "charlie", "dylan"]
    ACTIONS = ["run", "walk", "jump", "swim", "climb", "eat", "sleep", "move",
               "grab", "release", "use"]
    print("=== Game Data Stream Processor ===")
    gen = gen_event(PLAYERS, ACTIONS)
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    events: list[tuple[str, str]] = []
    for _ in range(10):
        events = events + [(next(gen))]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
