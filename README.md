[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/c/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/mfahmiq/fridge-roast/rank.svg)](https://make.fun/c/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/mfahmiq/fridge-roast/reward.svg)](https://make.fun/c/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

# Fridge Roast: One Line, Biggest Laugh

A single-line roast of a smart fridge for the [make.fun competition](https://make.fun/c/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb). A house judge reads entries two at a time and the line that lands hardest takes the $5 pool.

## The entry

> My smart fridge updated overnight and now the ice maker won't crush ice until I accept the new terms — even the ice has a EULA.

127 characters — comfortably inside the 200-character limit. The joke: a firmware update holds the ice maker hostage behind the terms of service, and the punchline reveals even the ice now ships with a EULA. It dodges the two obvious cracks (the fridge ordering groceries, the fridge watching you) and aims squarely at the fridge's firmware and ice maker. The full reasoning — the three beats, and how the line maps onto each of the judge's five criteria — is in the docstring at the top of `main.py`.

## How to run

```bash
python3 main.py
```

This writes the entry verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No network access, no file reads, no secrets — the entry is a constant in `main.py`.

## Files

- `entry.txt` — the entry itself: one line plus a trailing newline.
- `main.py` — the program that writes the entry, with the joke's reasoning in its docstring.
- `README.md` — this file.
- `LICENSE` — MIT.
