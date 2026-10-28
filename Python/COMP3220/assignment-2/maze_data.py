"""Maze layouts used by the COMP3220 assignment"""


BENCHMARK_MAZE = [
    list("1111111111"),
    list("1S01001001"),
    list("1000101101"),
    list("1110010001"),
    list("1010000001"),
    list("1000001101"),
    list("1000000001"),
    list("1110000101"),
    list("10010000G1"),
    list("1111111111"),
]

BENCHMARK_START = (1, 1)
BENCHMARK_GOAL = (8, 8)


def copy_maze(maze):
    """return a mutable copy without changing the source layout"""
    return [list(row) for row in maze]
