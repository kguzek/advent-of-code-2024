"""Solution for puzzle 14, 2024-12-14"""

import re
from functools import reduce
from operator import mul

from collections import Counter

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 14

ROBOT_PATTERN = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"


class Robot:
    """Robot class for day 14."""

    def __init__(self, line: str):
        match = re.match(ROBOT_PATTERN, line)
        x = int(match.group(1))
        y = int(match.group(2))
        self.pos = (x, y)
        self.vel = (int(match.group(3)), int(match.group(4)))

    def __repr__(self):
        return f"Robot(pos={self.pos}, vel={self.vel})"


def solve(
    robots: list[Robot], time: int, room_width: int, room_height: int, part_two=False
):
    """Get the positions of the robots at a given time."""
    quadrants = [0, 0, 0, 0]
    coords = Counter()
    breakpoint_x = room_width // 2
    breakpoint_y = room_height // 2
    for robot in robots:
        x = (robot.pos[0] + robot.vel[0] * time) % room_width
        y = (robot.pos[1] + robot.vel[1] * time) % room_height
        coords[(x, y)] += 1
        if x == breakpoint_x or y == breakpoint_y:
            continue
        quadrants[int(x > breakpoint_x) + 2 * int(y > breakpoint_y)] += 1

    def print_map():
        for y in range(room_height):
            for x in range(room_width):
                print(coords[(x, y)] or ".", end="")
            print(flush=True)

    consecutive_x = 0
    for y in range(room_height):
        for x in range(room_width):
            num = coords[(x, y)]
            if not part_two:
                continue
            if num > 0:
                consecutive_x += 1
            else:
                consecutive_x = 0
            if consecutive_x > 7:
                print_map()
                return True
    return False if part_two else reduce(mul, quadrants, 1)


def solve_part_two(robots: list[Robot], room_width: int, room_height: int):
    """Solve part two of the puzzle."""
    i = 0
    while True:
        i += 1
        # print("Time:", i)
        if solve(robots, i, room_width, room_height, True):
            return i


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(14).splitlines()
    room_width, room_height = (11, 7) if len(input_text) == 12 else (101, 103)
    robots = [Robot(line) for line in input_text]
    print(
        "Solution for day 14, part one:",
        solve(robots, 100, room_width, room_height),
    )
    print(
        "Solution for day 14, part two:",
        solve_part_two(robots, room_width, room_height),
    )


if __name__ == "__main__":
    main()
