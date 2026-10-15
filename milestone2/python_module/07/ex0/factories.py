import abc
from ex0 import creatures


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> creatures.Creature:
        ...

    @abc.abstractmethod
    def create_evolved(self) -> creatures.Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Flameling()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Aquabub()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Torragon()
