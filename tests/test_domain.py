from tailfirst.domain import (
    BLACK_RAINSTORM_MM_H,
    CONTROLS,
    in_domain,
)


def test_hong_kong_in_domain() -> None:
    assert in_domain(114.17, 22.32)


def test_outside_domain() -> None:
    assert not in_domain(0.0, 51.5)


def test_black_rainstorm_threshold() -> None:
    assert BLACK_RAINSTORM_MM_H == 70.0


def test_attribution_controls_locked() -> None:
    assert "frozen_aurora_gomez_linear" in CONTROLS
    assert len(CONTROLS) == 4
