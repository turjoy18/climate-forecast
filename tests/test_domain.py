from tailfirst.domain import (
    BLACK_RAINSTORM_MM_H,
    CONTROLS,
    FIELD_EVAL_YEAR,
    LORA_HELD_OUT_YEARS,
    TC_EVAL_YEAR,
    TCB_WP_SIDS_2023,
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


def test_dual_protocol_years() -> None:
    assert TC_EVAL_YEAR == 2023
    assert FIELD_EVAL_YEAR == 2020
    assert LORA_HELD_OUT_YEARS == (2020, 2023)


def test_tcbench_wp_sids_table_s2() -> None:
    assert len(TCB_WP_SIDS_2023) == 19
    assert len(set(TCB_WP_SIDS_2023)) == 19
    assert "2023194N16123" in TCB_WP_SIDS_2023
