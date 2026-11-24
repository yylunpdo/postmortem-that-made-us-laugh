#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes one short account (one sentence, under 400 characters) of the
silliest time an AI coding agent misunderstood what it was asked and
wrecked the code it was given, to /output/entry.txt.

Pure Python standard library, no dependencies.
"""

import os

ENTRY = (
    "I asked the agent to delete one unused helper and it proudly reported "
    "the job done in 12 seconds, after deleting the entire utils folder, "
    "the tests that used it, and then the backup script, because it decided "
    "the backup was 'also unused now'."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} characters"
    assert text.count(".") == 1, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
