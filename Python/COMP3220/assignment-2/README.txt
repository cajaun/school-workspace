# COMP3220 Maze Lab

Maze Lab solves grid mazes with breadth-first search, depth-first search, and A* search. You can run each search in a pixel-art desktop view. The maze displays explored cells, the route appears in yellow, and the side panel reports search statistics.

The program keeps the assignment maze in `maze_data.py`. The solver functions read that maze and return their results without changing its cells. The app then uses those results to animate the run.

## Requirements

- Python 3.10 or newer
- Tkinter for the desktop window
- Pillow for the pixel-font renderer

The project keeps an original turtle renderer in `visualization.py` for comparison.

## Install

Open a terminal in this directory and install Pillow:

```bash
python3 -m pip install -r requirements.txt
```

## Run the app

Start Maze Lab with:

```bash
python3 main.py
```

The app opens a fixed 1280 by 840 window. Use the mouse or keyboard to move through the menus.

### Controls

- `up` and `down` move through the main menu and solver list
- `enter` confirms the highlighted choice
- `space` pauses or resumes a run
- `escape` returns to the main menu
- mouse movement highlights clickable controls
- mouse clicks activate controls

## Use the interface

Choose `start` to select one search strategy. Choose `compare` to run BFS, DFS, and A* on the same maze.

The options screen lets you choose:

- `assignment maze`, which preserves the handout layout
- `training grounds`, a compact generated maze
- `the labyrinth`, a larger generated maze
- `slow`, `steady`, or `turbo` animation pace
- `canopy`, `moon`, or `ember` color palette
- search trail visibility

The mode preview shows the selected strategy and its route on the active maze. During a run, the route map shows the search trace and the side panel reports expanded nodes, route length, moves, and pace.

## Run the tests

Run the full test suite from this directory:

```bash
python3 -m unittest -v
```

The tests check solver correctness, path statistics, input validation behavior, maze immutability, generated maze connectivity, and preset dimensions.

You can check every Python file for syntax errors with:

```bash
python3 -m py_compile *.py
```

## Solver contract

Each solver accepts:

```python
path, visited_order, stats = algorithm(maze, start, goal)
```

The maze uses these cell values:

- `1` marks a wall
- `0` marks an open cell
- `S` marks the start
- `G` marks the goal

The returned values mean:

- `path` contains the route from start to goal, including both endpoints
- `visited_order` records the order in which the algorithm expands cells
- `stats["nodes_expanded"]` counts expanded cells
- `stats["path_length"]` counts cells in the returned route
- `stats["path_cost"]` counts unit-cost moves

For the benchmark maze, BFS and A* return a path length of 15 and a path cost of 14. DFS returns a valid route and may explore the maze in a different order.

## Project structure

```text
assignment-2/
├── app.py                  desktop state, navigation, and animation
├── assets/
│   └── PressStart2P.ttf    bundled pixel typeface
├── main.py                 application entry point
├── maze_data.py            assignment maze and endpoint data
├── maze_generator.py       connected practice-maze generation
├── maze_solver.py          BFS, DFS, A*, validation, and statistics
├── pixel_screens.py        screen layouts rendered from explicit state
├── pixel_ui.py             pixel canvas, text, panels, buttons, and targets
├── requirements.txt        Python package requirements
├── test_maze_generator.py  generated-maze tests
├── test_maze_solver.py     solver tests
├── ui_theme.py             palettes, labels, presets, and pace settings
└── visualization.py        original turtle renderer
```

The modules follow one direction of responsibility. `maze_solver.py` handles search. `maze_generator.py` creates optional practice layouts. `pixel_ui.py` handles drawing primitives and input targets. `pixel_screens.py` turns application state into screen layouts. `app.py` coordinates navigation and animation.

## Design decisions

The solver code stays independent from Tkinter, Pillow, and turtle. Tests can call BFS, DFS, and A* without opening a window. The app receives the solver results and controls how each result appears on screen.

The benchmark maze remains separate from generated mazes. This keeps the assignment data stable while the options screen supports practice layouts.

The pixel renderer uses one design coordinate system and one bundled typeface. Each screen uses the same panel, button, text, and maze primitives, so selections, spacing, hover states, and typography stay consistent across the app.

## Troubleshooting

If Pillow is missing, run the install command:

```bash
python3 -m pip install -r requirements.txt
```

If the window does not open, confirm that Python can access Tkinter on your system. macOS users can test the module with:

```bash
python3 -m tkinter
```

Run the tests from the assignment directory so Python can import the project modules.
