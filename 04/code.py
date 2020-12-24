from dataclasses import dataclass
from typing import List, Optional
import re


@dataclass
class IDCard:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None

    def is_valid(self) -> bool:
        return bool(
            self.byr
            and self.iyr
            and self.eyr
            and self.hgt
            and self.hcl
            and self.ecl
            and self.pid
        )

    def enforced_validation(self) -> bool:
        if not self.is_valid():
            return False

        if len(self.byr) != 4 or "1920" > self.byr or self.byr > "2002":
            return False
        if len(self.iyr) != 4 or "2010" > self.iyr or self.iyr > "2020":
            return False
        if len(self.eyr) != 4 or "2020" > self.eyr or self.eyr > "2030":
            return False
        if not re.match(r"\d?\d\d(cm|in)", self.hgt):
            return False
        if "cm" in self.hgt and ("150" > self.hgt[:-2] or self.hgt[:-2] > "193"):
            return False
        if "in" in self.hgt and ("59" > self.hgt[:-2] or self.hgt[:-2] > "76"):
            return False
        if not re.fullmatch(r"#[0-9a-f]{6}", self.hcl):
            return False
        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if len(self.pid) != 9:
            return False

        try:
            int(self.pid)
        except ValueError:
            return False

        return True

    @classmethod
    def build(cls, raw_input):
        items = {
            key: value
            for key, value in map(lambda item: item.split(":"), raw_input.split(" "))
        }

        return IDCard(**items)


def parse_input(file_name: str):
    raw_ids = list()

    with open(file_name) as f:
        current_line = []

        for line in map(lambda line: line.strip(), f):
            if line:
                current_line.append(line)
                continue

            raw_ids.append(" ".join(current_line))
            current_line = []

    return [IDCard.build(raw_id) for raw_id in raw_ids]


def part_1(id_cards: List[IDCard]):
    """
    Expected answer: 208.
    """
    return len(list(filter(lambda id_card: id_card.is_valid(), id_cards)))


def part_2(id_cards: List[IDCard]):
    """
    Expected answer: 167.
    """
    return len(list(filter(lambda id_card: id_card.enforced_validation(), id_cards)))

    return None


if __name__ == "__main__":
    id_cards = parse_input("passports.txt")

    res_1 = part_1(id_cards)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(id_cards)
    print("The answer for part 2 is:", res_2)
