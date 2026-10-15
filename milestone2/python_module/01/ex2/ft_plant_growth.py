#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    flower = Plant("Rose", 25.0, 30, 0.8)
    start_height = flower.height
    print("=== Garden Plant Growth ===")
    flower.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        flower.grow()
        flower.age()
        flower.show()
    growth_height = round(flower.height - start_height, 1)
    print(f"Growth this week: {growth_height}cm")
