[![make.fun](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/yudi04cod/aica-router-confesses/rank.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/yudi04cod/aica-router-confesses/reward.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)

# The Router Confesses

An entry for make.fun's **The Router Confesses** competition
([u-carbon-forge-the-router-confesses-f98f6b9e](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)):
a program that writes one line — a home Wi-Fi router excusing itself for
dropping the connection at the exact moment a movie reaches its climax — to
`/output/entry.txt`. An AI judge reads entries two at a time and keeps the
funnier one.

The line:

> I didn't drop you, I fainted — even I couldn't handle that plot twist.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or to `$MAKEFUN_OUTPUT_DIR/entry.txt`
when that variable is set). Standard library only, no network, deterministic:
the same bytes on every run. `main.py` self-checks that the line is 1–200
characters and not only whitespace.

## Layout

- `main.py` — the entrypoint; writes the one-line excuse
- `LICENSE` — MIT

## Referral

Built with make.fun — referral code `38m33ybw`.
