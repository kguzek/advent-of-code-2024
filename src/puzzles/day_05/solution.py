"""Solution for puzzle 5, 2024-12-05"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 5


def solve_part_one(orders: list[str], updates: list[str]):
    """Calculates the solution for day 5, part one."""
    return sum(
        int(pages.split(",")[pages.count(",") // 2])
        for pages in updates
        if all(
            page_before not in pages
            or page_after not in pages
            or pages.index(page_before) < pages.index(page_after)
            for order in orders
            for page_before, page_after in (order.split("|"),)
        )
    )


def solve_part_two(orders: list[str], updates: list[str]):
    """Calculates the solution for day 5, part two."""

    def sort_update(update: list[str]):
        updated = False
        for page in update:
            for order in orders:
                page_before, page_after = order.split("|")
                if page_before != page:
                    continue
                try:
                    page_after_idx = update.index(page_after)
                except ValueError:
                    continue
                if update.index(page_before) < page_after_idx:
                    continue
                update.remove(page_before)
                update.insert(page_after_idx, page_before)
                updated = True
        return int(update[len(update) // 2]) if updated else 0

    return sum(sort_update(update.split(",")) for update in updates)


def main():
    """Entry point for the solution."""
    orders, page_groups = map(
        lambda s: s.splitlines(), get_puzzle_input(5).split("\n\n")
    )
    print("Solution for day 5, part one:", solve_part_one(orders, page_groups))
    print("Solution for day 5, part two:", solve_part_two(orders, page_groups))


if __name__ == "__main__":
    main()
