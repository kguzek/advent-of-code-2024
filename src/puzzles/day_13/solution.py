"""Solution for puzzle 13, 2024-12-13"""

import re

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 13

BUTTON_CONFIG_PATTERN = re.compile(
    r"^Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)$"
)


def parse_machine_config(
    machine_config: str,
) -> tuple[int, int, int, int, int, int]:
    """Parses the input text and returns the button configuration for that group."""
    match = BUTTON_CONFIG_PATTERN.fullmatch(machine_config)
    if match is None:
        raise RuntimeError(f"Invalid input:\n'{machine_config}'")
    return tuple(map(int, match.groups()))


def solve_part_one(machine_configs: list[str]):
    """Calculates the solution for day 13, part one."""
    tokens_spent = 0
    for machine_config in machine_configs:
        machine_config = parse_machine_config(machine_config)
        delta_a_x, delta_a_y, delta_b_x, delta_b_y, prize_x, prize_y = machine_config
        max_b_presses = min(prize_x // delta_b_x, prize_y // delta_b_y)
        print(f"{max_b_presses = }")
        for b_presses in range(max_b_presses + 1, 0, -1):
            a_presses = (prize_x - b_presses * delta_b_x) // delta_a_x
            if (
                prize_x != a_presses * delta_a_x + b_presses * delta_b_x
                or prize_y != a_presses * delta_a_y + b_presses * delta_b_y
            ):
                continue
            tokens_spent += 3 * a_presses + b_presses
    return tokens_spent


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 13, part two."""


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(13).strip().split("\n\n")
    print("Solution for day 13, part one:", solve_part_one(input_text))
    print("Solution for day 13, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
