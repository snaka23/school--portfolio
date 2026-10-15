from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def count_plus() -> int:
        nonlocal count
        count += 1
        return count
    return count_plus


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def plus_power(bulk: int) -> int:
        nonlocal total
        total += bulk
        return total
    return plus_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(name: str) -> str:
        return enchantment_type + ' ' + name
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        if key in storage:
            return storage[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    c1 = mage_counter()
    print(f"counter_a call 1: {c1()}")
    print(f"counter_a call 2: {c1()}")
    c2 = mage_counter()
    print(f"counter_b call 1: {c2()}")
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print("\nTesting enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    enchantment2 = enchantment_factory("Frozen")
    print(f"{enchantment('Sword')}")
    print(f"{enchantment2('Shield')}")
    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]
    store("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")
