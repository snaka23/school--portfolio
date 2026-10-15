from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fire ball attacked {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def has_enough_power(target: str, power: int) -> bool:
    return power >= 50


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return (
        lambda target, power:
        base_spell(target, power * multiplier)
    )


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (
        lambda target, power:
        spell(target, power)
        if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: list(
        map(lambda spell: spell(target, power), spells)
    )


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combiner = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combiner('Dragon', 50)}")
    print("\nTesting power amplifier...")
    amplifier = power_amplifier(fireball, 3)
    print(
        f"Original: {fireball('Dragon', 50)}, "
        f"Amplified: {amplifier('Dragon', 50)}"
    )
    print("\nTesting spell conditional caster...")
    caster = conditional_caster(has_enough_power, fireball)
    print(f"is verified spell: {caster('Dragon', 60)}")
    print(f"is verified spell: {caster('Dragon', 30)}")
    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence('Dragon', 80))
