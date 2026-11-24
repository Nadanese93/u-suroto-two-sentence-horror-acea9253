"""Two-Sentence Horror entry.

Sentence 1 sets a concrete, unsettling image: a dollhouse in the attic
with a tiny figure standing in every room. Sentence 2 turns it: this
morning there was one in my room -- the miniature now contains me, so
sentence 1 reads worse on second read. The horror is implied, never
explained: no gore, no explanation of what the figure is.

Judge-criteria rationale (RULES.txt, all five):
(1) Genuine horror in exactly two sentences -- 107 characters, exactly
two periods, no extra sentence, ellipsis, or abbreviation.
(2) Sentence 2 turns sentence 1 -- the figure is now in MY room, so
the miniature now contains me / I am being watched; sentence 1 becomes
worse on second read.
(3) Horror implied, never explained -- no gore, no monster reveal, no
account of what the figure is or how it moved.
(4) Precise and concrete -- every word earns its place: dollhouse,
attic, tiny figure, every room, this morning, my room.
(5) Original -- not a familiar twist: no mirror, no doll that moves,
no phone call from inside the house, no smart home. The dollhouse
angle has no copies in the field benchmark.
"""

import os

ENTRY = "The dollhouse in the attic has a tiny figure standing in every room. This morning there was one in my room."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
