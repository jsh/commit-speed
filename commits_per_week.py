#!/usr/bin/env python3
"""Print number of commits per week."""

import os

from git import Repo  # type: ignore


def main():
    """The big tent."""
    seconds_per_week = 60 * 60 * 24 * 7
    cwd = os.getcwd()
    repo = Repo(cwd)
    commits = repo.iter_commits("--all")

    first = next(commits)
    commits_in_week = 1
    weeks_end = first.committed_date
    weeks_start = weeks_end - seconds_per_week
    for commit in commits:
        commit_date = commit.committed_date
        if commit_date < weeks_start:
            print(commits_in_week)
            commits_in_week = 0
            weeks_end = weeks_start
            weeks_start = weeks_end - seconds_per_week
        commits_in_week += 1
    print(commits_in_week)

if __name__ == "__main__":
    main()
