"""render each pixel screen from explicit application state"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from maze_data import BENCHMARK_GOAL, BENCHMARK_MAZE, BENCHMARK_START
from maze_solver import bfs
from pixel_ui import PixelCanvas
from ui_theme import ALGORITHM_DETAILS, MAZE_PRESETS, PACE_OPTIONS, THEMES, Theme


SOLVERS = ("bfs", "dfs", "astar")


@dataclass(frozen=True)
class RunScreenState:
    active_mode: str
    algorithm_queue: Sequence[str]
    algorithm_index: int
    selected_solver: str
    preset_name: str
    maze: Sequence[Sequence[object]]
    start: tuple[int, int]
    goal: tuple[int, int]
    visited_order: Sequence[tuple[int, int]]
    visit_index: int
    path: Sequence[tuple[int, int]]
    path_index: int
    progress: float
    status_text: str
    expanded_text: str
    route_text: str
    cost_text: str
    paused: bool
    pace_name: str


def palette(theme: Theme) -> dict[str, str]:
    return {
        "background": theme.background,
        "surface": theme.surface,
        "surface_alt": theme.surface_alt,
        "border": theme.border,
        "text": theme.text,
        "muted": theme.muted,
        "accent": theme.accent,
        "accent_text": theme.accent_text,
        "accent_soft": theme.accent_soft,
        "success": theme.success,
        "danger": theme.danger,
        "wall": theme.wall,
        "open_cell": theme.open_cell,
        "visited": theme.visited,
        "path": theme.path,
        "grid": theme.grid,
        "button": theme.surface_alt,
        "button_active": theme.accent,
        "gold": theme.path,
        "dark_text": theme.wall,
        "shadow": theme.wall,
    }


def draw_menu(
    screen: PixelCanvas,
    theme: Theme,
    menu_items: Sequence[str],
    menu_index: int,
    backdrop_maze: Sequence[Sequence[object]],
) -> None:
    colors = palette(theme)
    screen.fill(colors["background"])
    draw_maze_backdrop(screen, colors, backdrop_maze)
    screen.text((160, 13), "MAZE LAB", 13, colors["text"], "center", shadow=colors["wall"])
    screen.text((160, 31), "COMP3220 / SEARCH ARCADE", 4, colors["muted"], "center")

    labels = ("START", "COMPARE", "OPTIONS", "HOW TO PLAY", "EXIT")
    for index, label in enumerate(labels):
        y = 52 + index * 25
        screen.button(
            menu_items[index],
            (96, y, 224, y + 18),
            label,
            colors["surface_alt"],
            colors["text"],
            selected=index == menu_index,
            font_size=5,
        )
    screen.text((160, 199), "UP / DOWN MOVE   ENTER SELECT", 3, colors["muted"], "center")


def draw_solver_select(
    screen: PixelCanvas,
    theme: Theme,
    selected_solver: str,
    maze: Sequence[Sequence[object]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> None:
    colors = palette(theme)
    screen.fill(colors["background"])
    draw_header(screen, colors, "SELECT MODE", "CHOOSE A STRATEGY, THEN START THE RUN")

    screen.text((13, 52), "SEARCH STRATEGIES", 4, colors["muted"])
    for index, name in enumerate(SOLVERS):
        details = ALGORITHM_DETAILS[name]
        top = 60 + index * 40
        selected = name == selected_solver
        row = (13, top, 216, top + 34)
        screen.panel(
            row,
            colors["surface_alt"] if selected else colors["surface"],
            colors["path"] if selected else colors["border"],
            selected,
        )
        screen.target(f"select:solver:{name}", row)
        screen.text((19, top + 6), f"0{index + 1}", 3, colors["muted"])
        screen.text((19, top + 17), details["short_label"], 8, colors["text"])
        screen.text((53, top + 7), details["label"].upper(), 4, colors["text"])
        screen.text((53, top + 17), details["summary"], 3, colors["muted"], max_width=116)
        action_box = (177, top + 8, 211, top + 25)
        active = selected or screen.hovered_key == f"select:solver:{name}"
        screen.panel(
            action_box,
            colors["path"] if selected else colors["surface_alt"],
            colors["path"] if active else colors["border"],
            active,
        )
        screen.text_center(
            action_box,
            "SELECTED" if selected else "SELECT",
            3,
            colors["wall"] if selected else colors["text"],
        )

    preview = (224, 60, 308, 174)
    screen.panel(preview, colors["surface"], colors["border"])
    screen.text((230, 65), "MODE PREVIEW", 4, colors["muted"])
    details = ALGORITHM_DETAILS[selected_solver]
    screen.text((230, 75), details["summary"], 4, colors["text"], max_width=74)
    preview_maze = maze or BENCHMARK_MAZE
    preview_start = start if maze else BENCHMARK_START
    preview_goal = goal if maze else BENCHMARK_GOAL
    screen.maze(
        preview_maze,
        preview_start,
        preview_goal,
        (230, 97, 303, 149),
        path=preview_path(preview_maze, preview_start, preview_goal),
        **maze_colors(colors),
    )
    # keep the preview and card stack on one vertical rhythm
    screen.text((230, 155), "YELLOW ROUTE SHOWS THE RESULT", 3, colors["muted"], max_width=70)
    screen.text((230, 162), "THIS SCREEN WILL REVEAL", 3, colors["muted"], max_width=70)

    screen.button("select:start", (12, 195, 157, 205), "START RUN", colors["accent"], colors["accent_text"], font_size=4)
    screen.button("select:settings", (163, 195, 308, 205), "OPEN SETTINGS", colors["surface_alt"], colors["text"], font_size=4)


def draw_settings(
    screen: PixelCanvas,
    theme: Theme,
    preset_name: str,
    pace_name: str,
    theme_key: str,
    show_trace: bool,
) -> None:
    colors = palette(theme)
    screen.fill(colors["background"])
    draw_header(screen, colors, "OPTIONS", "CHOOSE THE MAZE, PACE, PALETTE, AND SEARCH DETAIL")

    screen.text((13, 52), "MAZE LAYOUT", 4, colors["muted"])
    for index, (key, details) in enumerate(MAZE_PRESETS.items()):
        top = 60 + index * 40
        selected = key == preset_name
        row = (13, top, 216, top + 34)
        screen.panel(
            row,
            colors["surface_alt"] if selected else colors["surface"],
            colors["path"] if selected else colors["border"],
            selected,
        )
        screen.target(f"settings:preset:{key}", row)
        screen.text((19, top + 6), f"0{index + 1}", 3, colors["muted"])
        screen.text((53, top + 7), details["label"].upper(), 4, colors["text"])
        screen.text((53, top + 18), details["description"], 3, colors["muted"], max_width=116)

    style_panel = (224, 60, 308, 174)
    screen.panel(style_panel, colors["surface"], colors["border"])
    screen.text((230, 65), "RUN STYLE", 4, colors["text"])
    screen.text((230, 75), "TUNE THE SEARCH", 3, colors["muted"])
    options = tuple((key, value["label"]) for key, value in PACE_OPTIONS.items())
    draw_choice_list(screen, colors, "settings:pace:", options, pace_name, (230, 84, 302, 130), 15)
    screen.text((230, 137), "PALETTE", 3, colors["muted"])
    for index, key in enumerate(THEMES):
        left = 230 + index * 24
        chip = (left, 143, left + 22, 155)
        selected = key == theme_key
        screen.panel(
            chip,
            colors["accent"] if selected else colors["surface_alt"],
            colors["path"] if selected else colors["border"],
            selected,
        )
        screen.target(f"settings:theme:{key}", chip)
        palette_label = {"canopy": "CAN", "moon": "MOON", "ember": "EMB"}[key]
        screen.text_center(chip, palette_label, 2, colors["wall"] if selected else colors["text"])
    screen.button(
        "settings:trace",
        (230, 160, 302, 171),
        f"TRAIL {'ON' if show_trace else 'OFF'}",
        colors["surface_alt"],
        colors["text"],
        font_size=3,
    )


def draw_help(screen: PixelCanvas, theme: Theme) -> None:
    colors = palette(theme)
    screen.fill(colors["background"])
    draw_header(screen, colors, "HOW TO PLAY", "THREE SEARCH IDEAS, ONE MAZE, ONE ROUTE")
    for index, name in enumerate(SOLVERS):
        details = ALGORITHM_DETAILS[name]
        left = 12 + index * 101
        right = left + 94
        card = (left, 52, right, 163)
        screen.panel(card, colors["surface"], colors["border"])
        screen.text((left + 8, 60), f"0{index + 1}", 3, colors["muted"])
        screen.text((left + 8, 72), details["short_label"], 8, colors["text"])
        screen.text((left + 8, 88), details["label"].upper(), 3, colors["text"])
        screen.text((left + 8, 101), details["summary"], 4, colors["muted"], max_width=78)

    guide = (12, 171, 308, 199)
    screen.panel(guide, colors["surface"], colors["border"])
    screen.text((20, 178), "CONTROLS", 4, colors["text"])
    screen.text((20, 188), "SPACE PAUSE / RESUME    ESC MAIN MENU    ENTER CONFIRM", 3, colors["muted"])
    screen.text((303, 181), "RUN THE SAME MAZE WITH A DIFFERENT SEARCH IDEA", 3, colors["accent"], "right", max_width=112)


def draw_run(screen: PixelCanvas, theme: Theme, state: RunScreenState) -> None:
    colors = palette(theme)
    screen.fill(colors["background"])
    screen.button("run:menu", (8, 8, 47, 18), "MENU", colors["surface_alt"], colors["text"], compact=True, font_size=3)
    current_name = state.algorithm_queue[state.algorithm_index] if state.algorithm_queue else state.selected_solver
    title = "COMPARE" if state.active_mode == "all" else ALGORITHM_DETAILS[current_name]["short_label"].upper()
    screen.text((59, 9), title, 7, colors["text"], shadow=colors["wall"])
    screen.text((59, 21), MAZE_PRESETS[state.preset_name]["label"].upper(), 3, colors["muted"])
    screen.text((310, 11), f"RUN {state.algorithm_index + 1}/{len(state.algorithm_queue)}", 3, colors["muted"], "right")

    map_panel = (8, 32, 220, 202)
    side_panel = (225, 32, 312, 202)
    screen.panel(map_panel, colors["surface"], colors["border"])
    screen.panel(side_panel, colors["surface"], colors["border"])
    screen.text((15, 39), "ROUTE MAP", 4, colors["text"])
    screen.text((211, 39), "S START  G GOAL", 3, colors["muted"], "right")
    screen.maze(
        state.maze or BENCHMARK_MAZE,
        state.start,
        state.goal,
        (14, 50, 214, 193),
        visited_cells(state.visited_order, state.visit_index),
        path_cells(state.path, state.path_index),
        **maze_colors(colors),
    )

    details = ALGORITHM_DETAILS[current_name]
    screen.text((232, 41), details["label"].upper(), 4, colors["text"])
    screen.text((232, 50), details["summary"], 3, colors["muted"], max_width=72)
    screen.panel((231, 72, 306, 119), colors["surface_alt"], colors["border"])
    screen.text((236, 78), "RUN STATUS", 3, colors["muted"])
    screen.text((236, 88), state.status_text.upper(), 4, colors["text"], max_width=62)
    screen.rect((236, 105, 301, 109), colors["wall"], colors["grid"])
    screen.rect((237, 106, 237 + int(63 * state.progress / 100), 108), colors["accent"])

    draw_stat(screen, colors, "EXPANDED", state.expanded_text, (232, 124))
    draw_stat(screen, colors, "ROUTE", state.route_text, (271, 124))
    draw_stat(screen, colors, "MOVES", state.cost_text, (232, 143))
    draw_stat(screen, colors, "PACE", PACE_OPTIONS[state.pace_name]["label"], (271, 143))

    pause_label = "RESUME" if state.paused else "PAUSE"
    screen.button("run:pause", (231, 163, 306, 173), pause_label, colors["accent"], colors["accent_text"], font_size=3)
    if state.algorithm_index + 1 < len(state.algorithm_queue):
        screen.button("run:next", (231, 176, 306, 186), "NEXT SOLVER", colors["surface_alt"], colors["text"], font_size=3)
    else:
        screen.button("run:menu", (231, 176, 306, 186), "MAIN MENU", colors["surface_alt"], colors["text"], font_size=3)
    screen.button("run:restart", (231, 189, 268, 199), "RESTART", colors["surface_alt"], colors["muted"], font_size=3)
    screen.button("run:new", (270, 189, 306, 199), "NEW", colors["surface_alt"], colors["muted"], font_size=3)


def draw_header(screen: PixelCanvas, colors: dict[str, str], title: str, subtitle: str) -> None:
    screen.button("back", (12, 11, 47, 20), "MAIN MENU", colors["background"], colors["accent"], compact=True, font_size=3)
    screen.text((13, 28), title, 11, colors["text"], shadow=colors["wall"])
    screen.text((13, 43), subtitle, 4, colors["muted"], max_width=292)


def draw_choice_list(
    screen: PixelCanvas,
    colors: dict[str, str],
    prefix: str,
    options: Sequence[tuple[str, str]],
    selected: str,
    bounds: tuple[int, int, int, int],
    row_height: int,
) -> None:
    left, top, right, bottom = bounds
    for index, (value, label) in enumerate(options):
        row_top = top + index * row_height
        if row_top + row_height > bottom + 1:
            break
        key = prefix + value
        is_selected = value == selected
        row = (left, row_top, right, row_top + row_height - 2)
        screen.panel(
            row,
            colors["surface_alt"] if is_selected else colors["surface"],
            colors["path"] if is_selected else colors["border"],
            is_selected,
        )
        screen.target(key, row)
        screen.text((left + 6, row_top + 5), label.upper(), 3, colors["wall"] if is_selected else colors["text"])


def draw_stat(screen: PixelCanvas, colors: dict[str, str], label: str, value: str, position: tuple[int, int]) -> None:
    screen.text(position, label, 2, colors["muted"])
    screen.text((position[0], position[1] + 7), str(value), 4, colors["text"])


def draw_maze_backdrop(
    screen: PixelCanvas,
    colors: dict[str, str],
    backdrop_maze: Sequence[Sequence[object]],
) -> None:
    cell_size = 8
    maze_width = len(backdrop_maze[0]) * cell_size
    maze_height = len(backdrop_maze) * cell_size
    origin_x = (320 - maze_width) // 2
    origin_y = (210 - maze_height) // 2
    # keep the menu world visible behind the controls
    for row, maze_line in enumerate(backdrop_maze):
        for col, maze_value in enumerate(maze_line):
            left = origin_x + col * cell_size
            top = origin_y + row * cell_size
            color = colors["accent_soft"] if maze_value == "1" else colors["background"]
            screen.rect((left, top, left + cell_size, top + cell_size), color)


def preview_path(
    maze: Sequence[Sequence[object]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> set[tuple[int, int]]:
    path, _, _ = bfs(maze, start, goal)
    return set(path)


def visited_cells(visited_order: Sequence[tuple[int, int]], visit_index: int) -> set[tuple[int, int]]:
    return set(visited_order[:visit_index])


def path_cells(path: Sequence[tuple[int, int]], path_index: int) -> set[tuple[int, int]]:
    return set(path[:path_index])


def maze_colors(colors: dict[str, str]) -> dict[str, str]:
    return {
        "wall": colors["wall"],
        "open_cell": colors["open_cell"],
        "visited_color": colors["visited"],
        "path_color": colors["path"],
        "grid": colors["grid"],
        "start_color": colors["success"],
        "goal_color": colors["danger"],
        "marker": colors["background"],
    }
