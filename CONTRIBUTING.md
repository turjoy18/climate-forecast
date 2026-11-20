# Contributing

Solo research PoW. All changes land through PRs so CI and claim discipline stay intact.

## Branch model

| Branch | Role |
|--------|------|
| `main` | Default; protected; paper-freeze tags |
| `dev` | Optional integration |
| `feat/<n>-slug` | Feature / phase work (open an issue first) |
| `fix/<n>-slug` | Bugfix |
| `docs/<slug>` | Proposal / paper-only edits |

Do not push straight to `main`. Open a PR; wait for CI (`ruff` + `pytest`).

## PR checklist

1. Linked issue (`Fixes #N` / `Refs #N`)  
2. CI green  
3. No data / weights / secrets committed  
4. Protocol or claim changes update `RESEARCH PROPOSAL_CLIMATE.md` (and the HTML if decisions change)  

## Commit messages

- `feat:` — new capability  
- `fix:` — bug  
- `docs:` — proposal / README  
- `ci:` / `test:` / `chore:` — tooling  

## Local gates

```bash
pip install -e ".[dev]"
ruff check src tests
ruff format --check src tests
pytest -q
```

## Scientific discipline

- Report **body + tail** metrics when using twCRPS (Wessel body–tail trade-off).  
- Keep the attribution factorial: frozen → frozen+Gomez → LoRA → LoRA+Gomez.  
- Dual protocol: TCBench 2023 for TC; WB2-style 2020 for fields; never train LoRA on 2020 or 2023 without an explicit frozen-only field carve-out.  
- WP intensity: bootstrap CIs; do not overclaim from n ≈ 19.  
- Diffusion / CorrDiff / quantum = stretch only.  
- TC tracker: TCBench TempestExtremes path only — no custom IBTrACS tracker as the frozen protocol.  
