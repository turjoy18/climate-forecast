# RESEARCH PROPOSAL

**Working title:** Tail-First Fine-Tuning: Extremes-Weighted LoRA Adaptation of Aurora for Western Pacific Tropical-Cyclone Intensity and Heavy Precipitation

**Status:** Decisions locked 20 Nov 2026 · TCBench dual-protocol lock (Option 1 for TC)  
**Hardware:** 1 × RTX PRO 6000 Blackwell (~92 GB usable)  
**Primary artefact:** see also `Extreme Weather AI Research Proposal.html`

---

## a) Project Title

Tail-First Fine-Tuning: Extremes-Weighted LoRA Adaptation of Aurora for Western Pacific Tropical-Cyclone Intensity and Heavy Precipitation

*(Supersedes: “Predicting Extreme Weather Events Using AI-Powered Climate Modeling”)*

---

## b) Project Aims and Objectives

### b1) Final aims and objectives

**Primary aim (novel ML method; climate as stress domain):** Show that extremes-weighted / threshold-weighted losses and IBTrACS-supervised intensity objectives, applied via LoRA (Aurora 1.3B) or full fine-tune (Aurora-Small 113M) on a cropped Western Pacific domain, recover **tail and tropical-cyclone intensity skill** that mean-trained foundation models lose — without training a new global model or a diffusion model from scratch.

**Objectives**

1. **Adapt** Aurora-Small (full FT) and/or Aurora 1.3B (LoRA) on domain `100–135°E, 5–40°N` with extremes-weighted + quantile + twCRPS losses on extreme-subsampled cases.
2. **Close the intensity gap** with IBTrACS-supervised multi-task / postprocessing heads (track is secondary; intensity is primary). Secondary arm: 0–6 h heavy precip / HK black-rainstorm (`>70 mm/h`) exceedance.
3. **Evaluate** under the **dual protocol** (below): TCBench v3 for TC track+intensity (2023 WP subset); WB2-style 2020 for field extremes; HKO/IMERG for black-rain — with anti-leak training windows and bootstrap CIs on the small WP sample.
4. **Ship** arXiv draft + code/weights + evaluation notebooks/dashboard. **No** React Native app.

### b2) Key issues and problems

- AI weather models beat HRES on mean scores but systematically fail on **record-breaking extremes** (Zhang et al., *Science Advances*, 2026, doi:10.1126/sciadv.aec1433) and **TC intensity** (reanalysis-smoothed extrema; Sahu et al., 2025; Gomez et al., *AIES*, 2026).
- MSE / mean CRPS training **attenuates peaks**; beating HRES on global RMSE is the trap, not the contribution.
- Aurora already shows strong **TC track** skill (Bodnar et al., *Nature*, 2025); intensity and thresholded heavy rain remain open for a solo fine-tuning PoW.
- Generative intensity fix (FuXi-TC, *npj Clim. Atmos. Sci.*, 2026) exists as related SOTA — we cite it; we do **not** retrain diffusion from scratch.

### b3) Specific research questions (falsifiable)

| ID | Question | Falsified if |
|----|----------|--------------|
| **RQ1** | Can extremes-weighted LoRA / Aurora-Small FT recover tail skill lost to mean training? | Tail metrics (CSI/ETS, twCRPS, record-exceedance error) do not beat frozen Aurora at matched **body** metrics (mean RMSE / unweighted CRPS), or only by destroying calibration. |
| **RQ2** | Can IBTrACS-supervised intensity objectives close the TC intensity gap without a from-scratch diffusion model? | Intensity error does not move toward HRES on held-out WNP storms at matched track error — **after** the frozen-Aurora + Gomez-head control. |
| **RQ3** | Is a LoRA-ensemble (perturbation / multi-LoRA / dropout-style) calibrated on extremes thresholds, with decision value (REV)? | Spread–skill far from 1 on extremes thresholds after CRPS/twCRPS fine-tuning + temperature scaling. *Diffusion sampling is stretch-only — not the core ensemble.* |

**Body–tail trade-off (Wessel et al., *MWR* 2025):** training on twCRPS improves extremes and can worsen the distribution body. Always report **mean/body metrics alongside tail metrics**. Mitigate with Wessel’s weighted training and/or linear pooling of body- and tail-optimised members — do not claim a win that only exists on the tail.

**Attribution controls (required):** WP1 and WP2 both attack smoothing. Pre-register the factorial:
1. frozen Aurora alone  
2. **frozen Aurora + Gomez-style head** (cheap floor; Gomez used Pangu/FourCastNet — transfer to Aurora is itself a test)  
3. LoRA / Aurora-Small FT alone  
4. LoRA / FT + Gomez head  

Without (2), a win cannot be attributed to the loss vs the head.

### Dual eval protocol (locked 20 Nov 2026 — Option 1 for TC)

| Claim | Protocol | Year | Notes |
|-------|----------|------|-------|
| TC track + intensity | **TCBench v3** (Gomez et al., arXiv:2601.23268v3) | **2023** | WP SID subset from Table S2 (**19** SIDs, verified). TempestExtremes → TCBench schema. Aurora not in baselines — produce `2023_AURORA.csv`. |
| Field extremes / FSS / twCRPS | WB2-style | **2020** | Grid scores only — not the TC protocol. |
| 0–6 h black-rain | HKO gauges + IMERG | event set | Unchanged. |

**Pin:** official repo [tcbench/TCBench](https://github.com/tcbench/TCBench); HF dataset doi:[10.57967/hf/8882](https://doi.org/10.57967/hf/8882); code doi:[10.5281/zenodo.23801372](https://doi.org/10.5281/zenodo.23801372). Preprint under revision: **non-homogenised** track scores (paper §1); basin filtering in R1 — cite **v3** explicitly. Do **not** clone `msgomez06/TCBench_Alpha`.

**Option 2** (borrow tracker only, keep 2020 as TC eval) is a temporary implementation borrow while editing — **never** the frozen TC protocol.

#### Caveat A — training-window leak
TCBench recommends train 2017–2020 / val 2021–2022 / test 2023. A 2020 field test is **in-sample** if LoRA trains through 2020. **Required:** exclude **both 2020 and 2023** from LoRA/FT training (`LORA_HELD_OUT_YEARS`), **or** restrict the 2020 field eval to **frozen-base only**. Dual protocol must not quietly leak.

#### Caveat B — small 2023 WP sample
Table S2 lists **19** WP SIDs (verified). Intensity-tier splits (e.g. typhoon / super-typhoon counts) are **not locked** until classified from IBTrACS for those SIDs. Intensity stats will be noisy — report **bootstrap CIs**; do not overclaim from point estimates.

#### Phase 0 step 1 (actual work)
Not “clone and run notebook only.” Aurora ∉ TCBench baselines. Work is: run frozen Aurora → **TempestExtremes** track extraction → `track_matcher.py` → **`2023_AURORA.csv`** in TCBench schema (`sid, initial_time, valid_time, wind_max, pressure_min, lat, lon`), then evaluate WP SIDs. Pin TCBench commit used in the scorecard.

---

## c) Inter-disciplinary rationale

**Computer Science (primary):** foundation-model adaptation (LoRA / FT), loss design (extremes-weighted, quantile, twCRPS), intensity heads / postprocessing, probabilistic calibration, ablations, significance testing.

**Environmental / atmospheric science (stress domain + verification):** ERA5 / IFS initial conditions; Western Pacific TC meteorology; IBTrACS best tracks; IMERG + Hong Kong Observatory gauges; WeatherBench 2 protocol + binary-extremes / neighbourhood scores.

Classical-only. Quantum is **out of scope** (optional tensor-network negative control only — not the thesis).

---

## d) Research Plan and Methodology

### d1) Tasks by objective

**Phase 0 order (before any LoRA):** (i) pin TCBench v3; Aurora → TempestExtremes → `2023_AURORA.csv`; score WP Table-S2 SIDs (+ frozen HRES/TIGGE where available) → (ii) Gomez-style **linear** head on **frozen** Aurora (TCBench postproc scripts / AIES template) → (iii) WB2-style 2020 field harness (frozen-only until anti-leak training window set) → (iv) only then LoRA / FT with `LORA_HELD_OUT_YEARS = (2020, 2023)`.

**WP1 — LoRA / Aurora-Small extremes adaptation (RQ1)**  
- Data pipeline (Anemoi/Zarr; W Pacific crop) + harness that reproduces frozen GraphCast/Aurora + HRES **before** training.  
- Fine-tune Aurora-Small (full) and Aurora 1.3B (LoRA); extremes-subsampled cases; ablations: loss on/off, LoRA rank, subsample rate; **always report body + tail**.  
- Gate: tail metrics beat frozen base **and** frozen+Gomez control at matched body metrics.

**WP2 — Intensity supervision + heavy-rain arm (RQ2)**  
- Tracking-independent IBTrACS postprocessing on Aurora fields (Gomez-style). Start with linear; escalate architecture only if needed.  
- Heavy-precip / black-rainstorm exceedance vs HKO + IMERG; 0–6 h secondary arm.  
- Optional generative/CorrDiff **stretch only** if intensity gate fails after LoRA + heads.

**WP3 — Calibration, value, write-up (RQ3)**  
- LoRA-ensemble (multi-adapter / IC perturbation / MC dropout-class — **not** diffusion sampling as core). Rank histograms, spread–skill, reliability; REV.  
- Evaluation notebooks/dashboard (replaces prototype app).  
- arXiv draft → NeurIPS/ICLR AI-for-Earth workshop → *JAMES* / *GMD* / AMS AI journal.

### d2) Methods and stack

| Layer | Choice |
|-------|--------|
| Base models | Aurora-Small (113M, full FT); Aurora 1.3B (LoRA) |
| Domain | 100–135°E, 5–40°N; leads 0–72 h core, 0–6 h secondary |
| Losses | Extremes-weighted MSE + pinball (90/95/99) + twCRPS; report body CRPS/RMSE; Wessel weighted-train / linear-pool mitigation |
| Data | ERA5 / IFS analysis init; TCBench IBTrACS-aligned (HF doi:10.57967/hf/8882); IMERG; HKO gauges |
| TC eval | TCBench v3, year 2023, 19 WP SIDs (Table S2); output `2023_AURORA.csv` |
| Field eval | WB2-style year 2020; anti-leak: exclude 2020+2023 from LoRA train, or frozen-only 2020 |
| Training | PyTorch, bf16, gradient checkpointing, 8-bit AdamW/Adafactor on 1 × Blackwell |
| Serving / viz | Evaluation notebooks + lightweight dashboard (Plotly/Streamlit-class) — **not** React Native |
| Out of scope | From-scratch global pretraining; from-scratch diffusion; quantum; product app |

### d3) Rationale and key references

Mean-trained AIWP wins WeatherBench-style averages and loses the tail and TC intensity. The publishable solo contribution on one 92 GB GPU is **method**: loss + adaptation + intensity supervision on a released foundation model, with an evaluation bar that includes HRES on extremes — not another LSTM/CNN + mobile app.

1. Bodnar et al. — Aurora, *Nature*, 2025. doi:10.1038/s41586-025-09005-y  
2. Zhang et al. — Record-breaking extremes, AI vs HRES, *Science Advances*, 2026. doi:10.1126/sciadv.aec1433  
3. Sun et al. — Gray-swan TCs, *PNAS*, 2025. doi:10.1073/pnas.2420914122  
4. Price et al. — GenCast, *Nature*, 2024. doi:10.1038/s41586-024-08252-9  
5. Rasp et al. — WeatherBench 2, *JAMES*, 2024  
6. Guo et al. — FuXi-TC (related generative SOTA), *npj Clim. Atmos. Sci.*, 2026. doi:10.1038/s41612-026-01501-w  
7. Gomez et al. — NeWM TC intensity postprocessing, *AIES*, 2026. doi:10.1175/AIES-D-25-0073.1  
8. Gomez et al. — **TCBench**, arXiv:2601.23268**v3**, 2026 (preprint). HF doi:10.57967/hf/8882; code doi:10.5281/zenodo.23801372; repo https://github.com/tcbench/TCBench  
9. Wessel et al. — twCRPS training for extremes, *MWR*, 2025  
10. Huang et al. — Aurora extremes, pattern–amplitude divergence, *Atmosphere*, 2026  
11. Tennie & Palmer — Quantum for weather/climate, *BAMS*, 2023 (why quantum is out)

Full model table, compute honesty, and quantum blunt section: `Extreme Weather AI Research Proposal.html`.

---

## e) Expected Deliverables and Milestones

| Phase | When (indicative) | Gate / output |
|-------|-------------------|---------------|
| 0 | Weeks 1–3 | `2023_AURORA.csv` on TCBench WP SIDs; linear Gomez floor; WB2-2020 field harness (anti-leak) |
| 1 | Weeks 3–8 | WP1 LoRA/FT ablations vs frozen and frozen+Gomez; RQ1 gate (body+tail) |
| 2 | Weeks 8–14 | WP2 intensity / heavy-rain arm (escalate head only if needed); RQ2 gate |
| 3 | Weeks 14–18 | Calibration, REV, notebooks; arXiv draft |

**Deliverables**

1. Adapted weights + training/eval code (reproducible).  
2. Curated W Pacific extremes subset + WeatherBench 2 / extremes harness.  
3. Evaluation dashboard/notebooks (figures + decision-value summary).  
4. arXiv manuscript; workshop then *JAMES*/*GMD*/AMS AI — **not** Nature Communications as first shot.

**Explicitly dropped from the original draft:** React Native prototype, usability testing, “which features are most predictive?”, LSTM/CNN from scratch, Flask product API as a research goal.
