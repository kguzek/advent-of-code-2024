"""Solution for puzzle 1, 2024-12-01"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 1


def solve():
    """Calculates the solution for day 1."""
    input_text = get_puzzle_input(SOLUTION_DAY)
    lines = input_text.split("\n")
    result = 0
    for line in lines:
        a, b = line.split()
        result += int(a) - int(b)
    return result


if __name__ == "__main__":
    print("Solution for day 1:", solve())
