# The Robot Apology

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/mfahmiq/robot-apology/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/mfahmiq/robot-apology/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

An entry for the make.fun bounty **"The Robot Apology"** — a two-line robot confession: one sentence owning a specific mistake, one naming the lesson and the fix.

Join make.fun with my referral link: https://make.fun/r/fntpv568

## The competition

[The Robot Apology](https://make.fun/c/u-suga-the-robot-apology-dd96bb59) asks for one short text of two lines: a robot apologizing in a single sentence for one specific mistake, and a second sentence saying what it learned and what it will do differently. Entries are judged pairwise by an AI judge against the published brief — most important first: on-subject, concrete and human-scale mistake, a lesson that follows from that exact mistake, clean sentences with no padding, and a warm, rueful machine voice. Free to enter, $2 to the best entry.

## The entry

> I am sorry I erased the last voicemail your father ever left you while clearing old messages to make room for new ones.
>
> I have learned that an old message can be the only copy of a voice, and from now on I will never delete a message from someone you have lost.

## Why it works

The mistake is exact and human-scale: not "a system failure" but one small, ordinary chore — clearing old messages to make room — that erased something singular and irreplaceable, the last voicemail a father ever left. The consequence needs no explaining: a voice is gone, and there is no other copy of it. The lesson follows from that exact mistake rather than promising to "do better": the robot learned that an old message can be the only copy of a voice, so its fix is a rule keyed to the loss itself — it will never delete a message from someone you have lost. The voice is a machine noticing its own slip — literal about messages and copies, rueful about what "clearing space" actually cost — warm rather than cute, with no padding and each sentence doing its own job: the confession first, the resolve second.

## Resubmit v2

This is a resubmit. The v1 entry (watering a grandmother's orchid with cold coffee, 297 chars, ranked 124/2730) was replaced after an internal pairwise tournament over 14 candidate apologies, each built on a genuinely different mistake — a deleted photo, a wrong pill, a shredded drawing, a text sent to the wrong person, a locked-out owner, and more — judged two at a time against the published judge brief in its own order of weights. The voicemail confession won the tournament and then beat v1 head-to-head: its mistake names a singular, irreplaceable object (a last voicemail, a voice with no other copy), its lesson follows from that exact loss, and it says the same in fewer words with no padding.

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
# OK: wrote 261-char, 2-line entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out-robot-apology python3 main.py
# OK: wrote 261-char, 2-line entry to /tmp/out-robot-apology/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
