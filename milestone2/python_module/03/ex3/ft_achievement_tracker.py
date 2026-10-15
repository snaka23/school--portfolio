import random


def gen_player_archievements(achievement_list: list[str]) -> set[str]:
    num = random.randint(1, 9)
    picked = random.sample(achievement_list, num)
    return set(picked)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    archievement_master = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
    ]
    alice = gen_player_archievements(archievement_master)
    print(f"Player Alice: {alice}")
    bob = gen_player_archievements(archievement_master)
    print(f"Player Bob: {bob}")
    charlie = gen_player_archievements(archievement_master)
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_archievements(archievement_master)
    print(f"Player Dylan: {dylan}")
    print()
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print()
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print()
    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    master_set = set(archievement_master)
    miss_alice = master_set.difference(alice)
    miss_bob = master_set.difference(bob)
    miss_charlie = master_set.difference(charlie)
    miss_dylan = master_set.difference(dylan)
    print(f"Alice is missing: {miss_alice}")
    print(f"Bob is missing: {miss_bob}")
    print(f"Charlie is missing: {miss_charlie}")
    print(f"Dylan is missing: {miss_dylan}")
