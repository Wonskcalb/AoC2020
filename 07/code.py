from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, Optional, Set
import re


@dataclass
class Node:
    value: str
    children: Dict[str, int] = field(default_factory=dict)


def parse_input(file_name: str):
    graph = dict()

    def parse_children(sub_bag_definition: str) -> Dict[str, int]:
        if sub_bag_definition == "no other bags.":
            return {}

        return {
            sub_bag.rsplit(" ", 1)[0]: int(count)
            for count, sub_bag in map(
                lambda bag: bag.split(" ", 1), map(str.strip, bag_content.split(","))
            )
        }

    with open(file_name) as f:
        for line in f:
            bag_id, bag_content = map(str.strip, line.split("contain"))

            graph[bag_id.rsplit(" ", 1)[0]] = Node(
                value=bag_id, children=parse_children(bag_content)
            )

    assert len(graph) == 594

    return graph


def part_1(rules: Dict):
    """
    Expected answer: 302.
    """

    def bag_containing_color(color: str) -> Set[str]:
        return set(k for k, v in rules.items() if color in v.children.keys())

    to_process = bag_containing_color("shiny gold")

    answer = set()

    while color := to_process.pop() if to_process else None:
        if color in answer:
            continue

        answer.add(color)
        to_process |= bag_containing_color(color)

    return len(answer)


def part_2(rules: Dict):
    """
    From a single shiny gold bag, count all the bags required, recursively.
    Expected answer: 4165
    """
    bag_quantity = Counter()

    to_process = Counter(
        {bag: quantity for bag, quantity in rules["shiny gold"].children.items()}
    )

    while item := to_process.popitem() if to_process else None:
        bag, quantity = item
        bag_quantity.update({bag: quantity})

        bags_to_add = {k: v * quantity for k, v in rules[bag].children.items()}
        to_process.update(bags_to_add)

    return sum(bag_quantity.values())


if __name__ == "__main__":
    rules = parse_input("rules.txt")

    res_1 = part_1(rules)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(rules)
    print("The answer for part 2 is:", res_2)
