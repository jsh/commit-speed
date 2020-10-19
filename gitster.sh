#!/bin/bash -eu
# Percentage of weekly commits by Junio C Hamano
# Ugh. Written in haste. This *so* needs a re-write.

set -e                                                       # exit on any error
set -u                                                       # unset var is error
set -o pipefail                                              # any cmd in pipeline


echo "Fraction of Commits by Junio C Hamano"
echo
printf "week\tfraction\n"
printf "================\n"
for i in {0..811}; do
    printf "$((811-i))\t"
    gitster=$(git shortlog -ns --all --author='gitster@pobox.com' --before="$i weeks ago" --after="$((i+1)) weeks ago" | awk '{print $NR}')
    all=$(git rev-list --all --count --before="$i weeks ago" --after="$((i+1)) weeks ago")
    echo "$gitster/$all" | bc -l | cut -c1-3                                                            
done 
