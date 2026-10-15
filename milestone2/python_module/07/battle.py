from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    factory_a: CreatureFactory, factory_b: CreatureFactory
) -> None:
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print("Testing battle")
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print(" fight!")
    print(creature_a.attack())
    print(creature_b.attack())


def main() -> None:
    test_factory(FlameFactory())
    print()
    test_factory(AquaFactory())
    print()
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
