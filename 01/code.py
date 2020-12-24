from itertools import tee
from typing import List, Tuple


def find_two_sum(lst: List[int], target: int) -> Tuple[int, int]:
    ptr_begin, ptr_end = 0, len(lst) - 1

    # TODO find better way to iter around `expense_report` without using indexes
    while True:
        curr_sum = lst[ptr_begin] + lst[ptr_end]
        if ptr_begin >= ptr_end:
            raise ValueError

        if curr_sum == target:
            break
        elif curr_sum > target:
            ptr_end -= 1
        else:
            ptr_begin += 1

    return lst[ptr_begin], lst[ptr_end]


def part_1(expense_report, expected):
    """
    Find two numbers in expense_report that equals to expected, and multiply them.

    Should return 969024
    """

    a, b = find_two_sum(expense_report, expected)
    return a * b


def part_2(expense_report, expected):
    """
    Find three numbers in expense_report that equals to expected, and multiply them.

    Should return 230057040
    """

    for value in expense_report:
        try:
            a, b = find_two_sum(expense_report, expected - value)
            return a * b * value

        except ValueError:
            continue

    return None


if __name__ == "__main__":
    with open("expense_report.txt") as f:
        expense_report = sorted(int(line.strip()) for line in f if line.strip())

    expense_report, expense_report_dup = tee(expense_report)
    expected = 2020

    res_1 = part_1(list(expense_report), expected)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(list(expense_report_dup), expected)
    print("The answer for part 2 is:", res_2)
