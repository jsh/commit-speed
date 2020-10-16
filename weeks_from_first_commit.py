#!/usr/bin/env python3
"""Print weeks from first commit."""

from datetime import date
import shlex
import subprocess

latest_commit_date = date.today()
command = "git log --all --date='format:%F' --format='%cd' --reverse master"
completed_process = subprocess.run(
    shlex.split(command), capture_output=True, text=True, check=True
)
first_commit = completed_process.stdout.split("\n")[0]
first_commit_date = date.fromisoformat(first_commit)
result = (latest_commit_date - first_commit_date).days // 7 + 1  # just in case
print(result)
