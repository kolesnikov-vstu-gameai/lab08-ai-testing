"""Performance-тесты с явными порогами (подберите под свою машину, зафиксируйте в отчёте)."""

import time

import pytest

pytest.importorskip("aiunder.bsp")
from aiunder import bsp  # noqa: E402

GEN_BUDGET_MS = 50


@pytest.mark.timeout(10)
def test_generation_budget():
    times = []
    for s in range(20):
        t = time.perf_counter()
        bsp.generate(seed=s)
        times.append((time.perf_counter() - t) * 1000)
    p95 = sorted(times)[int(0.95 * len(times)) - 1]
    assert p95 < GEN_BUDGET_MS, f"p95 = {p95:.1f} ms > {GEN_BUDGET_MS} ms"
