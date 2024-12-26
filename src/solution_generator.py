"""Common functions for all puzzles."""

import os
import sys

from puzzle_input import get_puzzle_input, PUZZLE_FILEPATH


INIT_FILE_TEMPLATE = '''"""Package definition for puzzle {day} solution files"""
'''

SOLUTION_FILE_TEMPLATE = '''"""Solution for puzzle {day}, 2024-12-{day_padded}"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = {day}


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day {day}, part one."""


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day {day}, part two."""


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input({day}).splitlines()
    print("Solution for day {day}, part one:", solve_part_one(input_text))
    print("Solution for day {day}, part two:", solve_part_two(input_text))
    

if __name__ == "__main__":
    main()
'''


def setup_solution(day: int):
    """Creates the directory in puzzles/{day} and saves the input to input.txt"""
    print(f"Setting up solution for puzzle {day}...")
    day_padded = str(day).zfill(2)
    directory = PUZZLE_FILEPATH.format(day_padded=day_padded)
    get_puzzle_input(day)
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/solution.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(
            SOLUTION_FILE_TEMPLATE.format(day=day, day_padded=day_padded)
        )
    with open(f"{directory}/__init__.py", "w", encoding="utf-8") as init_file:
        init_file.write(INIT_FILE_TEMPLATE.format(day=day))
    print("Solution file created.")


def main():
    """Main entry point for the script."""
    raw_day = (
        sys.argv[1] if len(sys.argv) > 1 else input("Enter the day of the puzzle:\n> ")
    )
    day = int(raw_day)
    setup_solution(day)


if __name__ == "__main__":
    main()
