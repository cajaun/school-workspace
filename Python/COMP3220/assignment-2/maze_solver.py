"""Search algorithms for the COMP3220 maze assignment"""

from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from itertools import count
from numbers import Real
from typing import Callable, Sequence


Position = tuple[int, int]
Heuristic = Callable[[Position, Position], int | float]

_DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def manhattan_distance(node: Position, goal: Position) -> int:
    """return the four-direction distance between two cells"""
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def _is_open_cell(value: object) -> bool:
    if isinstance(value, str):
        return value in {"0", "S", "G"}
    return value == 0


def _validate_inputs(maze: Sequence[Sequence[object]], start: Position, goal: Position) -> tuple[int, int]:
    if not maze:
        raise ValueError("maze must contain at least one row")

    width = len(maze[0])
    if width == 0 or any(len(row) != width for row in maze):
        raise ValueError("maze must be rectangular and non-empty")

    rows = len(maze)
    for name, position in (("start", start), ("goal", goal)):
        if len(position) != 2:
            raise ValueError(f"{name} must be a (row, col) pair")
        row, col = position
        if not (0 <= row < rows and 0 <= col < width):
            raise ValueError(f"{name} is outside the maze")
        if not _is_open_cell(maze[row][col]):
            raise ValueError(f"{name} must be on an open cell")

    return rows, width


def _neighbors(
    maze: Sequence[Sequence[object]],
    position: Position,
    rows: int,
    cols: int,
):
    row, col = position
    for row_change, col_change in _DIRECTIONS:
        next_row = row + row_change
        next_col = col + col_change
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if _is_open_cell(maze[next_row][next_col]):
                yield next_row, next_col


def _reconstruct_path(parents: dict[Position, Position | None], start: Position, goal: Position) -> list[Position]:
    if goal not in parents:
        return []

    path: list[Position] = []
    current: Position | None = goal
    while current is not None:
        path.append(current)
        if current == start:
            return path[::-1]
        current = parents[current]

    return []


def _make_stats(path: list[Position], nodes_expanded: int, path_cost: int | float = 0) -> dict[str, int | float]:
    if not path:
        return {
            "nodes_expanded": nodes_expanded,
            "path_length": 0,
            "path_cost": 0,
        }

    return {
        "nodes_expanded": nodes_expanded,
        "path_length": len(path),
        "path_cost": path_cost,
    }


def bfs(maze, start, goal):
    """return a shortest path and the breadth first search trace"""
    rows, cols = _validate_inputs(maze, start, goal)
    frontier = deque([start])
    discovered = {start}
    parents: dict[Position, Position | None] = {start: None}
    visited_order: list[Position] = []

    while frontier:
        current = frontier.popleft()
        visited_order.append(current)

        if current == goal:
            break

        # mark cells when discovered so the queue never duplicates them
        for neighbor in _neighbors(maze, current, rows, cols):
            if neighbor in discovered:
                continue
            discovered.add(neighbor)
            parents[neighbor] = current
            frontier.append(neighbor)

    path = _reconstruct_path(parents, start, goal)
    return path, visited_order, _make_stats(path, len(visited_order), len(path) - 1 if path else 0)


def dfs(maze, start, goal):
    """return a valid path and the depth first search trace"""
    rows, cols = _validate_inputs(maze, start, goal)
    frontier = [start]
    discovered = {start}
    parents: dict[Position, Position | None] = {start: None}
    visited_order: list[Position] = []

    # reverse the neighbors so the first direction stays deterministic
    while frontier:
        current = frontier.pop()
        visited_order.append(current)

        if current == goal:
            break

        neighbors = list(_neighbors(maze, current, rows, cols))
        for neighbor in reversed(neighbors):
            if neighbor in discovered:
                continue
            discovered.add(neighbor)
            parents[neighbor] = current
            frontier.append(neighbor)

    path = _reconstruct_path(parents, start, goal)
    return path, visited_order, _make_stats(path, len(visited_order), len(path) - 1 if path else 0)


def _checked_heuristic(heuristic: Heuristic, node: Position, goal: Position) -> int | float:
    value = heuristic(node, goal)
    if not isinstance(value, Real):
        raise TypeError("heuristic must return a number")
    if value < 0:
        raise ValueError("heuristic must return a non-negative value")
    return value


def astar(maze, start, goal, heuristic=manhattan_distance):
    """return a cost optimal path and the a star search trace"""
    rows, cols = _validate_inputs(maze, start, goal)
    sequence = count()
    start_heuristic = _checked_heuristic(heuristic, start, goal)
    frontier = [(start_heuristic, start_heuristic, next(sequence), start, 0)]
    parents: dict[Position, Position | None] = {start: None}
    g_scores: dict[Position, int] = {start: 0}
    expanded_costs: dict[Position, int] = {}
    visited_order: list[Position] = []

    while frontier:
        _, _, _, current, queued_cost = heappop(frontier)
        current_cost = g_scores.get(current)
        if current_cost is None or queued_cost != current_cost:
            continue

        previous_cost = expanded_costs.get(current)
        if previous_cost is not None and current_cost >= previous_cost:
            continue
        expanded_costs[current] = current_cost
        visited_order.append(current)

        if current == goal:
            break

        # reopen cells when a cheaper route appears
        for neighbor in _neighbors(maze, current, rows, cols):
            tentative_cost = current_cost + 1
            if tentative_cost >= g_scores.get(neighbor, float("inf")):
                continue

            parents[neighbor] = current
            g_scores[neighbor] = tentative_cost
            neighbor_heuristic = _checked_heuristic(heuristic, neighbor, goal)
            heappush(
                frontier,
                (
                    tentative_cost + neighbor_heuristic,
                    neighbor_heuristic,
                    next(sequence),
                    neighbor,
                    tentative_cost,
                ),
            )

    path = _reconstruct_path(parents, start, goal)
    return path, visited_order, _make_stats(path, len(visited_order), g_scores.get(goal, 0))
