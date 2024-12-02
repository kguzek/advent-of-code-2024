"""Solution for puzzle 2, 2024-12-02"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 2


def get_list(line: str):
    """Converts line to int list."""
    return list(map(int, line.split()))


def is_safe(levels: list[int]) -> bool:
    """Determines whether or not the line of levels is safe."""
    previous_level = None
    for a, b in zip(levels[:-1], levels[1:]):
        level = b - a
        # Ensure each difference is between 1 and 3
        # and that the sequence is either ascending or descending
        if (not 1 <= abs(level) <= 3) or (
            previous_level is not None and ((level > 0) != (previous_level > 0))
        ):
            return False
        previous_level = level
    return True


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 2, part one."""
    return sum(1 for line in input_text if is_safe(get_list(line)))


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 2, part two."""

    def are_any_safe(levels: list[int]) -> bool:
        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                return True
        return is_safe(levels)

    return sum(1 for line in input_text if are_any_safe(get_list(line)))


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(2).splitlines()
    print("Solution for day 2, part one:", solve_part_one(input_text))
    print("Solution for day 2, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
