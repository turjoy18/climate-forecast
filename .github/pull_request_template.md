## Summary

<!-- What and why (not how). Link proposal section if scientific. -->

## Type

- [ ] `feat` — Phase / method work
- [ ] `fix`
- [ ] `docs` — proposal / paper
- [ ] `ci` / `chore` / `test`

## Linked issue

Fixes #

## Checklist

- [ ] CI passes (`ruff` + `pytest`)
- [ ] No data / weights / secrets committed
- [ ] Body **and** tail metrics touched if changing losses/eval
- [ ] Attribution controls preserved (`frozen`, `frozen+Gomez`, …) if claiming a win
- [ ] Diffusion / quantum changes labelled **stretch only**

## Test plan

- [ ] `pytest -q`
- [ ] (if applicable) note which baseline / control this unblocks
