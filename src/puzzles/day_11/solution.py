"""Solution for puzzle 11, 2024-12-11"""

from functools import cache

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 11


@cache
def change_stone(stone: int) -> tuple[int, int | None]:
    """Determines the next values of a stone after a blink."""
    if stone == 0:
        return 1, None
    stone_str = str(stone)
    num_digits = len(stone_str)
    if num_digits % 2 == 0:
        halfway_idx = num_digits // 2
        return int(stone_str[:halfway_idx]), int(stone_str[halfway_idx:])
    return stone * 2024, None


def get_stones_after_blinks(
    stones: list[int], times_blinked: int, blink_offset: int = 0
):
    """Computes the list of stones after the given number of blinks."""
    for blink in range(times_blinked):
        print(
            f"Blink {blink + blink_offset + 1:>2}, number of stones: ",
            end="",
            flush=True,
        )
        to_append = []
        for i, stone in enumerate(stones):
            stone, extra_stone = change_stone(stone)
            stones[i] = stone
            if extra_stone is not None:
                to_append.append(extra_stone)
        stones += to_append
        print(len(stones))
    return stones


def main():
    """Entry point for the solution."""
    stones = [int(stone) for stone in get_puzzle_input(11).split()]
    stones_after_25_blinks = get_stones_after_blinks(stones, 25)
    print("Solution for day 11, part one:", len(stones_after_25_blinks))
    stones_after_75_blinks = get_stones_after_blinks(stones_after_25_blinks, 50, 25)
    print("Solution for day 11, part two:", len(stones_after_75_blinks))


if __name__ == "__main__":
    main()
