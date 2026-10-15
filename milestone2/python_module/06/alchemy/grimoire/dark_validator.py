from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    words = ingredients.lower().replace(",", " ").split()
    is_valid = False
    for word in words:
        if word in allowed:
            is_valid = True
            break
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
