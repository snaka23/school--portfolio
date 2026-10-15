import sys


def get_valid_scores() -> list[int]:
    score_list: list[int] = []
    i = 1
    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            score_list = score_list + [score]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i = i + 1
    return score_list


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score = get_valid_scores()
    if len(score) < 1:
        string = "No scores provided. Usage:"
        print(f"{string} python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score) / len(score)}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
