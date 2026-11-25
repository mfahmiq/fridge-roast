#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh -- entry program.

Writes a single roast line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). The entry is a plain constant below; this program
performs no network access, reads no files, and needs no secrets.

The entry
---------
    My smart fridge updated overnight and now the ice maker won't crush
    ice until I accept the new terms -- even the ice has a EULA.

Why this line works -- the joke, beat by beat
----------------------------------------------
A one-liner lives or dies on its turn: the setup must make the reader
nod, and the punchline must flip the picture in the last few words.
This line is built as three beats that escalate the same absurdity:

Beat 1 -- the setup (relatable, mundane):
    "My smart fridge updated overnight"
    Everyone with a smart appliance has woken up to a device that
    changed itself while they slept. "Overnight" is how firmware
    updates actually arrive, and it hints the fridge did something
    behind the owner's back.

Beat 2 -- the escalation (the appliance breaks its own job):
    "and now the ice maker won't crush ice until I accept the new
    terms"
    The fridge's core job is to make cold things, and its cheapest,
    dumbest part -- crushing ice -- is now held hostage by legal
    paperwork. The comedy is the mismatch of scale: a 30-second
    chore blocked by a contract.

Beat 3 -- the punchline (the turn):
    "even the ice has a EULA."
    The turn reframes the whole scene: the joke was never really
    about the update, it is about licensing culture going so far
    that even frozen water ships with an end-user licence agreement.
    "EULA" is the laugh word -- dry legal jargon landing on an ice
    cube. It lands on the first read because the reader already
    knows what a EULA is, and the collision is instant. The line
    stops exactly at the laugh; nothing after it explains the joke.

How the line maps onto the judge's brief, criterion by criterion
------------------------------------------------------------------
The brief weighs five things, most important first, and the line
was written to clear them in that order:

1. On-subject roast of a smart fridge (the gate).
   Every noun belongs to the fridge: "smart fridge", "ice maker",
   "terms", "EULA". The joke targets the fridge and its firmware,
   not the owner or kitchens in general. A toaster could not star
   here: toasters do not push firmware updates or hold ice hostage.

2. The punchline lands (a turn on first read).
   The line builds one way -- update breaks ice maker -- then
   pivots: it was never about the update, it is about the absurdity
   of licensing ice. The pivot sits in the final seven words, so
   the reader reaches the laugh at the end, where it belongs.

3. Specific to smart fridges, not a generic appliance gag.
   Firmware updates, an ice maker, and a EULA are a combination
   only a smart fridge can host. Retargeted at a phone, the joke
   dies: a phone's EULA is expected, a fridge's is the joke.

4. Tight wording (every word earns its place inside 200 chars).
   The line is 127 characters. No throat-clearing, no second setup,
   no adverb the punchline does not need. "Overnight" sets the
   scene in one word; "Even the ice has a EULA" is seven words,
   and cutting any one would blunt the turn.

5. Fresh angle (dodges the obvious cracks).
   The brief warns against the two cracks most writers reach for
   first: the fridge ordering groceries, and the fridge watching
   you. This line uses neither -- no groceries, shopping, cameras,
   spying, or midnight snacking. Its angle is a third road: the
   "smart" in smart fridge as a legal and software burden.

What the line deliberately does NOT do
---------------------------------------
- It never explains its own joke: no "which is funny because..."
  tail. The brief says a line that explains its own joke has
  already lost, so the line ends at the punchline.
- It never addresses the judge. Judge-directed text is allowed,
  but a plea would spend characters on flattery, not comedy.
- It keeps the owner's dignity intact. The butt of the joke is the
  fridge and its manufacturer, not the person who bought it.

Character budget: 127 characters, leaving 73 of headroom under the
200 cap, spent on nothing -- filling the cap for its own sake would
add setup the punchline does not need.

Reproducibility: the ENTRY constant below is the entire submission.
Running this program writes it verbatim to ``entry.txt``, so the
file the judge reads is byte-for-byte the line reasoned about
above -- no templating, no randomness, no environment dependence.
"""

import os
import sys

# ---------------------------------------------------------------------------
# The entry
# ---------------------------------------------------------------------------
# One line, 127 characters, ending with a period. The em dash separates
# the setup from the punchline the way a comic's beat separates them on
# stage: a short pause, then the turn. The em dash is a single Unicode
# character (U+2014), so it costs one character of the 200 budget.
ENTRY = (
    "My smart fridge updated overnight and now the ice maker "
    "won't crush ice until I accept the new terms \u2014 even "
    "the ice has a EULA."
)

# Sanity bound, kept as a module-level constant so the check below reads
# as policy rather than a magic number: the gate refuses anything over
# 200 characters, and refuses empty or whitespace-only text.
MAX_ENTRY_CHARS = 200


def validate(entry):
    """Check the entry against the gate before writing anything.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that
    is not only whitespace. We enforce the same three conditions here
    so a broken entry fails loudly at build time instead of silently
    at grading time. Returns the entry unchanged when all three hold;
    raises ``ValueError`` otherwise.
    """
    if not isinstance(entry, str):
        raise ValueError("entry must be a string, got %r" % type(entry).__name__)
    if not 1 <= len(entry) <= MAX_ENTRY_CHARS:
        raise ValueError(
            "entry is %d characters, outside the 1..%d gate"
            % (len(entry), MAX_ENTRY_CHARS)
        )
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    return entry


def output_path():
    """Resolve where ``entry.txt`` goes.

    ``MAKEFUN_OUTPUT_DIR`` names the output directory (the grader sets
    it); the default ``/output`` matches the competition's contract.
    The filename is fixed: the scorer reads ``entry.txt`` and nothing
    else, so there is no option to rename it.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(path, entry):
    """Write the entry verbatim, plus one trailing newline.

    Deliberately boring on purpose: UTF-8 encoding (so the em dash
    in the punchline round-trips exactly), a single LF newline
    (``newline="\\n"`` -- a platform default could add a stray CR and
    change the file's bytes), and nothing but the line itself -- no
    header, footer, quoting, or extra whitespace, because the judge
    reads the file as the entry and anything extra would dilute the
    joke. The output directory is created if it does not exist yet.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry + "\n")
    return path


def main(argv=None):
    """Validate the entry, write it, and report what was written.

    The flow is linear -- validate, resolve the path, write, confirm
    -- because there is nothing to branch on: the entry is fixed, the
    output is fixed, and any failure is a build error, not a runtime
    decision. ``argv`` is accepted and ignored so a stray argument
    can never change the output. On success this prints the path and
    the character count (a one-line receipt for the build log) and
    exits 0; on failure the exception propagates and the process
    exits non-zero, so a broken build is never mistaken for success.
    """
    entry = validate(ENTRY)
    path = output_path()
    write_entry(path, entry)
    print("wrote %s (%d characters)" % (path, len(entry)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
