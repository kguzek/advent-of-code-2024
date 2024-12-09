"""Solution for puzzle 6, 2024-12-06"""

from typing import Callable

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 6
# Enables debug output
OPTIMISED_MODE = True

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]


input_start_positions = {}


def debug_print(*args, **kwargs):
    """Prints debug output."""
    if not OPTIMISED_MODE:
        print(*args, **kwargs)


def _find_start_position(input_text: list[str]):
    """Finds the starting position of the guard."""
    for y, line in enumerate(input_text):
        for x, tile in enumerate(line):
            if tile == "^":
                return x, y
    raise RuntimeError("Could not determine the guard start position")


def get_start_position(input_text: list[str]):
    """Finds the starting position of the guard, using memoization."""
    joined = "\n".join(input_text)
    if joined not in input_start_positions:
        input_start_positions[joined] = _find_start_position(input_text)
    return input_start_positions[joined]


def get_obstacle_positions(
    input_text: list[str],
    callback: Callable[[int, int, int], None] = None,
):
    """Yields the positions of the obstacles in the input."""
    direction = 0
    delta_x, delta_y = deltas[direction]
    x, y = get_start_position(input_text)

    def is_in_bounds(x, y):
        """Checks if the given coordinates are within the map area."""
        return 0 <= x < len(input_text[0]) and 0 <= y < len(input_text)

    while is_in_bounds(x, y):
        while True:
            if callback is not None:
                callback(x, y, direction)
            if not is_in_bounds(x + delta_x, y + delta_y):
                # Guard managed to escape the map
                return
            if input_text[y + delta_y][x + delta_x] in ("#", "O"):
                # Change of direction
                yield (x, y, direction)
                direction = (direction + 1) % 4
                delta_x, delta_y = deltas[direction]
            else:
                break
        x += delta_x
        y += delta_y


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 6, part one."""
    positions = set()
    for _ in get_obstacle_positions(input_text, lambda x, y, _: positions.add((x, y))):
        pass
    return positions


def is_infinite_loop(input_text: list[str], obstacle_position: tuple[int, int]):
    """Checks if the input and start coordinates result in a loop."""
    seen_positions = set()
    x, y = obstacle_position
    input_text = (
        input_text[:y]
        + [input_text[y][:x] + "O" + input_text[y][x + 1 :]]
        + input_text[y + 1 :]
    )

    def draw_trail(x, y, direction, force=False):
        if OPTIMISED_MODE:
            return
        tile = input_text[y][x]
        if tile == "^":
            return
        trail = "-" if direction % 2 else "|"
        if tile != "." and (tile != trail or force):
            trail = "+"
        input_text[y] = input_text[y][:x] + trail + input_text[y][x + 1 :]

    for seen_position in get_obstacle_positions(input_text, draw_trail):
        if seen_position in seen_positions:
            debug_print(
                f"Infinite loop detected at {seen_position}:\n{"\n".join(input_text)}\n"
            )
            return True
        seen_positions.add(seen_position)
        draw_trail(*seen_position, True)
    return False


def solve_part_two(input_text: list[str], positions: set[tuple[int, int]]):
    """Calculates the solution for day 6, part two."""
    return sum(
        1
        for position in positions
        if position != get_start_position(input_text)
        and is_infinite_loop(input_text, position)
    )


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(6).splitlines()
    positions = solve_part_one(input_text)
    print("Solution for day 6, part one:", len(positions))
    print("Solution for day 6, part two:", solve_part_two(input_text, positions))


if __name__ == "__main__":
    main()
