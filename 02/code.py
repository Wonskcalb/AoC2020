from collections import Counter
from dataclasses import dataclass
from operator import xor
from typing import Callable


@dataclass
class Holder:
    min_occurence: int
    max_occurence: int
    letter: str

    @staticmethod
    def parse_from_string(raw_policy: str):
        limits, letter = raw_policy.split(" ")

        min_occurence, max_occurence = map(int, limits.split("-"))

        return Holder(
            min_occurence=min_occurence, max_occurence=max_occurence, letter=letter
        )


def old_policy(holder: Holder, password: str) -> bool:
    if holder.letter not in password:
        return False

    count = password.count(holder.letter)

    return holder.min_occurence <= count <= holder.max_occurence


def octas_policy(holder: Holder, password: str) -> bool:
    pos_1 = password[holder.min_occurence - 1]
    pos_2 = password[holder.max_occurence - 1]

    return xor(pos_1 == holder.letter, pos_2 == holder.letter)


def part_1():
    """
    The goal here is to return the number of passwords where the letter is present
    between min_occurence and max_occurence times.

    Answer should be 528.
    """
    counter = 0

    with open("passwords.txt", "r") as f:
        for raw_policy, password in map(lambda line: line.strip().split(": "), f):
            if old_policy(Holder.parse_from_string(raw_policy), password):
                counter += 1

    return counter


def part_2():
    """
    The goal here is to return the number of passwords where one of the two letters at
    position min_occurence and max_occurence are defined letter. It's invalid if
    both are the same (xor). Positions start at 1 not 0

    Answer should be 497
    """

    counter = 0

    with open("passwords.txt", "r") as f:
        for raw_policy, password in map(lambda line: line.strip().split(": "), f):
            if octas_policy(Holder.parse_from_string(raw_policy), password):
                counter += 1

    return counter


if __name__ == "__main__":
    res_1 = part_1()
    print("The answer for part 1 is:", res_1)

    res_2 = part_2()
    print("The answer for part 2 is:", res_2)
