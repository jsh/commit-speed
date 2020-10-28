#!/usr/bin/env python3
"""Plot regression of total commits against week number."""

import sys

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import scipy.stats  # type: ignore


def lineplot(week, commits):
    """Plot commits against week."""
    slope, intercept, rvalue, pvalue, stderr = scipy.stats.linregress(week, commits)
    line = (
        f"Regression line: y={slope:.2f}x+{intercept:.2f}, "
        f"r^2={rvalue**2:.2f}, p={pvalue:.2f}, e={stderr:.2f}"
    )
    plt.style.use("ggplot")
    _, axes = plt.subplots()
    axes.plot(week, commits, linewidth=0, marker=".", label="observed")
    axes.plot(week, intercept + slope * week, label=line)
    axes.set_xlabel("week")
    axes.set_ylabel("commits")
    axes.legend(facecolor="white")
    plt.show()


def main():
    """The big tent."""
    with open(sys.argv[1]) as fin:
        total_commits = [int(line.rstrip("\n")) for line in fin]
    week = np.arange(0, len(total_commits))
    commits = np.array(total_commits)
    lineplot(week, commits)


if __name__ == "__main__":
    main()
