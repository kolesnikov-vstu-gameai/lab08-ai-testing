"""Бот-плеер: ходит по сетке уровня к финишу (жадно по BFS-дистанции), собирает метрики."""

import random
from dataclasses import dataclass, field

import numpy as np


@dataclass
class BotMetrics:
    steps: int = 0
    reached_goal: bool = False
    stuck_events: int = 0
    visited: set = field(default_factory=set)


def run_bot(grid: np.ndarray, dist: np.ndarray, start: tuple, goal: tuple,
            max_steps=2000, epsilon=0.1, seed=0) -> BotMetrics:
    rng = random.Random(seed)
    pos, m = start, BotMetrics()
    for _ in range(max_steps):
        m.steps += 1
        m.visited.add(pos)
        if pos == goal:
            m.reached_goal = True
            break
        y, x = pos
        moves = [(y + dy, x + dx) for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))
                 if 0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1] and dist[y + dy, x + dx] >= 0]
        if not moves:
            m.stuck_events += 1
            break
        # dist считается ОТ финиша: идём в клетку с меньшим значением; иногда случайно (epsilon)
        nxt = rng.choice(moves) if rng.random() < epsilon else min(moves, key=lambda p: dist[p])
        if dist[nxt] >= dist[pos] and rng.random() >= epsilon:
            m.stuck_events += 1
        pos = nxt
    return m
