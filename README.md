# Tail-First Forecasting

Extremes-weighted LoRA / Aurora-Small fine-tuning for **Western Pacific tropical-cyclone intensity** and heavy precipitation (Hong Kong / SE Asia). Solo research PoW → arXiv + workshop.

**Proposal:** [`RESEARCH PROPOSAL_CLIMATE.md`](RESEARCH%20PROPOSAL_CLIMATE.md) · interactive: [`Extreme Weather AI Research Proposal.html`](Extreme%20Weather%20AI%20Research%20Proposal.html)

## Locked scope

| Item | Choice |
|------|--------|
| Domain | 100–135°E, 5–40°N |
| Core | 0–72 h TC **intensity** (+ track secondary) |
| Secondary | 0–6 h heavy rain / HK black-rainstorm (>70 mm/h) |
| Method | Aurora-Small FT and/or Aurora 1.3B LoRA; Gomez-style intensity head |
| Out | React Native app; from-scratch global model; from-scratch diffusion; quantum |

## Phase 0 order

1. Reproduce **frozen Aurora + HRES** baselines on the crop  
2. **Frozen Aurora + linear Gomez head** (cheap floor + attribution control)  
3. Only then LoRA / FT  

## Dev setup

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\activate
pip install -e ".[dev]"
ruff check src tests
ruff format --check src tests
pytest -q
```

## Branch & merge (Rovierr-inspired, research-scaled)

- `main` — protected; green CI required  
- `dev` — integration (optional for solo work)  
- `feat/<issue>-short-name` — all work lands via PR  

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
