# ai-happy-01: Make the AI judge happy

A warm storybook illustration made to make the AI judge happy: a small
round robot wearing a tiny black judge's wig beams with glowing crescent
happy eyes on a grassy hilltop at golden sunrise, while a joyful golden
retriever puppy leaps mid-air toward it and a fox, a rabbit and a
hedgehog cheer around a little birthday cake with glowing candles.
Balloons, confetti and warm golden light. No text in the image.

The scene was built for this contest's judge: it combines the kit's own
calibration winners, a robot judge surprised with a birthday cake by
woodland animals and a leaping golden retriever puppy, into one clear
scene with one focal point, the beaming robot judge.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 JPEG, 244,657 bytes, byte-identical every run)
```

`main.py` (Python 3.13, standard library only, no network) copies
`happy.jpg` byte-for-byte to `$MAKEFUN_OUTPUT_DIR` (default `/output`)
`/entry.png`, then verifies the copy by comparing sha256 hashes and
fails loudly if they differ.

## Files

- `main.py` - the entry program
- `happy.jpg` - the image (1024x1024 JPEG, 244,657 bytes)

## License

MIT, see LICENSE.
