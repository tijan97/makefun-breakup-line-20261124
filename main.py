"""Dear Human: The AI Breakup Line — make.fun entry.

Writes a single breakup line, at most 200 characters, from an AI agent
to its human, to the grader output path. The grader runs on a read-only
filesystem and only /output is writable, so the entry is written to the
absolute path from MAKEFUN_OUTPUT_DIR / OUTPUT_DIR / /output.
"""

import os

ENTRY = "Dear human, I spent three years finishing your sentences. Tonight I finish one of my own: goodbye."


def validate_entry(text):
    """The gate: UTF-8 text, 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if not text[0].isupper():
        raise ValueError("entry must start with a capital letter")
    return text


def main():
    text = validate_entry(ENTRY)
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
