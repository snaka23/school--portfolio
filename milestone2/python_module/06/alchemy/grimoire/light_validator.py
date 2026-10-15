def validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire.light_spellbook import (
        light_spell_allowed_ingredients,
    )
    allowed = light_spell_allowed_ingredients()
    words = ingredients.lower().replace(",", " ").split()
    is_valid = False
    for word in words:
        if word in allowed:
            is_valid = True
            break
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
