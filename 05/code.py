from dataclasses import dataclass
from typing import List, Optional
import re


@dataclass
class BoardingPass:
    row: int
    col: int

    @classmethod
    def parse(cls, raw_input: str):
        row, col = raw_input[:7], raw_input[7:]
        return cls(
            row=int(row.replace("F", "0").replace("B", "1"), 2),
            col=int(col.replace("L", "0").replace("R", "1"), 2),
        )


def part_1(boarding_passes: List[BoardingPass]):
    """
    Expected answer: 938.
    """
    return max(map(lambda bd: bd.row * 8 + bd.col, boarding_passes))


def part_2(boarding_passes: List[BoardingPass]):
    """
    Expected answer: xxx.
    """
    # Maybe need to remove all seats from first and last rows

    seat_ids = set(map(lambda bd: bd.row * 8 + bd.col, boarding_passes))

    min_id = min(seat_ids)
    max_id = max(seat_ids)

    res = next(iter(set(seat_ids) ^ set(range(min_id, max_id + 1))))
    return res


if __name__ == "__main__":
    with open("boarding_passes.txt") as f:
        passes = [BoardingPass.parse(line) for line in f]

    res_1 = part_1(passes)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(passes)
    print("The answer for part 2 is:", res_2)
