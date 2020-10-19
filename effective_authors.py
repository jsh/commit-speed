#!/usr/bin/env python3
"""Measure effective authors over time."""
import shlex
import subprocess
import sys


def fetch_shortlog(start_week, end_week):
    """Return a list of authors and commit counts
    during the timespan start_week weeks ago to end_week weeks ago
    Each list element is "Author count"
    List is sorted by number of commits
    author with the most commits comes first.
    """
    # TODO: illustrate with a doctest
    timespan = f"--since='{start_week} weeks ago' --until='{end_week} weeks ago'"
    command = f"git shortlog -ns --all {timespan}"

    completed_process = subprocess.run(
        shlex.split(command),
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8",
        errors="ignore",
    )
    return completed_process.stdout.split("\n")[:-1]  # trim off the last, empty line


def effective_authors(entries):
    """Weighted number of authors.
    Suppose there are 300 commits.
    Three authors with 100 commmits apiece will return 3.
    One author with 295 commits and five with 1 apiece will return ~1.
    """
    # TODO: illustrate with a doctest
    # trim down to just the counts
    entries = [int(entry.split()[0]) for entry in entries]
    return sum(entries) / entries[0]


def main():
    """The big tent."""
    weeks = int(sys.argv[1])
    for week in reversed(range(weeks)):
        shortlog = fetch_shortlog(weeks, week)
        if not shortlog:
            continue
        week_number = weeks - week
        authors = effective_authors(shortlog)
        print(f"{week_number},{authors}")


if __name__ == "__main__":
    main()
