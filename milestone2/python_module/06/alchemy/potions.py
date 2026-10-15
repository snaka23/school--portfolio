import elements
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{elements.create_fire()}' and "
        f"'{elements.create_water()}'"
    )
