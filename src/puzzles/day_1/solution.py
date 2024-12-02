"""Solution for puzzle 1, 2024-12-01"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 1


def solve_alternative():
    """Calculates the solution for day 1."""
    input_text = get_puzzle_input(SOLUTION_DAY)
    result = 0
    for line in input_text:
        a, b = line.split()
        result += int(a) - int(b)
    return abs(result)


def solve():
    """Calculates the solution for day 1."""
    input_text = get_puzzle_input(SOLUTION_DAY)
    list_a = []
    list_b = []
    for line in input_text:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
    # Sum the pairs of elements of lista and listb sorted ascending
    result = sum(abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b)))

    print(result, solve_alternative())
    return result


if __name__ == "__main__":
    print("Solution for day 1:", solve())
