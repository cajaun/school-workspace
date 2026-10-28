"""Tests for the non-graphical maze search functions"""

import unittest

from maze_data import BENCHMARK_GOAL, BENCHMARK_MAZE, BENCHMARK_START, copy_maze
from maze_solver import astar, bfs, dfs


def _assert_valid_path(test_case, maze, start, goal, path):
    test_case.assertTrue(path)
    test_case.assertEqual(path[0], start)
    test_case.assertEqual(path[-1], goal)
    for current, following in zip(path, path[1:]):
        test_case.assertEqual(abs(current[0] - following[0]) + abs(current[1] - following[1]), 1)
        test_case.assertIn(maze[following[0]][following[1]], {"0", "S", "G", 0})


class MazeSolverTests(unittest.TestCase):
    def test_bfs_finds_shortest_benchmark_path(self):
        maze = copy_maze(BENCHMARK_MAZE)
        path, visited_order, stats = bfs(maze, BENCHMARK_START, BENCHMARK_GOAL)
        _assert_valid_path(self, maze, BENCHMARK_START, BENCHMARK_GOAL, path)
        self.assertEqual(stats["path_length"], 15)
        self.assertEqual(stats["path_cost"], 14)
        self.assertTrue(visited_order)

    def test_dfs_finds_a_valid_benchmark_path(self):
        maze = copy_maze(BENCHMARK_MAZE)
        path, _, stats = dfs(maze, BENCHMARK_START, BENCHMARK_GOAL)
        _assert_valid_path(self, maze, BENCHMARK_START, BENCHMARK_GOAL, path)
        self.assertEqual(stats["path_length"], len(path))

    def test_astar_finds_optimal_benchmark_path(self):
        maze = copy_maze(BENCHMARK_MAZE)
        path, _, stats = astar(maze, BENCHMARK_START, BENCHMARK_GOAL)
        _assert_valid_path(self, maze, BENCHMARK_START, BENCHMARK_GOAL, path)
        self.assertEqual(stats["path_length"], 15)
        self.assertEqual(stats["path_cost"], 14)

    def test_algorithms_accept_integer_rows(self):
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        path, _, _ = astar(maze, (1, 1), (3, 1))
        _assert_valid_path(self, maze, (1, 1), (3, 1), path)

    def test_no_path_returns_empty_path(self):
        maze = [
            list("11111"),
            list("1S101"),
            list("11101"),
            list("100G1"),
            list("11111"),
        ]
        for algorithm in (bfs, dfs, astar):
            path, visited_order, stats = algorithm(maze, (1, 1), (3, 3))
            self.assertEqual(path, [])
            self.assertTrue(visited_order)
            self.assertEqual(stats["path_length"], 0)
            self.assertEqual(stats["path_cost"], 0)

    def test_start_equal_goal(self):
        maze = [list("111"), list("1S1"), list("111")]
        for algorithm in (bfs, dfs, astar):
            path, visited_order, stats = algorithm(maze, (1, 1), (1, 1))
            self.assertEqual(path, [(1, 1)])
            self.assertEqual(visited_order, [(1, 1)])
            self.assertEqual(stats["path_length"], 1)

    def test_solver_does_not_mutate_maze(self):
        maze = copy_maze(BENCHMARK_MAZE)
        original = copy_maze(maze)
        bfs(maze, BENCHMARK_START, BENCHMARK_GOAL)
        dfs(maze, BENCHMARK_START, BENCHMARK_GOAL)
        astar(maze, BENCHMARK_START, BENCHMARK_GOAL)
        self.assertEqual(maze, original)


if __name__ == "__main__":
    unittest.main()
