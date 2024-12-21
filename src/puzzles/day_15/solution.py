"""Solution for puzzle 15, 2024-12-15"""

import os

from math import floor

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 15


def find_robot_position(warehouse: list[list[str]]):
    """Finds the position of the robot in the warehouse."""
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == "@":
                return x, y
    return (-1, -1)


MOVE_MAP = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def solve(warehouse: list[list[str]], moves: str, part_two: bool = False):
    """Calculates the solution for day 15, part one."""
    os.system("clear")
    x, y = find_robot_position(warehouse)
    for move_number, move in enumerate(moves):
        print(f"Move {move_number + 1}: {move} | {x = }, {y = }")
        print("\n".join("".join(row) for row in warehouse))
        input()
        os.system("clear")
        dx, dy = MOVE_MAP[move]
        next_x, next_y = x, y
        if part_two:
            dx = dx / 2
        pushing = True
        while pushing:
            next_x += dx
            next_y += dy
            next_tile = warehouse[next_y][floor(next_x)]
            match next_tile:
                case ".":
                    warehouse[y][floor(x)] = "."
                    warehouse[y + dy][floor(x + dx)] = "@"
                    if next_y != y + dy or (
                        next_x != x + dx and floor(x) != floor(x + dx)
                    ):
                        warehouse[next_y][floor(next_x)] = "O"
                    pushing = False
                    x += dx
                    y += dy
                    break
                case "O":
                    continue
                case "#":
                    pushing = False
                    break
    return sum(
        sum(100 * y + x for x, tile in enumerate(row) if tile == "O")
        for y, row in enumerate(warehouse)
    )


def main():
    """Entry point for the solution."""
    warehouse, moves = [
        part.splitlines() for part in get_puzzle_input(15).split("\n\n")
    ]
    warehouse = [list(row) for row in warehouse]
    moves = "".join(moves)
    print("Solution for day 15, part one:", solve(warehouse.copy(), moves))
    print("Solution for day 15, part two:", solve(warehouse.copy(), moves, True))


if __name__ == "__main__":
    main()
