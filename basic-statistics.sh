#!/bin/bash
# crude commit statistics for a repo

set -e                                                       # exit on any error
set -u                                                       # unset var is error
set -o pipefail                                              # any cmd in pipeline

PATH+=:$(dirname $0)                                         # extra exes
proj=$(basename $(git remote -v | awk '{print $2}'))         # repo name
echo project: $proj

commits=$(git rev-list --all --count)                        # all commits
echo commits: $commits

committers=$(git shortlog -s | wc -l)
echo committers: $committers

first_commit=$(weeks_from_first_commit.py)                   # in weeks
echo first commit: $first_commit weeks ago

