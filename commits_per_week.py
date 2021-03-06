#!/usr/bin/env python3
"""Print number of commits per week."""

import sys
from typing import List

from git import Repo  # type: ignore

from parse_args import parse_args

SECONDS_PER_WEEK = 60 * 60 * 24 * 7


def commits_per_week(repo: Repo) -> List[int]:
    """Commits per week in repo.

    :param repo git.Repo: repo to report on
    :return: list of commits, earliest commit first
    :rtype: list[int]
    """
    commits = repo.iter_commits("--all")
    commits_in_weeks = []

    last_commit = next(commits)
    week_end = last_commit.committed_date
    week_start = week_end - SECONDS_PER_WEEK
    commits_in_week = 1
    for commit in commits:
        commit_date = commit.committed_date
        if commit_date < week_start:
            commits_in_weeks.append(commits_in_week)
            commits_in_week = 0
            week_end = week_start
            week_start = week_end - SECONDS_PER_WEEK
        commits_in_week += 1
    # very first commits may not make up an entire week
    commits_in_weeks.append(commits_in_week)
    commits_in_weeks.reverse()  # Matthew 20:16
    return commits_in_weeks


def cums(counts: List[int]) -> List[int]:
    """Turn a list of counts into a cumulative list.

    :param list[int] counts: the list of counts
    :returns: cumulative counts, e.g., [1,2,3] -> [1,3,6]
    :rtype: list[int]
    """
    accumulator = 0
    running_sums = []
    for count in counts:
        accumulator += count
        running_sums.append(accumulator)
    return running_sums


def main():
    """The big tent."""
    args = parse_args(sys.argv[1:])
    repo = Repo(args.repo)
    cpw = commits_per_week(repo)
    if args.cumulative:
        cpw = cums(cpw)
    for commits in cpw:
        print(commits)


if __name__ == "__main__":
    main()
