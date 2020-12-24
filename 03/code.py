from typing import List


def compute_tree_for_slope(
    terrain: List[List[str]], right_step: int, down_step: int
) -> int:
    """
    Get the number of tree hit by traversing the terrain with the given slope.
    """

    tree_count = 0
    pos_x, pos_y = 0, 0

    while pos_x < len(terrain):
        try:
            if terrain[pos_x][pos_y] == "#":
                tree_count += 1
            pos_y += right_step
            pos_x += down_step

        except IndexError as e:
            pos_y = pos_y % len(terrain[pos_x])

    return tree_count


def part_1(terrain: List[List[str]]) -> int:
    """
    Get the numer of trees encountered on terrain with a slope of 3 right and 1 down.

    Expected answer: 162.
    """

    return compute_tree_for_slope(terrain, 3, 1)


def part_2(terrain: List[List[str]]):
    """
    Get the numer of trees encountered for each slope on the terrain and multiply them
    together.

    Expected answer: 3064612320.
    """
    res = 1

    for right_slope, down_slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= compute_tree_for_slope(terrain, right_slope, down_slope)

    return res


if __name__ == "__main__":
    terrain = []
    with (open("map.txt")) as f:
        for line in f:
            terrain.append(line.strip())

    assert len(terrain) == 323

    res_1 = part_1(terrain)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(terrain)
    print("The answer for part 2 is:", res_2)
