#!/usr/bin/env python3
"""One Star — entry for The Moon Gets One Star on make.fun.

Prints exactly one line (at most 120 characters): a one-star review
of the Moon, written like a real review.
"""

LINE = "1 star. Been 'almost full' for a week, lights up my yard without asking, and follows my car everywhere. Creepy."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 120
    print(LINE)


if __name__ == "__main__":
    main()
