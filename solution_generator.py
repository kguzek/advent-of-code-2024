"""Common functions for all puzzles."""

import os

from puzzle_input import get_puzzle_input

SOLUTION_FILE_TEMPLATE = '''
"""Solution for puzzle {day}, 2024-12-{dayPadded}"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = {day}
'''


def setup_solution(day: int):
    """Creates the directory in puzzles/{day} and saves the input to input.txt"""
    print(f"Setting up solution for puzzle {day}...")
    directory = f"puzzles/{day}"
    os.makedirs(directory, exist_ok=True)
    input_text = get_puzzle_input(day)
    with open(f"{directory}/input.txt", "w", encoding="utf-8") as input_file:
        input_file.write(input_text)
    with open(f"{directory}/solution.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(
            SOLUTION_FILE_TEMPLATE.format(day=day, dayPadded=str(day).zfill(2))
        )
    print("Solution file created.")


def main():
    """Main entry point for the script."""
    day = int(input("Enter the day of the puzzle:\n> "))
    setup_solution(day)


if __name__ == "__main__":
    main()
