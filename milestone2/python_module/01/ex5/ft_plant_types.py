#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int, color: str):
        super().__init__(name, height, age_days)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        diameter: float
    ):
        super().__init__(name, height, age_days)
        self.diameter = diameter
        self.shade = False

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
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

    def age(self) -> None:
        self.age_days = self.age_days + 1
        self.value = self.value + 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
