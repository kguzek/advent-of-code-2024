"""Solution for puzzle 11, 2024-12-11"""

from collections import Counter
from functools import cache

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 11


@cache
def change_stone(stone: int) -> tuple[int, int | None]:
    """Returns the stone after one blink."""
    if stone == 0:
        return 1, None
    stone_str = str(stone)
    stone_str_len = len(stone_str)
    if stone_str_len % 2 != 0:
        return stone * 2024, None
    midpoint_idx = stone_str_len // 2
    return int(stone_str[:midpoint_idx]), int(stone_str[midpoint_idx:])


def get_stones_count(stones: Counter[int], times_blinked: int):
    """Calculates the solution for day 11, part one."""
    for _ in range(times_blinked):
        for stone, count in list(stones.items()):
            stones[stone] -= count
            new_stone, extra_stone = change_stone(stone)
            stones[new_stone] += count
            if extra_stone is None:
                continue
            stones[extra_stone] += count

    return stones.total()


def main():
    """Entry point for the solution."""
    stones = Counter(int(stone) for stone in get_puzzle_input(11).split())
    print("Solution for day 11, part one:", get_stones_count(stones, 25))
    print("Solution for day 11, part two:", get_stones_count(stones, 50))


if __name__ == "__main__":
    main()
