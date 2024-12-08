"""Solution for puzzle 4, 2024-12-04"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 4
TEXT_TO_FIND = "XMAS"

# A three character string to search for in an X-shape.
TEXT_TO_FIND_2 = "MAS"


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 4, part one."""
    return sum(
        all(
            0 <= y + xmas_idx * y_direction < len(input_text)
            and 0
            <= x + xmas_idx * x_direction
            < len(input_text[y + xmas_idx * y_direction])
            and input_text[y + xmas_idx * y_direction][x + xmas_idx * x_direction]
            == xmas_char
            for xmas_idx, xmas_char in enumerate(TEXT_TO_FIND)
        )
        for y, line in enumerate(input_text)
        for x, character in enumerate(line)
        if character == TEXT_TO_FIND[0]
        for x_direction in range(-1, 2 if len(line) - x >= len(TEXT_TO_FIND) else 1)
        for y_direction in range(
            -1, 2 if len(input_text) - y >= len(TEXT_TO_FIND) else 1
        )
    )


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 4, part two."""
    return sum(
        1
        for y, line in enumerate(input_text)
        for x, character in enumerate(line)
        if character == TEXT_TO_FIND_2[1]
        and 0 < x < len(line) - 1
        and 0 < y < len(input_text) - 1
        and sum(
            input_text[y + y_direction][x + x_direction] == TEXT_TO_FIND_2[0]
            and input_text[y - y_direction][x - x_direction] == TEXT_TO_FIND_2[2]
            for x_direction in (-1, 1)
            for y_direction in (-1, 1)
        )
        == 2
    )


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(4).splitlines()
    print("Solution for day 4, part one:", solve_part_one(input_text))
    print("Solution for day 4, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
