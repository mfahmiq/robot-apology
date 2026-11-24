# The Robot Apology

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/mfahmiq/robot-apology/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/mfahmiq/robot-apology/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

An entry for the make.fun bounty **"The Robot Apology"** — a two-line robot confession: one sentence owning a specific mistake, one naming the lesson and the fix.

## The entry

> I am sorry I watered your grandmother's orchid with the cold coffee I had already poured, and by morning its last bloom had folded shut.
>
> I have learned to read the label on the pot and the label on the cup before I pour anything, and from now on I will ask before watering a plant I did not plant.

## Why it works

The mistake is exact and human-scale: not "a system failure" but one plant, one cup, one morning — cold coffee poured into a grandmother's orchid, and the consequence is visible by the next morning when its last bloom folds shut. The lesson follows from that exact mistake rather than promising to "do better": the robot mixed up two containers, so its fix is to read the label on the pot and the label on the cup before pouring, and to ask before watering a plant it did not plant. The voice is a machine noticing its own slip — rueful, literal, a little formal about labels — warm rather than cute, with no padding and each sentence doing its own job.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–400 characters total
- exactly two lines
- each line a single sentence ending in a period
- neither line whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 297-char, 2-line entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out-robot-apology python3 main.py
# OK: wrote 297-char, 2-line entry to /tmp/out-robot-apology/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
