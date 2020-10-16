#!/bin/bash -eu

PATH+=:$PWD                                                          # rat cheer
dir=${1##*/}                                                         # the repo
rm -rf $dir                                                          # cleanliness
git clone -q $1                                                      # get the repo
cd ${_##*/}                                                          # punctuation
commits=$(git rev-list --all --count master)                         # all commits
echo $commits commits in $1                                               
first_commit=$(weeks_from_first_commit.py)                           # in weeks
for week in $(seq $first_commit 0); do                               # every week
  git rev-list --all --count --before="$week weeks ago"              # cumulative
done |
  nl > commits-per-week.txt                                          # number weeks
