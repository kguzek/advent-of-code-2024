"""Solution for puzzle 9, 2024-12-09"""

from itertools import zip_longest

from ...puzzle_input import get_puzzle_input

SOLUTION_DAY = 9


def solve_part_one(file_blocks: list[int], free_blocks: list[int], file_id: int):
    """Calculates the solution for day 9, part one."""
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


def solve_part_two(file_blocks: list[int], free_blocks: list[int], file_id: int):
    """Calculates the solution for day 9, part two."""
    file_blocks_copy = file_blocks.copy()
    free_blocks_copy = free_blocks.copy()
    checksum = 0

    def increment_checksum(file_block_idx: int, blocks_moved: int, position: int):
        nonlocal checksum
        checksum += file_block_idx * sum(range(position, position + blocks_moved))

    while file_id >= 0:
        for idx, free in enumerate(free_blocks):
            if free < file_blocks[file_id]:
                continue
            if idx >= file_id:
                break
            # print("...", file_id, file_blocks, free_blocks, idx)
            increment_checksum(
                file_id,
                file_blocks[file_id],
                sum(file_blocks[: idx + 1] + free_blocks_copy[: idx + 1])
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
            free_blocks_copy[idx] if idx < len(free_blocks) else 0
        ) + file_blocks_copy[idx]
    return checksum


def visualise_part_two(file_blocks: list[int], free_blocks: list[int], file_id: int):
    """Visualize the current state of the file and free blocks."""
    block_groups = [
        [str(file_id) * file_length, "." * free_length]
        for ((file_id, file_length), (_, free_length)) in zip_longest(
            enumerate(file_blocks), enumerate(free_blocks), fillvalue=(0, 0)
        )
    ]

    yield "".join(block for block_group in block_groups for block in block_group)

    while file_id >= 0:
        for idx, free in enumerate(free_blocks):
            if free < file_blocks[file_id]:
                continue
            if idx >= file_id:
                break
            free_blocks[idx] -= file_blocks[file_id]
            block_groups[idx] = block_groups[idx][:-1] + [
                f"{file_id}" * file_blocks[file_id],
                "." * free_blocks[idx],
            ]
            block_groups[file_id][0] = "." * file_blocks[file_id]
            file_blocks[file_id] = 0
            break
        yield "".join(block for block_group in block_groups for block in block_group)
        file_id -= 1
    yield block_groups


def main():
    """Entry point for the solution."""
    input_blocks = [int(c) for c in get_puzzle_input(9).strip()]
    file_blocks = input_blocks[::2]
    file_id = len(file_blocks) - 1
    free_blocks = input_blocks[1::2]
    print(
        "Solution for day 9, part one:",
        solve_part_one(file_blocks[:], free_blocks[:], file_id),
    )
    print(
        "Solution for day 9, part two:",
        solve_part_two(file_blocks[:], free_blocks[:], file_id),
    )
    # for visualisation in visualise_part_two(file_blocks[:], free_blocks[:], file_id):
    #     print(visualisation)


if __name__ == "__main__":
    main()
