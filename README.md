# Tail-First — Extremes-Weighted Aurora Adaptation for W Pacific TCs

**Tail-First** fine-tunes Aurora (LoRA / Aurora-Small) under extremes-weighted + twCRPS losses and a Gomez-style intensity head so the model is scored where mean training fails: **tropical-cyclone intensity** and heavy precipitation over the Western Pacific (Hong Kong / SE Asia).

| Doc | Purpose |
|-----|---------|
| [`RESEARCH PROPOSAL_CLIMATE.md`](RESEARCH%20PROPOSAL_CLIMATE.md) | Locked proposal (form sections a–e) |
| [`Extreme Weather AI Research Proposal.html`](Extreme%20Weather%20AI%20Research%20Proposal.html) | Interactive programme + decision log |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Branch / PR / claim discipline |
| Issues | Phase 0–3 work queue |

> Forecast the **tail**, not the mean. Track is largely solved; intensity is the gap.

**Phase 0 is open.** No LoRA until frozen Aurora produces a TCBench-schema track file and the linear Gomez floor exists. See issues [#1](https://github.com/turjoy18/climate-forecast/issues/1)–[#3](https://github.com/turjoy18/climate-forecast/issues/3).

## Tracks

| Track | Role | Status |
|-------|------|--------|
| **Proposal** | Claims, dual protocol, kill conditions | **Locked** 20 Nov 2026 |
| **Phase 0 harness** | TCBench Aurora tracks + Gomez floor + WB2-style fields | **Active** |
| **WP1 LoRA / FT** | Extremes-weighted adaptation (RQ1) | Blocked on Phase 0 |
| **WP2 intensity head** | IBTrACS / TCBench postproc (RQ2) | Blocked on Phase 0 |
| **WP3 calibration** | LoRA-ensemble + REV (RQ3) | Later |
| **Stretch** | CorrDiff / compound / tensor-network control | Optional — not core |

**Hardware:** 1 × RTX PRO 6000 Blackwell (~92 GB usable). Budget target ~5–20 GPU-days for the core result — not global pretraining.

## Dual eval protocol (locked)

| Claim | Protocol | Year |
|-------|----------|------|
| TC track + intensity | [TCBench](https://github.com/tcbench/TCBench) **v3** (arXiv:2601.23268v3), WP SID subset (Table S2, **n = 19**) | **2023** |
| Field extremes (FSS / twCRPS / CSI) | WeatherBench 2–style | **2020** |
| Black-rainstorm (>70 mm/h) | HKO gauges + IMERG | event set |

**Anti-leak:** exclude **2020 and 2023** from LoRA/FT training, or keep the 2020 field eval **frozen-base only**.  
**Small WP sample:** bootstrap CIs on intensity; do not overclaim from n ≈ 19. Intensity-tier counts within those SIDs are **not** locked until IBTrACS classification.  
**Pin:** HF doi:[10.57967/hf/8882](https://doi.org/10.57967/hf/8882); code doi:[10.5281/zenodo.23801372](https://doi.org/10.5281/zenodo.23801372). Do not use `msgomez06/TCBench_Alpha`.

## What this claims / does not claim

**Can claim (when gates pass)**

- Extremes-weighted LoRA / Aurora-Small FT improves tail metrics vs frozen Aurora **and** frozen+Gomez at matched body metrics (Wessel body–tail discipline).
- A Gomez-style intensity head on Aurora fields (transfer from Pangu/FourCastNet) moves intensity toward HRES / TCBench baselines on held-out 2023 WP SIDs.
- Evaluation against TCBench schema + WB2-style fields + HKO/IMERG, with significance / bootstrap.

**Cannot claim**

- A new global weather foundation model, or a diffusion model trained from scratch.
- Quantum advantage (classical-only; quantum is out of scope).
- Beating HRES on mean RMSE alone as an extremes result.
- Product / React Native delivery — notebooks and figures only.

**Attribution factorial (required):** `frozen_aurora` → `frozen_aurora_gomez_linear` → `lora_or_ft` → `lora_or_ft_gomez`.

## Phase 0 order

1. Pin `tcbench/TCBench` → frozen Aurora → TempestExtremes → **`2023_AURORA.csv`** → score Table S2 WP SIDs  
2. Linear Gomez head on **frozen** Aurora (cheap floor)  
3. WB2-style 2020 field harness (frozen-only until training window locked)  
4. Only then LoRA / FT  

## Quick start

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"

ruff check src tests
ruff format --check src tests
pytest -q
```

No frozen scorecard artifacts yet — Phase 0 delivers those.

## Layout

| Path | Purpose |
|------|---------|
| `src/tailfirst/` | Package: domain/protocol constants (locked) |
| `tests/` | Unit tests (CI) |
| `RESEARCH PROPOSAL_CLIMATE.md` | Proposal softcopy |
| `Extreme Weather AI Research Proposal.html` | Interactive proposal |
| `.github/` | CI, PR + issue templates |

## References

- Bodnar et al. 2025. *Aurora.* Nature. doi:10.1038/s41586-025-09005-y  
- Gomez et al. 2026. *TCBench.* arXiv:2601.23268v3  
- Gomez et al. 2026. *Global TC intensity via neural weather models.* AIES. doi:10.1175/AIES-D-25-0073.1  
- Zhang et al. 2026. *Physics-based models outperform AI on record-breaking extremes.* Science Advances. doi:10.1126/sciadv.aec1433  
- Rasp et al. 2024. *WeatherBench 2.* JAMES  
- Wessel et al. 2025. *twCRPS training for extremes.* MWR  

## License

MIT
