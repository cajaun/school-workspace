"""render the supplied pixel font consistently across tkinter surfaces"""

from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

try:
    from PIL import Image, ImageDraw, ImageFont, ImageTk
except ImportError:
    Image = ImageDraw = ImageFont = ImageTk = None


FONT_PATH = Path(__file__).resolve().parent / "assets" / "PressStart2P.ttf"


@dataclass
class PixelTarget:
    key: str
    bounds: tuple[int, int, int, int]


class PixelCanvas(tk.Frame):
    """render the app on a fixed high-resolution game surface"""

    WIDTH = 1280
    HEIGHT = 840
    DESIGN_SCALE = 4

    def __init__(
        self,
        parent: tk.Widget,
        background: str,
        on_action: Callable[[str], None],
        palette: dict[str, str] | None = None,
    ) -> None:
        if Image is None:
            raise RuntimeError("Pillow is required for the pixel interface")
        super().__init__(parent, bg=background)
        self.canvas = tk.Canvas(
            self,
            width=1280,
            height=840,
            bg=background,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)
        self.on_action = on_action
        self.palette = palette or {}
        self.drawer: Callable[[PixelCanvas], None] | None = None
        self.surface = None
        self.draw = None
        self.image = None
        self.targets: list[PixelTarget] = []
        self.hovered_key: str | None = None
        self._display_scale = 1.0
        self._display_origin = (0.0, 0.0)
        self._font_cache: dict[int, object] = {}
        self.canvas.bind("<Configure>", self._on_resize)
        self.canvas.bind("<Motion>", self._on_motion)
        self.canvas.bind("<Leave>", self._on_leave)
        self.canvas.bind("<Button-1>", self._on_click)

    def render(self, drawer: Callable[["PixelCanvas"], None] | None = None) -> None:
        if drawer is not None:
            self.drawer = drawer
        if self.drawer is None:
            return
        self.surface = Image.new("RGB", (self.WIDTH, self.HEIGHT), "#000000")
        self.draw = ImageDraw.Draw(self.surface)
        self.targets = []
        self.drawer(self)
        self._present()

    def fill(self, color: str) -> None:
        self.draw.rectangle((0, 0, self.WIDTH, self.HEIGHT), fill=color)

    def rect(self, bounds: tuple[int, int, int, int], fill: str, outline: str | None = None, width: int = 1) -> None:
        self.draw.rectangle(
            self._scale_bounds(bounds),
            fill=fill,
            outline=outline,
            width=max(1, width * self.DESIGN_SCALE),
        )

    def line(self, points: Sequence[tuple[int, int]], fill: str, width: int = 1) -> None:
        self.draw.line(self._scale_points(points), fill=fill, width=max(1, width * self.DESIGN_SCALE))

    def panel(
        self,
        bounds: tuple[int, int, int, int],
        fill: str,
        border: str,
        selected: bool = False,
        shadow: str | None = None,
    ) -> None:
        x1, y1, x2, y2 = bounds
        if shadow is not None:
            self.rect((x1 + 2, y1 + 2, x2 + 2, y2 + 2), shadow)
        self.rect(bounds, fill, border, 1)
        if selected:
            self.rect((x1 - 1, y1 - 1, x2 + 1, y2 + 1), fill, border, 2)

    def button(
        self,
        key: str,
        bounds: tuple[int, int, int, int],
        label: str,
        normal: str,
        foreground: str,
        selected: bool = False,
        compact: bool = False,
        font_size: int | None = None,
    ) -> None:
        active = selected or self.hovered_key == key
        fill = self._colors("button_active", normal) if active else normal
        border = self._colors("gold", foreground) if active else self._colors("border", foreground)
        self.panel(bounds, fill, border, active, self._colors("shadow", "#000000"))
        size = font_size or (4 if compact else 5)
        self.text_center(bounds, label, size, foreground if not active else self._colors("dark_text", foreground), shadow=None)
        self.targets.append(PixelTarget(key, self._scale_bounds(bounds)))

    def target(self, key: str, bounds: tuple[int, int, int, int]) -> None:
        self.targets.append(PixelTarget(key, self._scale_bounds(bounds)))

    def text(
        self,
        position: tuple[int, int],
        value: str,
        size: int,
        color: str,
        align: str = "left",
        max_width: int | None = None,
        shadow: str | None = None,
        spacing: int = 1,
    ) -> None:
        scaled_max_width = max_width * self.DESIGN_SCALE if max_width is not None else None
        lines = self._wrap(value, size, scaled_max_width)
        line_height = max(1, self._font(size).getbbox("Ag")[3] - self._font(size).getbbox("Ag")[1])
        x, y = position
        x *= self.DESIGN_SCALE
        y *= self.DESIGN_SCALE
        for index, line in enumerate(lines):
            bbox = self.draw.textbbox((0, 0), line, font=self._font(size))
            line_width = bbox[2] - bbox[0]
            draw_x = x if align == "left" else x - line_width / 2 if align == "center" else x - line_width
            draw_y = y + index * (line_height + spacing * self.DESIGN_SCALE)
            if shadow is not None:
                self.draw.text((draw_x + 1, draw_y + 1), line, font=self._font(size), fill=shadow)
            self.draw.text((draw_x, draw_y), line, font=self._font(size), fill=color)

    def text_center(
        self,
        bounds: tuple[int, int, int, int],
        value: str,
        size: int,
        color: str,
        shadow: str | None = None,
    ) -> None:
        x1, y1, x2, y2 = bounds
        line_height = (self._font(size).getbbox("Ag")[3] - self._font(size).getbbox("Ag")[1]) / self.DESIGN_SCALE
        self.text(((x1 + x2) // 2, int((y1 + y2 - line_height) / 2)), value, size, color, "center", shadow=shadow)

    def maze(
        self,
        maze: Sequence[Sequence[object]],
        start: tuple[int, int],
        goal: tuple[int, int],
        bounds: tuple[int, int, int, int],
        visited: set[tuple[int, int]] | None = None,
        path: set[tuple[int, int]] | None = None,
        wall: str = "#102f38",
        open_cell: str = "#bfe5a1",
        visited_color: str = "#68aa83",
        path_color: str = "#f3cc4b",
        grid: str = "#3c806f",
        start_color: str = "#a9dc8e",
        goal_color: str = "#ef9f72",
        marker: str = "#173e42",
    ) -> None:
        visited = visited or set()
        path = path or set()
        x1, y1, x2, y2 = bounds
        rows = len(maze)
        cols = len(maze[0])
        cell_size = max(1, min((x2 - x1) // cols, (y2 - y1) // rows))
        maze_width = cols * cell_size
        maze_height = rows * cell_size
        origin_x = x1 + ((x2 - x1) - maze_width) // 2
        origin_y = y1 + ((y2 - y1) - maze_height) // 2
        for row in range(rows):
            for col in range(cols):
                position = (row, col)
                left = origin_x + col * cell_size
                top = origin_y + row * cell_size
                color = wall if str(maze[row][col]) == "1" else open_cell
                if position in visited:
                    color = visited_color
                if position in path:
                    color = path_color
                if position == start:
                    color = start_color
                elif position == goal:
                    color = goal_color
                self.rect((left, top, left + cell_size, top + cell_size), color, grid, 1)
        marker_size = max(3, cell_size // 2)
        self.text_center((origin_x + start[1] * cell_size, origin_y + start[0] * cell_size, origin_x + (start[1] + 1) * cell_size, origin_y + (start[0] + 1) * cell_size), "S", marker_size, marker)
        self.text_center((origin_x + goal[1] * cell_size, origin_y + goal[0] * cell_size, origin_x + (goal[1] + 1) * cell_size, origin_y + (goal[0] + 1) * cell_size), "G", marker_size, marker)

    def _colors(self, _name: str, fallback: str) -> str:
        return self.palette.get(_name, fallback)

    def _font(self, size: int):
        if size not in self._font_cache:
            self._font_cache[size] = ImageFont.truetype(str(FONT_PATH), max(1, size * self.DESIGN_SCALE))
        return self._font_cache[size]

    def _wrap(self, value: str, size: int, max_width: int | None) -> list[str]:
        if max_width is None:
            return value.splitlines() or [""]
        lines: list[str] = []
        for paragraph in value.splitlines() or [""]:
            words = paragraph.split()
            current = ""
            for word in words:
                candidate = word if not current else f"{current} {word}"
                if current and self.draw.textlength(candidate, font=self._font(size)) > max_width:
                    lines.append(current)
                    current = word
                else:
                    current = candidate
            lines.append(current)
        return lines or [""]

    def _scale_bounds(self, bounds: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(value * self.DESIGN_SCALE for value in bounds)

    def _scale_points(self, points: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
        return [(x * self.DESIGN_SCALE, y * self.DESIGN_SCALE) for x, y in points]

    def _on_resize(self, _event: tk.Event) -> None:
        if self.surface is not None:
            self._present()

    def _on_motion(self, event: tk.Event) -> None:
        point = self._to_pixel(event.x, event.y)
        hovered = next((target.key for target in self.targets if self._contains(target.bounds, point)), None)
        if hovered != self.hovered_key:
            self.hovered_key = hovered
            self.render()

    def _on_leave(self, _event: tk.Event) -> None:
        if self.hovered_key is not None:
            self.hovered_key = None
            self.render()

    def _on_click(self, event: tk.Event) -> None:
        point = self._to_pixel(event.x, event.y)
        for target in self.targets:
            if self._contains(target.bounds, point):
                self.on_action(target.key)
                return

    def _to_pixel(self, x: int, y: int) -> tuple[int, int]:
        origin_x, origin_y = self._display_origin
        if self._display_scale <= 0:
            return 0, 0
        return int((x - origin_x) / self._display_scale), int((y - origin_y) / self._display_scale)

    @staticmethod
    def _contains(bounds: tuple[int, int, int, int], point: tuple[int, int]) -> bool:
        x1, y1, x2, y2 = bounds
        return x1 <= point[0] <= x2 and y1 <= point[1] <= y2

    def _present(self) -> None:
        if self.surface is None:
            return
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        if width <= 1 or height <= 1:
            width, height = 1280, 840
        scale = min(width / self.WIDTH, height / self.HEIGHT)
        scaled_size = (max(1, int(self.WIDTH * scale)), max(1, int(self.HEIGHT * scale)))
        scaled = self.surface if scaled_size == self.surface.size else self.surface.resize(scaled_size, Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(scaled)
        self.canvas.delete("all")
        origin_x = (width - scaled_size[0]) // 2
        origin_y = (height - scaled_size[1]) // 2
        self._display_scale = scale
        self._display_origin = (origin_x, origin_y)
        self.canvas.create_image(origin_x, origin_y, image=self.image, anchor="nw")
