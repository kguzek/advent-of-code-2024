# Advent of Code 2024

This is a solution generator and runtime environment for the [Advent of Code 2024](https://adventofcode.com/2024/).

## Generating solution template

From the project root, run:

```sh
./generator.sh [DAY]
```

For the generator script, you can omit the `DAY` parameter if you wish and provide it interactively when prompted.

## Writing a solution

Enter `src/puzzles/day_{DAY}/` and edit `solution.py` to your needs.
When you're finished with your solution, proceed to the next section.

## Running a solution

To execute the solution and test it, run the following from the project root:

```sh
./solver.sh <DAY>
```
Note that the `DAY` parameter is mandatory here.
