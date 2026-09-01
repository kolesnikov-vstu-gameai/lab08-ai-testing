"""Solvability-тест: 100 seeds генератора уровней должны быть проходимы."""

import pytest

pytest.importorskip("aiunder.bsp", reason="скопируйте bsp.py и validator.py из ЛР 7 в src/aiunder/")
from aiunder.validator import is_playable  # noqa: E402

from aiunder import bsp  # noqa: E402


@pytest.mark.parametrize("seed", range(100))
def test_level_is_playable(seed):
    assert is_playable(bsp.generate(seed=seed)), f"seed={seed} непроходим"
