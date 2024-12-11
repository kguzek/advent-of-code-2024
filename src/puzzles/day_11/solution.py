"""Solution for puzzle 11, 2024-12-11"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 11


def get_stones_after_blinks(
    stones: list[str], times_blinked: int, blink_offset: int = 0
):
    """Computes the list of stones after the given number of blinks."""
    for blink in range(times_blinked):
        print("Blink", blink + blink_offset)
        new_stones: list[str] = []
        for stone in stones:
            stone_int = int(stone)
            # To eliminate unnecessary leading zeros
            stone = str(stone_int)
            if stone_int == 0:
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                half_stone_length = len(stone) // 2
                new_stones.append(stone[:half_stone_length])
                new_stones.append(stone[half_stone_length:])
            else:
                new_stones.append(str(stone_int * 2024))
        stones = new_stones
    return stones


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(11).split()
    stones_after_25_blinks = get_stones_after_blinks(input_text, 25)
    print("Solution for day 11, part one:", len(stones_after_25_blinks))
    stones_after_75_blinks = get_stones_after_blinks(stones_after_25_blinks, 50, 25)
    print("Solution for day 11, part two:", len(stones_after_75_blinks))


if __name__ == "__main__":
    main()
