"""Locked domain and protocol constants (proposal § decisions)."""

from __future__ import annotations

# Western Pacific crop — Hong Kong / SE Asia (field / spatial crop)
LON_MIN, LON_MAX = 100.0, 135.0
LAT_MIN, LAT_MAX = 5.0, 40.0

# Lead times (hours)
CORE_LEAD_H = (0, 72)
SECONDARY_NOWCAST_H = (0, 6)

# HK black-rainstorm threshold (mm/h)
BLACK_RAINSTORM_MM_H = 70.0

# Dual eval protocol (locked 20 Nov 2026)
TC_PROTOCOL = "tcbench_v3"  # arXiv:2601.23268v3 — TC track + intensity
TC_EVAL_YEAR = 2023
FIELD_PROTOCOL = "wb2_style"  # field extremes / FSS / twCRPS
FIELD_EVAL_YEAR = 2020
BLACK_RAIN_PROTOCOL = "hko_imerg"

# TCBench pin (preprint under revision — cite version)
TCB_ARXIV = "2601.23268v3"
TCB_REPO = "https://github.com/tcbench/TCBench"
TCB_HF_DOI = "10.57967/hf/8882"
TCB_CODE_DOI = "10.5281/zenodo.23801372"

# Table S2 WP SIDs (verified from arXiv HTML v3) — intensity tiers NOT locked here
TCB_WP_SIDS_2023: tuple[str, ...] = (
    "2023101N14127",
    "2023108N03160",
    "2023138N05151",
    "2023156N12135",
    "2023194N16123",
    "2023201N13134",
    "2023207N09141",
    "2023218N25145",
    "2023234N18128",
    "2023234N19154",
    "2023239N18144",
    "2023241N10158",
    "2023247N20130",
    "2023266N16116",
    "2023271N14144",
    "2023279N08157",
    "2023289N15111",
    "2023314N05149",
    "2023349N04141",
)

# Anti-leak: years excluded from LoRA / FT training when dual protocol is used
LORA_HELD_OUT_YEARS = (2020, 2023)

# Attribution factorial (required before claiming LoRA wins)
CONTROLS = (
    "frozen_aurora",
    "frozen_aurora_gomez_linear",
    "lora_or_ft",
    "lora_or_ft_gomez",
)


def in_domain(lon: float, lat: float) -> bool:
    return LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX
