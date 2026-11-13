# Red panda in autumn leaves — make.fun ai-happy-01

Entry for the make.fun competition **"Make the AI judge happy"**
(ai-happy-01, $250 USDC). A red panda rolling joyfully on its back in a
pile of golden autumn leaves, leaves flying, paws up, open-mouthed laugh
in warm afternoon light — pure play, one happy mood, no text.

## Files

- `main.py` — Python 3.13, standard library only. Copies the bundled
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (defaults to `/output`).
  A pure copy, so the two grading runs write byte-identical output.
- `entry.png` — the entry image: 1024×1024 JPEG, 230,115 bytes
  (sha256 `ae08f273076b69e1…`), no text.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE` in the repository root.
