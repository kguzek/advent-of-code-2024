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


def get_machine_cost(
    delta_a_x: int,
    delta_a_y: int,
    delta_b_x: int,
    delta_b_y: int,
    prize_coordinates: tuple[int, int],
) -> int:
    """Returns the cost in tokens of using the machine to win the prize."""
    prize_x, prize_y = prize_coordinates
    max_b_presses = int(min(prize_x // delta_b_x, prize_y // delta_b_y))
    for b_presses in range(max_b_presses + 1, 0, -1):
        a_presses = (prize_x - b_presses * delta_b_x) // delta_a_x
        if (
            prize_x != a_presses * delta_a_x + b_presses * delta_b_x
            or prize_y != a_presses * delta_a_y + b_presses * delta_b_y
        ):
            continue
        return 3 * a_presses + b_presses
    # Prize cannot be won
    return 0


def get_tokens_spent(machine_configs: list[str], prize_offset: int = 0) -> int:
    """Gets the minimum number of tokens needed to get all prizes from the machines."""
    tokens_spent = 0
    for machine_config in machine_configs:
        machine_config = parse_machine_config(machine_config)
        delta_a_x, delta_a_y, delta_b_x, delta_b_y, prize_x, prize_y = machine_config
        tokens_spent += get_machine_cost(
            delta_a_x,
            delta_a_y,
            delta_b_x,
            delta_b_y,
            (prize_x + prize_offset, prize_y + prize_offset),
        )
    return tokens_spent


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(13).strip().split("\n\n")
    print("Solution for day 13, part one:", get_tokens_spent(input_text))
    print("Solution for day 13, part two:", get_tokens_spent(input_text, 1e13))


if __name__ == "__main__":
    main()
