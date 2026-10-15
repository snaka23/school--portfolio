class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.stats = Plant.Data()

    def show(self) -> None:
        self.stats.add_show()
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def show_stats(self) -> None:
        self.stats.show_statistics()

    class Data:
        def __init__(self):
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0

        def show_statistics(self) -> None:
            print(
                f"Stats: {self.__grow_count} grow, "
                f"{self.__age_count} age, "
                f"{self.__show_count} show"
            )

        def add_grow(self) -> None:
            self.__grow_count += 1

        def add_age(self) -> None:
            self.__age_count += 1

        def add_show(self) -> None:
            self.__show_count += 1

    @staticmethod
    def check_age(how_old: int) -> bool:
        return how_old > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        growth_rate: float
    ):
        super().__init__(name, height, age_days)
        self.color = color
        self.growth_rate = growth_rate
        self.bloomed = False

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)
        self.stats.add_grow()

    def age(self, ages: int) -> None:
        self.age_days += ages
        self.stats.add_age()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.bloomed = True


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        get_seed: int,
        growth_rate: float
    ):
        super().__init__(name, height, age_days, color, growth_rate)
        self.get_seed = get_seed
        self.seed = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed += self.get_seed

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")


class Tree(Plant):
    class Data(Plant.Data):
        def __init__(self):
            super().__init__()
            self.__shade_count = 0

        def add_shade(self) -> None:
            self.__shade_count += 1

        def show_statistics(self) -> None:
            super().show_statistics()
            print(f"{self.__shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        diameter: float
    ):
        super().__init__(name, height, age_days)
        self.stats: Tree.Data = Tree.Data()
        self.diameter = diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        self.stats.add_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and "
            f"{self.diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        season: str,
        growth_rate: float
    ):
        super().__init__(name, height, age_days)
        self.season = season
        self.growth_rate = growth_rate
        self.value = 0

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)
        self.stats.add_grow()

    def age(self) -> None:
        self.age_days = self.age_days + 1
        self.value = self.value + 1
        self.stats.add_age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.value}")


def display_statistics(plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print()
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown Plant]")
    display_statistics(unknown)
