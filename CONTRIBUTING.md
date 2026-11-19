# Contributing

Research PoW workflow, adapted from Rovierr HQ (`feature → integration → main`) and standard open-source ML practice.

## Branch model

| Branch | Role |
|--------|------|
| `main` | Default; protected; releases / paper-freeze tags |
| `dev` | Optional integration before `main` |
| `feat/<n>-slug` | Feature / phase work (open a GitHub issue first) |
| `fix/<n>-slug` | Bugfix |
| `docs/<slug>` | Proposal / paper-only edits |

Never push straight to `main`. Open a PR; wait for **CI** (ruff + pytest).

## PR checklist

1. Linked issue (`Fixes #N` / `Refs #N`)  
2. CI green  
3. No large data / weights / secrets  
4. If changing evaluation protocol or claims: update the proposal MD and note it in the PR  

## Commit messages

Conventional, short:

- `feat: …` — new capability  
- `fix: …` — bug  
- `docs: …` — proposal / README  
- `ci: …` — workflows / templates  
- `test: …` — tests only  
- `chore: …` — tooling  

## Code quality gates (required on PR)

- `ruff check`  
- `ruff format --check`  
- `pytest`  

Locally: `pip install -e ".[dev]" && ruff check src tests && ruff format --check src tests && pytest -q`

## Scientific discipline

- Report **body + tail** metrics when using twCRPS (Wessel body–tail trade-off).  
- Keep the attribution factorial: frozen → frozen+Gomez → LoRA → LoRA+Gomez.  
- Diffusion / CorrDiff / quantum = stretch only; do not sneak into core claims.
