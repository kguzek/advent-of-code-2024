"""Solution for puzzle 12, 2024-12-12"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 12


class Region:
    """A region of plots on the grid."""

    def __init__(self, region_map: list[str], x: int, y: int):
        self.type = region_map[y][x]
        self.plots: set[tuple[int, int]] = set()
        self.perimeter = 0
        self.number_of_sides = 0
        self._scan_plots(region_map, x, y)
        self.simple_fence_cost = len(self.plots) * self.perimeter
        self.bulk_fence_cost = len(self.plots) * self.number_of_sides

    def contains_plot(self, x: int, y: int) -> bool:
        """Checks if the region contains a plot at the given coordinates."""
        return (x, y) in self.plots

    def _scan_plots(self, region_map: list[str], x: int, y: int) -> bool:
        """Scans the plots around the base plot for plots belonging to the region.

        Returns a tuple containing booleans indicating respectively if the plot is on the edge
        of the region and if it is part of a new side."""
        if not 0 <= x < len(region_map[0]) or not 0 <= y < len(region_map):
            return True, False
        if not region_map[y][x] == self.type:
            return True, False
        self.plots.add((x, y))
        for delta_x, delta_y in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            # Needed to avoid infinite loops
            if self.contains_plot(x + delta_x, y + delta_y):
                continue
            is_at_edge, is_new_side = self._scan_plots(
                region_map, x + delta_x, y + delta_y
            )
            if is_at_edge:
                self.perimeter += 1
            if is_new_side:
                self.number_of_sides += 1
        return False, False


def get_region_data(region_map: list[str]):
    """Returns the regions in the region map."""
    regions: set[Region] = set()
    total_simple_cost = 0
    total_bulk_cost = 0
    height = len(region_map)
    width = len(region_map[0])
    for y in range(height):
        for x in range(width):
            if any(region.contains_plot(x, y) for region in regions):
                continue
            region = Region(region_map, x, y)
            regions.add(region)
            total_simple_cost += region.simple_fence_cost
            total_bulk_cost += region.bulk_fence_cost
    return total_simple_cost, total_bulk_cost


def main():
    """Entry point for the solution."""
    input_text = get_puzzle_input(12).splitlines()
    total_simple_cost, total_bulk_cost = get_region_data(input_text)
    print("Solution for day 12, part one:", total_simple_cost)
    print("Solution for day 12, part two:", total_bulk_cost)


if __name__ == "__main__":
    main()
