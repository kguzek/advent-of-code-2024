"""Solution for puzzle 6, 2024-12-06"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 6

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 6, part one."""
    positions = set()
    for y, row in enumerate(input_text):
        if "^" in row:
            x = row.index("^")
            break
    else:
        raise RuntimeError("Could not find the start position")
    direction = 0
    delta_x, delta_y = deltas[direction]
    while 0 <= x < len(input_text[0]) and 0 <= y < len(input_text):
        positions.add((x, y))
        try:
            if input_text[y + delta_y][x + delta_x] == "#":
                # Change of direction
                direction = (direction + 1) % 4
                delta_x, delta_y = deltas[direction]
        except IndexError:
            break
        x += delta_x
        y += delta_y
    return len(positions)


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 6, part two."""


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(6).splitlines()
    print("Solution for day 6, part one:", solve_part_one(input_text))
    print("Solution for day 6, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
