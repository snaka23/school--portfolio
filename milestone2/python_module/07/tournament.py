from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
    InvalidStrategyError)
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    count = len(opponents)
    print(f"{count} opponents involved")
    creatures = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        creatures.append((creature, strategy))
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature_a, strategy_a = creatures[i]
            creature_b, strategy_b = creatures[j]
            print()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(opponents)
    print()
    opponents2 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(opponents2)
    print()
    opponents3 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())]
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(opponents3)


if __name__ == "__main__":
    main()
