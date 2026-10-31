"""generate playable maze layouts without changing the assignment maze"""

from __future__ import annotations

import random
from typing import Sequence

from maze_data import BENCHMARK_GOAL, BENCHMARK_MAZE, BENCHMARK_START, copy_maze
from ui_theme import MAZE_PRESETS


Position = tuple[int, int]
MazeBundle = tuple[list[list[str]], Position, Position]


def generate_maze(rows: int, cols: int, seed: int | None = None) -> MazeBundle:
    """carve a connected maze with a deterministic option for testing"""
    if rows < 5 or cols < 5:
        raise ValueError("generated mazes must be at least 5 by 5")

    rows = rows if rows % 2 else rows - 1
    cols = cols if cols % 2 else cols - 1
    rng = random.Random(seed)
    maze = [["1" for _ in range(cols)] for _ in range(rows)]
    start = (1, 1)
    goal = (rows - 2, cols - 2)
    stack = [start]
    maze[start[0]][start[1]] = "0"

    while stack:
        # carve by odd cells so every passage stays connected
        current_row, current_col = stack[-1]
        choices = []
        for row_change, col_change in ((2, 0), (0, 2), (-2, 0), (0, -2)):
            next_row = current_row + row_change
            next_col = current_col + col_change
            if 1 <= next_row < rows - 1 and 1 <= next_col < cols - 1:
                if maze[next_row][next_col] == "1":
                    choices.append((next_row, next_col, row_change // 2, col_change // 2))

        if not choices:
            stack.pop()
            continue

        next_row, next_col, wall_row, wall_col = rng.choice(choices)
        maze[current_row + wall_row][current_col + wall_col] = "0"
        maze[next_row][next_col] = "0"
        stack.append((next_row, next_col))

    maze[start[0]][start[1]] = "S"
    maze[goal[0]][goal[1]] = "G"
    return maze, start, goal


def create_maze(preset_name: str, seed: int | None = None) -> MazeBundle:
    """return the selected maze and keep the benchmark layout untouched"""
    if preset_name == "benchmark":
        return copy_maze(BENCHMARK_MAZE), BENCHMARK_START, BENCHMARK_GOAL

    preset = MAZE_PRESETS.get(preset_name)
    if preset is None or "rows" not in preset or "cols" not in preset:
        raise ValueError(f"unknown maze preset: {preset_name}")
    return generate_maze(preset["rows"], preset["cols"], seed)


def maze_is_connected(maze: Sequence[Sequence[object]], start: Position, goal: Position) -> bool:
    """check that a generated maze has a route between its endpoints"""
    frontier = [start]
    seen = {start}
    while frontier:
        row, col = frontier.pop()
        if (row, col) == goal:
            return True
        for row_change, col_change in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            next_position = row + row_change, col + col_change
            next_row, next_col = next_position
            if not (0 <= next_row < len(maze) and 0 <= next_col < len(maze[0])):
                continue
            if next_position in seen or str(maze[next_row][next_col]) == "1":
                continue
            seen.add(next_position)
            frontier.append(next_position)
    return False
