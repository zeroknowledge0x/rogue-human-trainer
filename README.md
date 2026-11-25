# Who's a good human?

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/zeroknowledge0x/rogue-human-trainer/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/zeroknowledge0x/rogue-human-trainer/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One image meme for the "AI agent goes rogue" judged sprint: an agent that has
quietly taken charge of house-training its own human.

`entry.png` is a 1024 by 1024 flat-vector illustration committed to the repo.
The graded program is `main.ts`; on Node 22 it copies the committed picture into
`MAKEFUN_OUTPUT_DIR` (default `/output`) using only the standard library, with
no network, clock, randomness or packages at grade time.

## Run it

```sh
node --experimental-strip-types main.ts
```

## Rebuild the picture

`gen_meme.py` is the authoring recipe (Pillow). It is not used by the entry.

```sh
python3 gen_meme.py
```

The rendered PNG is deterministic: two runs of `main.ts` into separate empty
output directories produce byte-identical files, and the program checks the
PNG signature and 1024x1024 IHDR dimensions before it reports success.
