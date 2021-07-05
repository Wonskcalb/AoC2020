from collections import Counter
from dataclasses import dataclass, field
from typing import List, Optional, Set, Tuple


def parse_input(file_name: str):

    with open(file_name) as f:
        return [line.strip().split(' ') for line in f]


def run_code(code: List) -> Tuple[int, int]:
    """
    Return the accumulator, a pointer to the last instruction and current instruction.
    If a loop exists, stops a the beginning of the loop.
    """
    executed_lines = set()

    prv_ptr, ins_ptr, acc = -1, 0, 0

    while True:
        if ins_ptr in executed_lines:
            break

        executed_lines.add(ins_ptr)

        cmd, args = code[ins_ptr]

        if cmd == "acc":
            acc += int(args)

        elif cmd == "nop":
            pass

        elif cmd == "jmp":
            prv_ptr = ins_ptr
            ins_ptr += int(args)
            continue

        prv_ptr = ins_ptr
        ins_ptr += 1

    else:
        # No loop detected
        return acc, -1

    return acc, ins_ptr


def part_1(code: List):
    """
    There is a loop in the code. Find the value of the accumulator before an
    instruction is executed twice.

    Expected answer: 1814.
    """
    acc, _ = run_code(code)

    return acc


def part_2(code: List):
    """
    Find the instruction that created the loop, switch it: nop -> jmp or jmp -> nop
    and return the value of the accumulator.

    Expected answer: xxxx
    """

    original_ins = None

    for idx, ins in enumerate(code):
        original_ins = ins[0]

        if ins[0] == "jmp":
            ins[0] = "nop"

        elif ins[0] == "nop":
            ins[0] = "jmp"

        acc, ins_ptr = run_code(code)

        if ins_ptr == -1:
            print("yey")
            break

        ins = original_ins
    else:
        return None

    return acc


if __name__ == "__main__":
    code = parse_input("bootcode.txt")

    res_1 = part_1(code)
    print("The answer for part 1 is:", res_1)

    res_2 = part_2(code)
    print("The answer for part 2 is:", res_2)
