COMP3220 maze solver
====================

This project solves a grid maze with breadth-first search, depth-first search,
and A* search. The search functions stay in maze_solver.py so they can run
without opening a graphics window. visualization.py draws their returned search
trace and final path with turtle.

requirements
------------

- Python 3.10 or newer
- A desktop session that supports tkinter and turtle

run the tests
-------------

From this directory, run:

    python3 -m unittest -v

run the visualizer
------------------

Run the interactive version:

    python3 main.py

Choose bfs, dfs, astar, or all when prompted. Enter a delay in seconds to
control the animation speed. This speed control is the creative enhancement.

You can also select a mode from the command line:

    python3 main.py --algorithm bfs --delay 0.04
    python3 main.py --algorithm dfs --delay 0.04
    python3 main.py --algorithm astar --delay 0.04
    python3 main.py --algorithm all --delay 0.04

project layout
--------------

- maze_solver.py contains the required bfs, dfs, and astar functions
- maze_data.py stores the required benchmark maze
- visualization.py renders search results with turtle
- main.py provides the command line interface
- test_maze_solver.py checks correctness without graphics

The benchmark comparison must use the maze in maze_data.py without changing
its cells. Each solver returns a path, a visited order, and statistics with
nodes_expanded, path_length, and path_cost keys. The handout expects the
benchmark path_length to be 15, which counts the 15 cells in the returned path.
The corresponding unit-cost path_cost is 14 moves.

ai disclosure
-------------

AI assistance was used for code structure, implementation support, and code review. The author reviewed and tested the submitted code.
