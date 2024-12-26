"""Solution for puzzle 1, 2024-12-01"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 1


def create_lists():
    """Generates two lists from the input."""
    input_text = get_puzzle_input(SOLUTION_DAY).splitlines()
    return zip(*(map(int, line.split()) for line in input_text))


def solve_part_one():
    """Calculates the solution for day 1."""
    list_a, list_b = create_lists()
    # Sum the pairs of elements of list_a and list_b sorted ascending
    return sum(abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b)))


def solve_part_two():
    """Calculates the solution for day 1, part 2."""
    list_a, list_b = create_lists()
    return sum(i * list_b.count(i) for i in list_a)


if __name__ == "__main__":
    print("Solution for day 1 part 1:", solve_part_one())
    print("Solution for day 1 part 2:", solve_part_two())
