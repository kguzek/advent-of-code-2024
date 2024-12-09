"""Solution for puzzle 8, 2024-12-08"""

from itertools import product

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 8


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 8, part one."""
    height = len(input_text)
    width = len(input_text[0])
    result = 0
    for y, line in enumerate(input_text):
        for x, char in enumerate(line):
            try:
                for delta_x, delta_y in product(
                    range(-width, width), range(-height, height)
                ):
                    if 0 in (delta_x, delta_y):
                        continue
                    far_x = x + 2 * delta_x
                    far_y = y + 2 * delta_y
                    if not (0 <= far_x < width and 0 <= far_y < height):
                        continue
                    close_antenna = input_text[y + delta_y][x + delta_x]
                    far_antenna = input_text[far_y][far_x]
                    if close_antenna != far_antenna or far_antenna in (
                        ".",
                        "#",
                    ):
                        continue
                    result += 1
                    if char == ".":
                        input_text[y] = input_text[y][:x] + "#" + input_text[y][x + 1 :]
                    raise RuntimeError("Found antinode")
            except RuntimeError as exc:
                if exc.args[0] != "Found antinode":
                    raise
                continue
    print("\n".join(input_text))
    return result


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 8, part two."""
    height = len(input_text)
    width = len(input_text[0])
    result = 0
    for y, line in enumerate(input_text):
        for x, char in enumerate(line):
            if char != ".":
                result += 1
                continue
            try:
                for delta_x, delta_y in product(
                    range(-width, width), range(-height, height)
                ):
                    if 0 in (delta_x, delta_y):
                        continue
                    search_x = x + delta_x
                    search_y = y + delta_y
                    found_antennae = set()
                    while 0 <= search_x < width and 0 <= search_y < height:
                        found_antenna = input_text[search_y][search_x]
                        if found_antenna not in (".", "#"):
                            if found_antenna in found_antennae:
                                break
                            found_antennae.add(found_antenna)
                        search_x += delta_x
                        search_y += delta_y
                    else:
                        continue
                    result += 1
                    input_text[y] = input_text[y][:x] + "#" + input_text[y][x + 1 :]
                    raise RuntimeError("Found antinode")
            except RuntimeError as exc:
                if exc.args[0] != "Found antinode":
                    raise
                continue
    print("\n".join(input_text))
    return result


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(8).splitlines()
    print("Solution for day 8, part one:", solve_part_one(input_text[:]))
    print("Solution for day 8, part two:", solve_part_two(input_text[:]))


if __name__ == "__main__":
    main()
