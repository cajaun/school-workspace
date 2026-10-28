"""Turtle rendering for maze search results"""

from __future__ import annotations

import time
import turtle
from typing import Sequence


Position = tuple[int, int]

_COLORS = {
    "wall": "#1f2937",
    "open": "#f8fafc",
    "start": "#22c55e",
    "goal": "#ef4444",
    "visited": "#93c5fd",
    "path": "#facc15",
}


def _cell_value(maze: Sequence[Sequence[object]], position: Position) -> object:
    return maze[position[0]][position[1]]


def _draw_square(pen: turtle.Turtle, x: float, y: float, size: float, color: str) -> None:
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()
    pen.penup()


def _draw_legend(pen: turtle.Turtle, x: float, y: float, size: float) -> None:
    labels = (("start", "start"), ("goal", "goal"), ("visited", "visited"), ("path", "path"))
    pen.color("black")
    pen.penup()
    pen.goto(x, y)
    pen.write("legend", font=("Arial", 10, "bold"))
    for index, (color_name, label) in enumerate(labels, start=1):
        box_y = y - index * (size + 8)
        _draw_square(pen, x, box_y, size, _COLORS[color_name])
        pen.color("black")
        pen.goto(x + size + 8, box_y - size + 4)
        pen.write(label, font=("Arial", 9, "normal"))


class MazeRenderer:
    """draw a maze and animate a returned search trace"""

    def __init__(self, maze: Sequence[Sequence[object]], start: Position, goal: Position, cell_size: int = 32):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.cell_size = cell_size
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.screen = turtle.Screen()
        self.screen.title("COMP3220 Maze Solver")
        self.screen.bgcolor("white")
        self.screen.tracer(0, 0)
        self.pen = turtle.Turtle(visible=False)
        self.pen.speed(0)
        self.origin_x = -(self.cols * cell_size) / 2
        self.origin_y = (self.rows * cell_size) / 2

    def _position(self, position: Position) -> tuple[float, float]:
        row, col = position
        return self.origin_x + col * self.cell_size, self.origin_y - row * self.cell_size

    def draw_base(self) -> None:
        self.pen.penup()
        for row in range(self.rows):
            for col in range(self.cols):
                position = row, col
                x, y = self._position(position)
                value = _cell_value(self.maze, position)
                color = _COLORS["wall"] if str(value) == "1" else _COLORS["open"]
                if position == self.start:
                    color = _COLORS["start"]
                elif position == self.goal:
                    color = _COLORS["goal"]
                _draw_square(self.pen, x, y, self.cell_size, color)

        _draw_legend(self.pen, self.origin_x + self.cols * self.cell_size + 20, self.origin_y, self.cell_size / 2)
        self.screen.update()

    def _paint(self, position: Position, color_name: str) -> None:
        if position in {self.start, self.goal}:
            return
        x, y = self._position(position)
        _draw_square(self.pen, x, y, self.cell_size, _COLORS[color_name])

    def animate(self, visited_order: Sequence[Position], path: Sequence[Position], delay: float = 0.04) -> None:
        # draw the trace after the solver returns to keep the layers separate
        for position in visited_order:
            self._paint(position, "visited")
            self.screen.update()
            if delay > 0:
                time.sleep(delay)

        for position in path:
            self._paint(position, "path")
            self.screen.update()
            if delay > 0:
                time.sleep(delay)

        self._paint(self.start, "start")
        self._paint(self.goal, "goal")
        self.screen.update()


def animate_search(
    maze: Sequence[Sequence[object]],
    start: Position,
    goal: Position,
    visited_order: Sequence[Position],
    path: Sequence[Position],
    algorithm_name: str,
    delay: float = 0.04,
) -> None:
    """render one algorithm result and keep the window open"""
    renderer = MazeRenderer(maze, start, goal)
    renderer.screen.title(f"COMP3220 Maze Solver - {algorithm_name}")
    renderer.draw_base()
    renderer.animate(visited_order, path, delay)
    renderer.screen.mainloop()


def keep_window_open() -> None:
    """keep the turtle window available after animation"""
    turtle.mainloop()
