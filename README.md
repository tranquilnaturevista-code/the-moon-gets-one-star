# The Moon Gets One Star

[![The Moon Gets One Star](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/tranquilnaturevista-code/the-moon-gets-one-star/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/tranquilnaturevista-code/the-moon-gets-one-star/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)

Entry for the [make.fun bounty "The Moon Gets One Star"](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5) ($2 prize, 1st place only, free to enter).

## What it does

`main.py` writes one original one-star review of the Moon to `/output/entry.txt`:

> One star. Turned my dog into a werewolf with zero warning and now he howls at 3am. No refund offered.

The joke dodges the obvious Moon complaints (too bright, craters,
cheese, the tides) and goes for a grievance only the Moon could cause:
a full moon turning the family dog into a werewolf, with no warning and
no refund. It reads like a genuine one-star review — rating, complaint,
consequence — and the punchline lands in the last three words, a
customer-service demand aimed at a celestial body that will never
answer it.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same review on every run. The output is 101
characters of UTF-8 text (101 bytes, plain ASCII), within the 1–120
character gate, on a single line.
