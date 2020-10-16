#!/bin/bash -eu
# create commits-per-week data
# from a repository

PATH+=:$(dirname $0)                                                 # extra exes
proj=${1%.git}                                                       # trim ".git" if given
dir=${proj##*/}                                                      # the repo
rm -rf $dir                                                          # cleanliness
git clone -q $proj                                                   # get the repo
cd ${_##*/}                                                          # punctuation
commits=$(git rev-list --all --count)                                # all commits
echo $commits commits in $proj                                               
first_commit=$(weeks_from_first_commit.py)                           # in weeks
for week in $(seq $first_commit 0); do                               # every week
  git rev-list --all --count --before="$week weeks ago"              # cumulative
done > commits-per-week.txt
awk '{print NR "," $1}' commits-per-week.txt > commits-per-week.csv  # spreadsheet-ize
