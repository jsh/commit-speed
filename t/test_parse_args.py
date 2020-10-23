#!/usr/bin/env python3
"""Test parse_args module.

Modeled on https://bit.ly/35u38gV
"""

import os

from parse_args import parse_args


def test_parse_args_defaults() -> None:
    """parse_args defaults."""
    parser = parse_args()
    assert not parser.verbose
    assert not parser.cumulative
    assert parser.repo == os.getcwd()


def test_verbose() -> None:
    """parse_args understands --verbose."""
    parser = parse_args(["--verbose"])
    assert parser.verbose


def test_cumulative() -> None:
    """parse_args understands --cumulative."""
    parser = parse_args(["--cumulative"])
    assert parser.cumulative


def test_repository() -> None:
    """parse_args understands --repo."""
    parser = parse_args(["--repo", "man"])
    assert parser.repo == "man"


def test_help() -> None:
    """Test help which throws a SystemExit."""
    # TODO: How do I do this?
