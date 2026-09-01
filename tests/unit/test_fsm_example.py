"""Пример unit-тестов. Замените на тесты своих FSM/BT/perception (минимум 10)."""

import pytest

pytest.importorskip("aiunder.fsm", reason="скопируйте fsm.py из ЛР 1 в src/aiunder/")
from aiunder.fsm import GuardFSM, State  # noqa: E402


@pytest.mark.parametrize("trigger,expected", [("see_player", State.ALERT), ("hear_noise", State.ALERT)])
def test_patrol_transitions(trigger, expected):
    g = GuardFSM()
    assert g.fire(trigger) and g.state == expected


def test_invalid_trigger_ignored():
    g = GuardFSM()
    assert not g.fire("teleport") and g.state == State.PATROL
