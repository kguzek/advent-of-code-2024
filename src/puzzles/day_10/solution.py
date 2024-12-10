"""Solution for puzzle 10, 2024-12-10"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 10


def get_destinations(
    input_text: list[list[int]], x: int, y: int, height: int = 0
) -> set[tuple[int, int]]:
    """Gets the coordinates of all 9s reachable from here."""
    return (
        set()
        # Out of bounds
        if not (0 <= x < len(input_text[0]) and 0 <= y < len(input_text))
        # Not increasing gradually
        or input_text[y][x] != height
        else (
            # Coordinates of the trail endpoint
            {(x, y)}
            if height == 9
            # Check surrounding tiles
            else set().union(
                *[
                    get_destinations(input_text, x + delta_x, y + delta_y, height + 1)
                    for delta_y, delta_x in ((-1, 0), (0, 1), (1, 0), (0, -1))
                ]
            )
        )
    )


def get_num_trails(input_text: list[list[int]], x: int, y: int, height: int = 0) -> int:
    """Gets the number of trails reachable from here."""
    return (
        0
        # Out of bounds
        if not (0 <= x < len(input_text[0]) and 0 <= y < len(input_text))
        # Not increasing gradually
        or input_text[y][x] != height
        else (
            # End of trail
            1
            if height == 9
            # Check surrounding tiles
            else sum(
                get_num_trails(input_text, x + delta_x, y + delta_y, height + 1)
                for delta_y, delta_x in ((-1, 0), (0, 1), (1, 0), (0, -1))
            )
        )
    )


def solve_part_one(input_text: list[list[int]]):
    """Calculates the solution for day 10, part one."""
    return sum(
        len(get_destinations(input_text, x, y))
        for y, row in enumerate(input_text)
        for x, position in enumerate(row)
        if position == 0
    )


def solve_part_two(input_text: list[list[int]]):
    """Calculates the solution for day 10, part two."""
    return sum(
        get_num_trails(input_text, x, y)
        for y, row in enumerate(input_text)
        for x, position in enumerate(row)
        if position == 0
    )


def main():
    """Entry point for the solution."""
    input_text = [
        [int(position) for position in list(row)]
        for row in get_puzzle_input(10).splitlines()
    ]
    print("Solution for day 10, part one:", solve_part_one(input_text))
    print("Solution for day 10, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
