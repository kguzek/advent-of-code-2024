"""Solution for puzzle 3, 2024-12-03"""

import re

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 3

MULTIPLICATION_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
MULTIPLICATION_PATTERN_2 = re.compile(r"(?<=do\(\)).+?mul\((\d+),(\d+)\)")


def solve_part_one(input_text: str):
    """Calculates the solution for day 3, part one."""
    matches = MULTIPLICATION_PATTERN.finditer(input_text)
    return sum(int(match.group(1)) * int(match.group(2)) for match in matches)


def solve_part_two(input_text: str):
    """Calculates the solution for day 3, part two."""
    # start_idx = 0
    # # for i, c in enumerate(input_text):
    # #     if  == "don't()"[start_idx]:


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(3)
    print("Solution for day 3, part one:", solve_part_one(input_text))
    print("Solution for day 3, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
