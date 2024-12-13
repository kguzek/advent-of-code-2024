"""Solution for puzzle 12, 2024-12-12"""

from itertools import product

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 12


class Region:
    """A region of plots on the grid."""

    def __init__(self, region_map: list[str], x: int, y: int):
        self.type = region_map[y][x]
        self.plots: set[tuple[int, int]] = set()
        self.perimeter = 0
        self._scan_plots(region_map, x, y)
        self.fence_cost = len(self.plots) * self.perimeter

    def contains_plot(self, x: int, y: int) -> bool:
        """Checks if the region contains a plot at the given coordinates."""
        return (x, y) in self.plots

    def _scan_plots(self, region_map: list[str], x: int, y: int) -> bool:
        """Scans the plots around the base plot for plots belonging to the region.

        Returns a boolean indicating if the plot is on the edge of the region."""
        if not 0 <= x < len(region_map[0]) or not 0 <= y < len(region_map):
            return True
        if not region_map[y][x] == self.type:
            return True
        self.plots.add((x, y))
        for delta_x, delta_y in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            # Needed to avoid infinite loops
            if self.contains_plot(x + delta_x, y + delta_y):
                continue
            if self._scan_plots(region_map, x + delta_x, y + delta_y):
                self.perimeter += 1
        return False


def solve_part_one(input_text: list[str]):
    """Calculates the solution for day 12, part one."""
    regions: set[Region] = set()
    total_cost = 0
    for y, row in enumerate(input_text):
        for x, _ in enumerate(row):
            if any(region.contains_plot(x, y) for region in regions):
                continue
            region = Region(input_text, x, y)
            regions.add(region)
            total_cost += region.fence_cost
    return total_cost


def solve_part_two(input_text: list[str]):
    """Calculates the solution for day 12, part two."""


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(12).splitlines()
    print("Solution for day 12, part one:", solve_part_one(input_text))
    print("Solution for day 12, part two:", solve_part_two(input_text))


if __name__ == "__main__":
    main()
