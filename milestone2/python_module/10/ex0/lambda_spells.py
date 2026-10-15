def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda a: f"* {a} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda a: a["power"], mages))
    return {
        "max_power": max(mages, key=lambda a: a["power"])["power"],
        "min_power": min(mages, key=lambda a: a["power"])["power"],
        "avg_power": round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Cloak", "power": 78, "type": "armor"},
        {"name": "Thunder Ring", "power": 63, "type": "accessory"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    for_display = " ".join(transformed)
    print(for_display)
    mages = [
        {"name": "Alex", "power": 45, "element": "fire"},
        {"name": "Jordan", "power": 72, "element": "shadow"},
        {"name": "Riley", "power": 30, "element": "ice"},
        {"name": "Sage", "power": 88, "element": "light"}
    ]
    print("\nTesting power filter")
    filter_mages = power_filter(mages, 50)
    print(f"They have power more than 50 {filter_mages}")
    print("\nTesting mage stats")
    stats_mages = mage_stats(mages)
    print(stats_mages)
