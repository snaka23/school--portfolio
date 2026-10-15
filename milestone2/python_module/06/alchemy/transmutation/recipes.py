from .. import elements, potions
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{elements.create_air()}' and '{potions.strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
