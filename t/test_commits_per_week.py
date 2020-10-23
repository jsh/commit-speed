#!/usr/bin/env python3
"""Test commits_per_week.
"""

from commits_per_week import cums


def test_cums() -> None:
    """cums sums correctly"""
    assert cums([]) == []
    assert cums([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
