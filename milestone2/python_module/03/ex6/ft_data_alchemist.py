import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    player_names = ["Alice", "bob", "Charlie",
                    "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {player_names}")
    capitalized_names = [name.capitalize() for name in player_names]
    print(f"New list with all names capitalized: {capitalized_names}")
    already_capitalized = [name for name in player_names if name[0].isupper()]
    print(f"New list of capitalized names only: {already_capitalized}")
    print()
    scores = {name: random.randint(1, 999) for name in capitalized_names}
    print(f"Score dict: {scores}")
    average = round(sum(scores[name] for name in scores) / len(scores), 2)
    print(f"Score average is {average}")
    high_scores = {name: scores[name] for name in scores
                   if scores[name] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
