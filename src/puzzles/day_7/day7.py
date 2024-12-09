"""Day 7 solution by github.com/derailed-dash"""

from __future__ import annotations
import operator
from functools import cache, reduce
from itertools import product

# Setup logger
YEAR = 2024
APP_NAME = "aoc" + str(YEAR)


def process_input(data) -> list[tuple]:
    """Return equations in the form: [(answer, numbers), ...]"""
    equations = []
    for line in data:
        ans, nums = line.split(":")
        ans = int(ans)
        nums = list(map(int, nums.split()))
        equations.append((ans, nums))

    return equations


@cache
def get_op_perms(ops: str, num_parameters: int):
    """
    Return all the ways of ordering our operators for a given number of parameters.
    E.g. if ops == "+*" and there are 3 parameters, then we need all permutations of 2 operators:
    [("+", "+"), ("+", "*"), ("*", "+"), ("*", "*")]
    """
    op_perms = list(product(ops, repeat=num_parameters - 1))
    return op_perms


def apply_op(num_pair: tuple[int], op: str) -> int:
    match op:  # Note Python's implementatiom of switch
        case "+":
            return operator.add(*num_pair)
        case "*":
            return operator.mul(*num_pair)
        case "|":
            return int("".join(str(num) for num in num_pair))
        case _:
            raise ValueError(f"Unknown operator: {op}")


def solve(data, ops):
    equations = process_input(data)  # [0] is the ans; [1] are the numbers
    total = 0

    for equation in equations:
        nums = equation[1]

        # get a list of operator combinations, with each element being of length n-1
        # E.g. with 3 numbers, we'll get: [('+', '+'), ('+', '*'), ('*', '+'), ('*', '*')]
        op_perms = get_op_perms(ops, len(nums))

        for op_perm in op_perms:  # a tuple of operators of length n-1
            ans = reduce(
                lambda acc, op_and_right: apply_op(
                    (acc, op_and_right[1]), op_and_right[0]
                ),
                zip(op_perm, nums[1:]),  # zip the operator with the next number
                nums[0],
            )  # Start with the first number

            if ans == equation[0]:
                total += equation[0]
                break  # we only need one successful result per equestion

    return total
