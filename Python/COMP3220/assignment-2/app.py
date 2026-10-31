"""coordinate the interactive pixel maze lab"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Callable

from maze_generator import create_maze, generate_maze
from maze_solver import astar, bfs, dfs
from pixel_screens import (
    SOLVERS,
    RunScreenState,
    draw_help,
    draw_menu,
    draw_run,
    draw_settings,
    draw_solver_select,
    palette,
)
from pixel_ui import PixelCanvas
from ui_theme import MAZE_PRESETS, PACE_OPTIONS, THEMES, Theme


ALGORITHMS: dict[str, Callable] = {"bfs": bfs, "dfs": dfs, "astar": astar}


class MazeApp:
    """coordinate the game surface, solver state, and screen transitions"""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Maze Lab | COMP3220")
        self.root.geometry("1280x840")
        self.root.minsize(1280, 840)
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.bind("<Escape>", self._handle_escape)
        self.root.bind("<space>", self._handle_space)
        self.root.bind("<Up>", self._handle_menu_up)
        self.root.bind("<Down>", self._handle_menu_down)
        self.root.bind("<Return>", self._handle_menu_confirm)

        self.theme_key = "canopy"
        self.theme: Theme = THEMES[self.theme_key]
        self.preset_name = "benchmark"
        self.pace_name = "steady"
        self.show_trace = True
        self.view = "menu"
        self.content: PixelCanvas | None = None
        self.pixel_view: PixelCanvas | None = None

        self.menu_items = ("menu:start", "menu:compare", "menu:options", "menu:help", "menu:exit")
        self.menu_index = 0
        self.solver_index = 0
        self.selected_solver = "bfs"

        self.animation_id: str | None = None
        self.paused = False
        self.active_mode = "bfs"
        self.algorithm_queue: list[str] = []
        self.algorithm_index = 0
        self.maze = []
        self.start = (0, 0)
        self.goal = (0, 0)
        self.backdrop_maze = generate_maze(25, 39, seed=3220)[0]
        self.path = []
        self.visited_order = []
        self.stats = {}
        self.phase = "idle"
        self.visit_index = 0
        self.path_index = 0
        self.progress = 0.0
        self.status_text = "mapping the maze"
        self.expanded_text = "—"
        self.route_text = "—"
        self.cost_text = "—"

        self.show_menu()

    def run(self) -> None:
        self.root.mainloop()

    def show_menu(self) -> None:
        self._cancel_animation()
        self.view = "menu"
        self.menu_index = 0
        self._show_pixel(self._draw_menu)

    def show_solver_select(self) -> None:
        self._cancel_animation()
        self.view = "solver_select"
        self.solver_index = SOLVERS.index(self.selected_solver)
        self._show_pixel(self._draw_solver_select)

    def show_settings(self) -> None:
        self._cancel_animation()
        self.view = "settings"
        self._show_pixel(self._draw_settings)

    def show_help(self) -> None:
        self._cancel_animation()
        self.view = "help"
        self._show_pixel(self._draw_help)

    def _show_run(self) -> None:
        self._cancel_animation()
        self.view = "run"
        self._show_pixel(self._draw_run)
        self.root.after(100, self._solve_active)

    def _show_pixel(self, drawer: Callable[[PixelCanvas], None]) -> None:
        self._clear_content()
        self.root.configure(bg=self.theme.background)
        self.pixel_view = PixelCanvas(
            self.root,
            self.theme.background,
            self._handle_pixel_action,
            palette(self.theme),
        )
        self.pixel_view.pack(fill="both", expand=True)
        self.content = self.pixel_view
        # rebuild targets with every state change so input stays in sync
        self.pixel_view.render(drawer)

    def _handle_pixel_action(self, key: str) -> None:
        if key == "back" or key.endswith(":back"):
            self.show_menu()
            return
        if key == "menu:start":
            self.show_solver_select()
        elif key == "menu:compare":
            self._start_comparison()
        elif key == "menu:options":
            self.show_settings()
        elif key == "menu:help":
            self.show_help()
        elif key == "menu:exit":
            self.root.destroy()
        elif key.startswith("select:solver:"):
            self.selected_solver = key.rsplit(":", 1)[-1]
            self.solver_index = SOLVERS.index(self.selected_solver)
            self._render_pixel()
        elif key == "select:start":
            self._start_single(self.selected_solver)
        elif key == "select:settings":
            self.show_settings()
        elif key.startswith("settings:preset:"):
            self.preset_name = key.rsplit(":", 1)[-1]
            self._render_pixel()
        elif key.startswith("settings:pace:"):
            self.pace_name = key.rsplit(":", 1)[-1]
            self._render_pixel()
        elif key.startswith("settings:theme:"):
            self.theme_key = key.rsplit(":", 1)[-1]
            self.theme = THEMES[self.theme_key]
            self.show_settings()
        elif key == "settings:trace":
            self.show_trace = not self.show_trace
            self._render_pixel()
        elif key == "run:menu":
            self.show_menu()
        elif key == "run:pause":
            self._toggle_pause()
        elif key == "run:next":
            self._next_algorithm()
        elif key == "run:restart":
            self._restart_run()
        elif key == "run:new":
            self._new_maze()

    def _draw_menu(self, screen: PixelCanvas) -> None:
        draw_menu(screen, self.theme, self.menu_items, self.menu_index, self.backdrop_maze)

    def _draw_solver_select(self, screen: PixelCanvas) -> None:
        draw_solver_select(screen, self.theme, self.selected_solver, self.maze, self.start, self.goal)

    def _draw_settings(self, screen: PixelCanvas) -> None:
        draw_settings(screen, self.theme, self.preset_name, self.pace_name, self.theme_key, self.show_trace)

    def _draw_help(self, screen: PixelCanvas) -> None:
        draw_help(screen, self.theme)

    def _draw_run(self, screen: PixelCanvas) -> None:
        state = RunScreenState(
            active_mode=self.active_mode,
            algorithm_queue=self.algorithm_queue,
            algorithm_index=self.algorithm_index,
            selected_solver=self.selected_solver,
            preset_name=self.preset_name,
            maze=self.maze,
            start=self.start,
            goal=self.goal,
            visited_order=self.visited_order,
            visit_index=self.visit_index,
            path=self.path,
            path_index=self.path_index,
            progress=self.progress,
            status_text=self.status_text,
            expanded_text=self.expanded_text,
            route_text=self.route_text,
            cost_text=self.cost_text,
            paused=self.paused,
            pace_name=self.pace_name,
        )
        draw_run(screen, self.theme, state)

    def _render_pixel(self) -> None:
        if self.pixel_view is not None:
            self.pixel_view.render()

    def _start_single(self, name: str) -> None:
        self._begin_run([name], name)

    def _start_comparison(self) -> None:
        self._begin_run(["bfs", "dfs", "astar"], "all")

    def _begin_run(self, algorithm_queue: list[str], mode: str) -> None:
        self._cancel_animation()
        self.active_mode = mode
        self.algorithm_queue = algorithm_queue
        self.algorithm_index = 0
        self.maze, self.start, self.goal = create_maze(self.preset_name)
        self._show_run()

    def _solve_active(self) -> None:
        if self.view != "run":
            return
        algorithm_name = self.algorithm_queue[self.algorithm_index]
        self.path, self.visited_order, self.stats = ALGORITHMS[algorithm_name](self.maze, self.start, self.goal)
        self.visit_index = 0
        self.path_index = 0
        self.progress = 0
        self.phase = "visited" if self.show_trace else "path"
        self.paused = False
        self.status_text = "exploring the maze"
        self.expanded_text = "0"
        self.route_text = "0"
        self.cost_text = "0"
        self._render_pixel()
        self._animate_next()

    def _animate_next(self) -> None:
        if self.view != "run" or self.paused:
            return
        if self.phase == "visited" and self.visit_index < len(self.visited_order):
            self.visit_index += 1
            self.expanded_text = str(self.visit_index)
            self.progress = self.visit_index / max(1, len(self.visited_order)) * 70
            self._render_pixel()
            self.animation_id = self.root.after(PACE_OPTIONS[self.pace_name]["delay"], self._animate_next)
            return
        if self.phase == "visited":
            self.phase = "path"
            self.status_text = "tracing the route"
            self._render_pixel()
        if self.phase == "path" and self.path_index < len(self.path):
            self.path_index += 1
            self.route_text = str(self.path_index)
            self.cost_text = str(max(0, self.path_index - 1))
            self.progress = 70 + self.path_index / max(1, len(self.path)) * 30
            self._render_pixel()
            self.animation_id = self.root.after(PACE_OPTIONS[self.pace_name]["delay"], self._animate_next)
            return
        self._finish_run()

    def _finish_run(self) -> None:
        self.phase = "complete"
        self.progress = 100
        self.expanded_text = str(self.stats.get("nodes_expanded", 0))
        self.route_text = str(self.stats.get("path_length", 0))
        self.cost_text = str(self.stats.get("path_cost", 0))
        self.status_text = "route found" if self.path else "no route found"
        self._render_pixel()

    def _toggle_pause(self) -> None:
        if self.phase == "complete":
            return
        self.paused = not self.paused
        self._render_pixel()
        if not self.paused:
            self._animate_next()

    def _next_algorithm(self) -> None:
        if self.algorithm_index + 1 >= len(self.algorithm_queue):
            return
        self.algorithm_index += 1
        self._show_run()

    def _restart_run(self) -> None:
        self._show_run()

    def _new_maze(self) -> None:
        self.maze, self.start, self.goal = create_maze(self.preset_name)
        self._show_run()

    def _handle_escape(self, _event: tk.Event) -> None:
        if self.view != "menu":
            self.show_menu()

    def _handle_space(self, _event: tk.Event) -> None:
        if self.view == "run":
            self._toggle_pause()

    def _handle_menu_up(self, _event: tk.Event) -> None:
        if self.view == "menu":
            self.menu_index = (self.menu_index - 1) % len(self.menu_items)
            self._render_pixel()
        elif self.view == "solver_select":
            self.solver_index = (self.solver_index - 1) % len(SOLVERS)
            self.selected_solver = SOLVERS[self.solver_index]
            self._render_pixel()

    def _handle_menu_down(self, _event: tk.Event) -> None:
        if self.view == "menu":
            self.menu_index = (self.menu_index + 1) % len(self.menu_items)
            self._render_pixel()
        elif self.view == "solver_select":
            self.solver_index = (self.solver_index + 1) % len(SOLVERS)
            self.selected_solver = SOLVERS[self.solver_index]
            self._render_pixel()

    def _handle_menu_confirm(self, _event: tk.Event) -> None:
        if self.view == "menu":
            self._handle_pixel_action(self.menu_items[self.menu_index])
        elif self.view == "solver_select":
            self._start_single(self.selected_solver)

    def _clear_content(self) -> None:
        self._cancel_animation()
        if self.content is not None:
            self.content.destroy()
            self.content = None
        self.pixel_view = None

    def _cancel_animation(self) -> None:
        if self.animation_id is not None:
            self.root.after_cancel(self.animation_id)
            self.animation_id = None
        self.paused = False


def launch() -> None:
    try:
        MazeApp().run()
    except tk.TclError as error:
        messagebox.showerror("Maze Lab", f"the desktop window could not open:\n{error}")
