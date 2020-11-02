#!/usr/bin/env python3
"""Print weeks from first commit."""

import shlex
import subprocess  # nosec
from datetime import date


def weeks() -> int:
    """Calculate the number of weeks for the current repo.
    :returns: number of weeks
    :rtype: int
    """
    # TODO: take a repo as an arg.

    latest_commit_date = date.today()
    command = "git log --all --date='format:%F' --format='%cd' --reverse"
    completed_process = subprocess.run(  # nosec
        shlex.split(command), capture_output=True, text=True, check=True
    )
    first_commit = completed_process.stdout.split("\n")[0]
    first_commit_date = date.fromisoformat(first_commit)
    return (latest_commit_date - first_commit_date).days // 7 + 1  # just in case


def main():
    """The big tent."""
    print(weeks())


if __name__ == "__main__":
    main()
