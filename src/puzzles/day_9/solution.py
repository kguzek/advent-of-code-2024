"""Solution for puzzle 9, 2024-12-09"""

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 9


def solve_part_one(input_blocks: list[int]):
    """Calculates the solution for day 9, part one."""
    file_blocks = input_blocks[::2]
    file_id = len(file_blocks) - 1
    free_blocks = input_blocks[1::2]
    free_block_idx = 0
    checksum = 0
    position = file_blocks[0]

    def increment_checksum(file_block_idx: int, blocks_moved: int):
        nonlocal checksum, position
        checksum += file_block_idx * sum(range(position, position + blocks_moved))
        position += blocks_moved

    while any(free_blocks) and file_id > free_block_idx:
        if free_blocks[free_block_idx] == 0:
            free_block_idx += 1
            # Increment by the skipped file blocks
            increment_checksum(free_block_idx, file_blocks[free_block_idx])
            continue
        file_blocks_moved = min(free_blocks[free_block_idx], file_blocks[file_id])
        free_blocks[free_block_idx] -= file_blocks_moved
        file_blocks[file_id] -= file_blocks_moved
        increment_checksum(file_id, file_blocks_moved)
        if file_blocks[file_id] == 0:
            file_id -= 1
    return checksum


def solve_part_two(input_blocks: list[int]):
    """Calculates the solution for day 9, part two."""
    file_blocks = input_blocks[::2]
    file_id = len(file_blocks) - 1
    free_blocks = input_blocks[1::2]
    checksum = 0

    def increment_checksum(file_block_idx: int, blocks_moved: int, position: int):
        nonlocal checksum
        checksum += file_block_idx * sum(range(position, position + blocks_moved))

    while file_id >= 0:
        for idx, free in enumerate(free_blocks):
            if free < file_blocks[file_id]:
                continue
            # print("...", file_id, file_blocks, free_blocks, idx)
            increment_checksum(
                file_id,
                file_blocks[file_id],
                sum(file_blocks[: idx + 1] + input_blocks[1::2][: idx + 1])
                - free_blocks[idx],
            )
            free_blocks[idx] -= file_blocks[file_id]
            file_blocks[file_id] = 0
            break
        file_id -= 1
    position = 0
    for idx, blocks in enumerate(file_blocks):
        if idx > 0 and blocks >= 0:
            increment_checksum(idx, blocks, position)
        position += (
            input_blocks[1::2][idx] if idx < len(free_blocks) else 0
        ) + input_blocks[::2][idx]
    return checksum


def main():
    """Entry point for the solution."""
    input_blocks = [int(c) for c in get_puzzle_input(9).strip()]
    print("Solution for day 9, part one:", solve_part_one(input_blocks))
    print("Solution for day 9, part two:", solve_part_two(input_blocks))


if __name__ == "__main__":
    main()
