"""Solution for puzzle 7, 2024-12-07"""

from typing import Generator

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 7

# Enables debug output
OPTIMISED_MODE = True


def parse_line(line: str):
    """Parses the input text and returns the data."""
    target, equation = line.split(":")
    return int(target), [int(operand) for operand in equation.split()]


def debug_print(*args, **kwargs):
    """Prints debug output."""
    if not OPTIMISED_MODE:
        print(*args, **kwargs)


def compute(current: int, operand: int, operator: str):
    """Applies the operator to the current value and operand."""
    match operator:
        case "+":
            return current + operand
        case "*":
            return current * operand
        case "|":
            return int(f"{current}{operand}")
        case _:
            raise ValueError(f"Unknown operator: '{operator}'")


def solve_equation(
    target: int,
    equation: list[int],
    operators: tuple[str, ...],
    current: int = None,
    operator: str = None,
    nest_level: int = 0,
):
    """Recursively applies the operator to the equation at the given index."""
    if current is None or operator is None:
        to_print = f"\n\n{" _ ".join(map(str, equation))} -> {target}:"
        current = equation.pop(0)
    else:
        operand = equation.pop(0)
        value = compute(current, operand, operator)
        to_print = f"\n{("· " * nest_level)}{current} {operator} {operand} = {value}"
        current = value
    if len(equation) == 0:
        debug_print(f"{to_print:<60} {"OK" if current == target else "X"}", end="")
        return current == target
    debug_print(to_print, end=" ")
    return any(
        solve_equation(
            target, equation.copy(), operators, current, operator, nest_level + 1
        )
        for operator in operators
    )


def solve(input_text: Generator[tuple[int, list[int]]], operators: str):
    """Calculates the solution for day 7, part one."""
    result = sum(
        target
        for target, equation in input_text
        if solve_equation(target, equation, operators)
    )
    debug_print()
    return result


def main():
    """Entry point for the solution."""
    input_raw = get_puzzle_input(7).splitlines()
    input_text = (parse_line(line) for line in input_raw)
    # print("Solution for day 7, part one:", solve_part_one(input_text))
    operators = "*+|"
    print(
        f"Solution for day 7 using operators {operators}: {solve(input_text, operators)}"
    )


if __name__ == "__main__":
    main()
