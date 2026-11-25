"""One-line entry for make.fun: a dog, a treat jar, and a hiding place.

The program writes exactly one 127-character line to entry.txt and
nothing else. The first half sets up the dog cracking the treat jar;
the last clause delivers the twist — the snacks now live in the
vegetable drawer, the one place neither dog nor owner ever looks.
No title, no preamble, and no explanation of the joke is included
in the output file.
"""

import os

LINE = "My dog learned to open the treat jar, so now I hide my snacks in the vegetable drawer — the one place neither of us ever looks."


def write_entry() -> str:
    """Write the line to the output directory and return its path."""
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
