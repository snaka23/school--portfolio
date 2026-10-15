from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        spend = end - start
        print(f"Spell completed in {spend:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[-1] < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i + 1 != max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {i + 1}/{max_attempts})"
                        )
                    continue
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) > 2:
            return False
        for a in name:
            if not (a.isalpha() or a.isspace()):
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def heal(power: int) -> str:
    raise ValueError("The spell is cursed!")


@retry_spell(max_attempts=3)
def waterball() -> str:
    return "Waaaaaaaagh spelled!"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())
    print("\nTesting retrying...")
    print(heal(42))
    print(waterball())
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Orge"))
    print(guild.validate_mage_name("Orge2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 8))
