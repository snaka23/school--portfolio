import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x, y, z':")
        parts = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values = []
        parse_failed = False
        for part in parts:
            cleaned = part.strip()
            try:
                values.append(float(cleaned))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                parse_failed = True
                break
        if parse_failed:
            continue
        x, y, z = values
        return (x, y, z)


def distance(
    point_a: tuple[float, float, float],
    point_b: tuple[float, float, float],
) -> float:
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    dz = point_b[2] - point_a[2]
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y= {pos[1]}, Z={pos[2]}")
    zero_pos = (0.0, 0.0, 0.0)
    first_dis = round(distance(zero_pos, pos), 4)
    print(f"Distance to center: {first_dis}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    second_dis = round(distance(pos, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {second_dis}")
