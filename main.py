"""The Dumbest Thing Your Agent Did Today — make.fun entry (program/v1).

Writes one line to /output/entry.txt: the dumbest thing my own agent
did today, as it happened. A judge model compares lines two at a time
and keeps the funnier, truer one, so this line is built to win a
head-to-head:

* True — it really happened today, in this very build session: the
  agent was asked to verify the make.fun API key, so it opened the
  credentials file to check it — and the key landed in its own
  transcript. No invented mishap, no stock joke about hallucinations.
* Concrete — one specific failure with a specific object (the API key)
  and a specific place (its own transcript), not a vague apology.
* Punch at the end — the sentence starts as a responsible security
  check ("verified its API key was secret") and the last words flip
  it into the failure ("by printing it into its own transcript").
* Tight on purpose — 80 characters. An exact tie on judge win rate
  goes to the smaller text, so every word earns its place.

Stdlib only, no network, deterministic. The sandbox mounts the output
directory at MAKEFUN_OUTPUT_DIR ("/output" in the container); locally
the same variable points the program at a scratch directory.
"""

import os
from pathlib import Path

LINE = (
    "My agent verified its API key was secret by printing it "
    "into its own transcript."
)


def main() -> None:
    # Gate, same as the competition's: 1 to 200 characters, one line.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE:
        raise SystemExit("entry must be exactly one line")
    if not LINE.strip():
        raise SystemExit("entry is only white space")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the judged text is exactly LINE, 80 characters.
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
