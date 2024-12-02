"""Common functions for all puzzles."""

import os

from .puzzle_input import get_puzzle_input, PUZZLES_FILEPATH, INPUT_FILEPATH


INIT_FILE_TEMPLATE = '''"""Package definition for puzzle {day} solution files"""
'''

SOLUTION_FILE_TEMPLATE = '''"""Solution for puzzle {day}, 2024-12-{dayPadded}"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = {day}


def solve_part_one():
    """Calculates the solution for day {day}, part one."""
    input_text = get_puzzle_input(SOLUTION_DAY)


def solve_part_two():
    """Calculates the solution for day {day}, part two."""
    input_text = get_puzzle_input(SOLUTION_DAY)

if __name__ == "__main__":
    print("Solution for day {day}, part one:", solve_part_one())
    print("Solution for day {day}, part two:", solve_part_two())
'''


def setup_solution(day: int):
    """Creates the directory in puzzles/{day} and saves the input to input.txt"""
    print(f"Setting up solution for puzzle {day}...")
    directory = f"{PUZZLES_FILEPATH}/day_{day}"
    os.makedirs(directory, exist_ok=True)
    input_text = get_puzzle_input(day)
    with open(INPUT_FILEPATH.format(day=day), "w", encoding="utf-8") as input_file:
        input_file.write(input_text)
    with open(f"{directory}/solution.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(
            SOLUTION_FILE_TEMPLATE.format(day=day, dayPadded=str(day).zfill(2))
        )
    with open(f"{directory}/__init__.py", "w", encoding="utf-8") as init_file:
        init_file.write(INIT_FILE_TEMPLATE.format(day=day))
    print("Solution file created.")


def main():
    """Main entry point for the script."""
    day = int(input("Enter the day of the puzzle:\n> "))
    setup_solution(day)


if __name__ == "__main__":
    main()
