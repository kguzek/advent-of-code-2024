"""Solution for puzzle 3, 2024-12-03"""

import re

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 3

MULTIPLICATION_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")


def solve_part_one(input_text: str):
    """Calculates the solution for day 3, part one."""
    matches = MULTIPLICATION_PATTERN.finditer(input_text)
    return sum(int(match.group(1)) * int(match.group(2)) for match in matches)


def solve_part_two(input_text: str):
    """Calculates the solution for day 3, part two."""
    start_idx = None
    enabled = True
    result = 0
    for i, c in enumerate(input_text):
        if c == "d" or c == "m":
            start_idx = i
            continue
        if start_idx is None or i - start_idx < 3:
            continue
        substring = input_text[start_idx : i + 1]
        match substring:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled and (
                match := MULTIPLICATION_PATTERN.fullmatch(substring)
            ):
                result += int(match.group(1)) * int(match.group(2))
    return result


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(3)
    print("Solution for day 3, part one:", solve_part_one(input_text))
    print("Solution for day 3, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
