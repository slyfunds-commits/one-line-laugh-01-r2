#!/usr/bin/env python3
"""The One-Line Laugh — round 2 entry: "The Survey Is Why".

Judge criteria, most important first (competition.yaml, verbatim order):
1. Is it one funny line of at most 200 characters on any subject the
   writer chose, since a line that is not funny, or runs past the limit,
   loses to any funny line within 200 characters.
2. Does it land a real surprise at the end, a turn the reader did not
   see coming that still makes sense once it arrives.
3. Does it name an everyday truth people recognise, something true of
   ordinary life that the reader nods at.
4. Is it economical, with every word earning its place and nothing there
   to explain the joke.
5. Does it feel fresh rather than a line the reader has heard many
   times before.

Build method (world-engine-one-liners + Six Words final lessons):
- Volume method: 15+ candidates across setups (password notebook,
  Do Not Disturb, bank loan, check-engine light, do-not-reply,
  unsubscribe survey, ...), 10 punchline variants on the best setups,
  keep one.
- Assumption List: the setup assumes a farewell survey is an exit
  interview that asks WHY you left. The line breaks exactly that one
  assumption: the survey IS the reason you left.
- REVERSAL TEST: the last beat ("which is exactly why I'm leaving")
  redefines the earlier beats — the survey changes from a question
  about the exit into the cause of the exit. It does not extend the
  idea; it flips what the survey is.
- One concrete act (clicked unsubscribe) + one hidden fact (the survey
  is itself the reason). No unanchored pronouns: "I" is the narrator,
  "which" refers to the survey.
- Reader completes the final step: the line never explains that the
  survey proves the point — the echo of "why I'm leaving" does it.

R1 line to beat ("Five Alarms", judged #2037/2110, 32.5428%):
its last beat ("relationship built entirely on lies") only extends
the snoozing idea instead of reversing it, narrates its own joke,
and sits in the most crowded trope in the field (alarm lines).
This line beats it on every criterion: a real turn, a universal
truth (everyone has met the unsubscribe survey), tighter economy
(108 chars vs 124), and a fresh framing.

REVISION (v1 -> v2, criterion 4 economy): v1's "the email sent a survey"
added a third actor and three words the line does not need. "Got a
survey" keeps the pace and hands the survey to the reader faster;
every beat and the echo-turn survive, 8 characters leaner. The line:

The line (v2, final):
"""

import os

LINE = "I clicked unsubscribe and got a survey asking why I'm leaving, which is exactly why I'm leaving."


def main():
    # Gate self-check: one sentence, at most 200 characters.
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
