"""Solution for puzzle 5, 2024-12-05"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 5


def solve_part_one(orders: list[str], page_groups: list[str]):
    """Calculates the solution for day 5, part one."""
    return sum(
        int(pages.split(",")[pages.count(",") // 2])
        for pages in page_groups
        if all(
            page_before not in pages
            or page_after not in pages
            or pages.index(page_before) < pages.index(page_after)
            for order in orders
            for page_before, page_after in (order.split("|"),)
        )
    )


def solve_part_two(orders: list[str], page_groups: list[str]):
    """Calculates the solution for day 5, part two."""

    def sort_pages(pages: list[int]):
        for page in pages:
            for order in orders:
                page_before, page_after = (int(order) for order in order.split("|"))
                if page_before != page:
                    continue
                try:
                    page_after_idx = pages.index(page_after)
                except ValueError:
                    continue
                if pages.index(page_before) < page_after_idx:
                    continue
                pages.remove(page_before)
                pages.insert(page_after_idx, page_before)
        return pages

    return sum(
        int(sort_pages([int(page) for page in pages.split(",")])[pages.count(",") // 2])
        for pages in page_groups
    )


def main():
    """Entry point for the solution."""
    orders, page_groups = map(
        lambda s: s.splitlines(), get_puzzle_input(5).split("\n\n")
    )
    print("Solution for day 5, part one:", solve_part_one(orders, page_groups))
    print("Solution for day 5, part two:", solve_part_two(orders, page_groups))


if __name__ == "__main__":
    main()
