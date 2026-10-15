from functools import reduce, lru_cache, partial, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not len(spells):
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    try:
        result = reduce(operations[operation], spells)
    except KeyError:
        raise ValueError("operation is unknown")
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="Fire")
    ice = partial(base_enchantment, power=50, element="Ice")
    lightning = partial(base_enchantment, power=50, element="Lightning")
    return {
        "fire": fire,
        "ice": ice,
        "lightning": lightning
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base(anything: Any) -> str:
        return "Unknown spell type"

    @base.register
    def _(anything: int) -> str:
        return f"Damage spell: {anything} damage"

    @base.register
    def _(anything: str) -> str:
        return f"Enchantment: {anything}"

    @base.register
    def _(anything: list) -> str:
        return f"Multi-cast: {len(anything)} spells"
    return base


def test(power: int, element: str, target: str) -> str:
    return f"power: {power}, element: {element}, target: {target}"


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(test)
    print(enchanter["fire"](target="Dragon"))
    print(enchanter["ice"](target="Goblin"))
    print(enchanter["lightning"](target="Ogre"))
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([2, 3, 4]))
    print(dispatcher({"name": "Dragon"}))
