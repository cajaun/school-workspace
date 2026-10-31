"""visual themes and interaction settings for the maze app"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str
    background: str
    surface: str
    surface_alt: str
    border: str
    text: str
    muted: str
    accent: str
    accent_text: str
    accent_soft: str
    success: str
    danger: str
    wall: str
    open_cell: str
    visited: str
    path: str
    grid: str


THEMES = {
    "canopy": Theme(
        name="canopy",
        background="#173e42",
        surface="#246256",
        surface_alt="#337868",
        border="#6da789",
        text="#f1f5c9",
        muted="#9bc89e",
        accent="#a9dc8e",
        accent_text="#174c4b",
        accent_soft="#3f8b71",
        success="#a9dc8e",
        danger="#ef9f72",
        wall="#102f38",
        open_cell="#bfe5a1",
        visited="#68aa83",
        path="#f3cc4b",
        grid="#3c806f",
    ),
    "moon": Theme(
        name="moon",
        background="#202b4c",
        surface="#29385d",
        surface_alt="#354a73",
        border="#5d78a4",
        text="#f8f0d9",
        muted="#9cafce",
        accent="#b8d4ef",
        accent_text="#304c76",
        accent_soft="#354a73",
        success="#b8d4ef",
        danger="#e9a99c",
        wall="#15213c",
        open_cell="#c9dced",
        visited="#91b7d0",
        path="#ffe6a3",
        grid="#7898bb",
    ),
    "ember": Theme(
        name="ember",
        background="#512f38",
        surface="#633943",
        surface_alt="#7a4a4f",
        border="#a06b61",
        text="#fff0d3",
        muted="#d59c8c",
        accent="#f3c08c",
        accent_text="#6b3b3b",
        accent_soft="#7a4a4f",
        success="#f3c08c",
        danger="#f2a296",
        wall="#3b252e",
        open_cell="#f4d4af",
        visited="#d79d8c",
        path="#fff09e",
        grid="#c48679",
    ),
}


PACE_OPTIONS = {
    "slow": {"label": "slow", "delay": 110, "description": "watch every decision"},
    "steady": {"label": "steady", "delay": 45, "description": "balanced pace"},
    "turbo": {"label": "turbo", "delay": 12, "description": "see the result fast"},
}


ALGORITHM_DETAILS = {
    "bfs": {
        "label": "Breadth first",
        "short_label": "bfs",
        "summary": "expands evenly and guarantees the shortest route",
    },
    "dfs": {
        "label": "Depth first",
        "short_label": "dfs",
        "summary": "dives deep before backtracking to try another route",
    },
    "astar": {
        "label": "A star",
        "short_label": "a*",
        "summary": "uses distance to the goal to guide its search",
    },
}


MAZE_PRESETS = {
    "benchmark": {
        "label": "Assignment maze",
        "description": "the fixed maze used for your benchmark results",
    },
    "training": {
        "label": "Training grounds",
        "description": "a compact generated maze for quick experiments",
        "rows": 15,
        "cols": 23,
    },
    "labyrinth": {
        "label": "The labyrinth",
        "description": "a larger generated maze with more turns to explore",
        "rows": 21,
        "cols": 31,
    },
}
