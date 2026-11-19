"""Locked domain and protocol constants (proposal § decisions)."""

from __future__ import annotations

# Western Pacific crop — Hong Kong / SE Asia
LON_MIN, LON_MAX = 100.0, 135.0
LAT_MIN, LAT_MAX = 5.0, 40.0

# Lead times (hours)
CORE_LEAD_H = (0, 72)
SECONDARY_NOWCAST_H = (0, 6)

# HK black-rainstorm threshold (mm/h)
BLACK_RAINSTORM_MM_H = 70.0

# Attribution factorial (required before claiming LoRA wins)
CONTROLS = (
    "frozen_aurora",
    "frozen_aurora_gomez_linear",
    "lora_or_ft",
    "lora_or_ft_gomez",
)


def in_domain(lon: float, lat: float) -> bool:
    return LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX
