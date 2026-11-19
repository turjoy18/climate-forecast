# RESEARCH PROPOSAL

**Working title:** Tail-First Fine-Tuning: Extremes-Weighted LoRA Adaptation of Aurora for Western Pacific Tropical-Cyclone Intensity and Heavy Precipitation

**Status:** Decisions locked 20 Nov 2026 · Consensus-backed rebuild of the generic draft  
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
3. **Evaluate** under a pre-registered protocol: WeatherBench 2 + CSI/ETS, FSS, twCRPS, TC track+intensity, against persistence/climatology, IFS HRES, IFS ENS / AIFS-ENS, GraphCast/Aurora, on a held-out year with significance — verified on IBTrACS + HKO gauges / IMERG, not ERA5 precip alone.
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

---

## c) Inter-disciplinary rationale

**Computer Science (primary):** foundation-model adaptation (LoRA / FT), loss design (extremes-weighted, quantile, twCRPS), intensity heads / postprocessing, probabilistic calibration, ablations, significance testing.

**Environmental / atmospheric science (stress domain + verification):** ERA5 / IFS initial conditions; Western Pacific TC meteorology; IBTrACS best tracks; IMERG + Hong Kong Observatory gauges; WeatherBench 2 protocol + binary-extremes / neighbourhood scores.

Classical-only. Quantum is **out of scope** (optional tensor-network negative control only — not the thesis).

---

## d) Research Plan and Methodology

### d1) Tasks by objective

**Phase 0 order (before any LoRA):** (i) reproduce frozen Aurora + HRES baselines on the W Pacific crop → (ii) Gomez-style **linear** head on **frozen** Aurora as the cheap floor → (iii) only then LoRA / FT.

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
| Data | ERA5 / IFS analysis init; IBTrACS; IMERG; HKO gauges |
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
8. Wessel et al. — twCRPS training for extremes, *MWR*, 2025  
9. Huang et al. — Aurora extremes, pattern–amplitude divergence, *Atmosphere*, 2026  
10. Tennie & Palmer — Quantum for weather/climate, *BAMS*, 2023 (why quantum is out)

Full model table, compute honesty, and quantum blunt section: `Extreme Weather AI Research Proposal.html`.

---

## e) Expected Deliverables and Milestones

| Phase | When (indicative) | Gate / output |
|-------|-------------------|---------------|
| 0 | Weeks 1–3 | Harness + frozen Aurora/HRES reproduce; then frozen Aurora + linear Gomez head |
| 1 | Weeks 3–8 | WP1 LoRA/FT ablations vs frozen and frozen+Gomez; RQ1 gate (body+tail) |
| 2 | Weeks 8–14 | WP2 intensity / heavy-rain arm (escalate head only if needed); RQ2 gate |
| 3 | Weeks 14–18 | Calibration, REV, notebooks; arXiv draft |

**Deliverables**

1. Adapted weights + training/eval code (reproducible).  
2. Curated W Pacific extremes subset + WeatherBench 2 / extremes harness.  
3. Evaluation dashboard/notebooks (figures + decision-value summary).  
4. arXiv manuscript; workshop then *JAMES*/*GMD*/AMS AI — **not** Nature Communications as first shot.

**Explicitly dropped from the original draft:** React Native prototype, usability testing, “which features are most predictive?”, LSTM/CNN from scratch, Flask product API as a research goal.
