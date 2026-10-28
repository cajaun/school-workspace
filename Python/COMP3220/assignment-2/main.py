"""Command line entry point for the maze visualizer"""

from __future__ import annotations

import argparse

from maze_data import BENCHMARK_GOAL, BENCHMARK_MAZE, BENCHMARK_START, copy_maze
from maze_solver import astar, bfs, dfs


ALGORITHMS = {"bfs": bfs, "dfs": dfs, "astar": astar}


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="visualize bfs, dfs, and a star on a maze")
    parser.add_argument("--algorithm", choices=["bfs", "dfs", "astar", "all"])
    parser.add_argument("--delay", type=float, default=None, help="seconds between animation steps")
    return parser.parse_args()


def _choose_algorithm() -> str:
    while True:
        choice = input("choose an algorithm [bfs, dfs, astar, all]: ").strip().lower()
        if choice in {"bfs", "dfs", "astar", "all"}:
            return choice
        print("choose bfs, dfs, astar, or all")


def _choose_delay() -> float:
    while True:
        answer = input("animation delay in seconds [0.04]: ").strip()
        if not answer:
            return 0.04
        try:
            delay = float(answer)
        except ValueError:
            print("enter a non-negative number")
            continue
        if delay >= 0:
            return delay
        print("enter a non-negative number")


def _run_algorithm(name: str, delay: float) -> None:
    from visualization import MazeRenderer

    maze = copy_maze(BENCHMARK_MAZE)
    path, visited_order, stats = ALGORITHMS[name](maze, BENCHMARK_START, BENCHMARK_GOAL)
    print(
        f"{name}: path found={bool(path)}, "
        f"path length={stats['path_length']}, "
        f"nodes expanded={stats['nodes_expanded']}"
    )

    renderer = MazeRenderer(maze, BENCHMARK_START, BENCHMARK_GOAL)
    renderer.screen.title(f"COMP3220 Maze Solver - {name}")
    renderer.draw_base()
    renderer.animate(visited_order, path, delay)


def main() -> None:
    from visualization import keep_window_open

    arguments = _parse_arguments()
    algorithm = arguments.algorithm or _choose_algorithm()
    delay = arguments.delay if arguments.delay is not None else _choose_delay()
    if delay < 0:
        raise SystemExit("delay must be non-negative")

    if algorithm == "all":
        for name in ("bfs", "dfs", "astar"):
            _run_algorithm(name, delay)
    else:
        _run_algorithm(algorithm, delay)

    keep_window_open()


if __name__ == "__main__":
    main()
