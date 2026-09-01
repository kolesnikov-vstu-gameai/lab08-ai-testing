import numpy as np

from bot.player_bot import run_bot


def test_bot_reaches_goal_on_corridor():
    grid = np.zeros((3, 10), dtype=np.int8)
    dist = np.tile(np.arange(9, -1, -1), (3, 1))  # расстояние до цели (2, 9) по x
    m = run_bot(grid, dist, start=(1, 0), goal=(1, 9), epsilon=0.0)
    assert m.reached_goal and m.steps <= 12
