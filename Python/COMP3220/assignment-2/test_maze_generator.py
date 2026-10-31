"""Tests for generated practice mazes"""

import unittest

from maze_generator import create_maze, generate_maze, maze_is_connected


class MazeGeneratorTests(unittest.TestCase):
    def test_generated_maze_has_a_route(self):
        maze, start, goal = generate_maze(15, 23, seed=3101)
        self.assertTrue(maze_is_connected(maze, start, goal))
        self.assertEqual(maze[start[0]][start[1]], "S")
        self.assertEqual(maze[goal[0]][goal[1]], "G")

    def test_preset_sizes_are_supported(self):
        for preset in ("training", "labyrinth"):
            maze, start, goal = create_maze(preset, seed=3101)
            self.assertTrue(maze_is_connected(maze, start, goal))
            self.assertEqual(len(maze) % 2, 1)
            self.assertEqual(len(maze[0]) % 2, 1)

    def test_benchmark_preset_keeps_assignment_layout(self):
        maze, start, goal = create_maze("benchmark")
        self.assertEqual(start, (1, 1))
        self.assertEqual(goal, (8, 8))
        self.assertEqual(len(maze), 10)
        self.assertEqual(len(maze[0]), 10)


if __name__ == "__main__":
    unittest.main()
