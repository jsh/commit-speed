#!/usr/bin/env python3
"""Argument handling."""

import argparse
import os
import sys
from typing import List, Optional


def parse_args(args: Optional[List] = None) -> argparse.Namespace:
    """Parse the args
    :param str description: description message for executable
    :param list or None args: the argument list to parse
    :returns: the args, massaged and sanity-checked
    :rtype: argparse.Namespace

    When this finishes we return a Namespace that has these attributes
      - verbose: how chatty to be (bool)
      - cumulative: from beginning instead of just for the week.
      - repo: which repo to survey
    """

    parser = argparse.ArgumentParser(description="Report weekly commits.")

    parser.add_argument("--verbose", help="be extra chatty", action="store_true")
    parser.add_argument(
        "--repo", help="which repository to survey", default=os.getcwd()
    )
    parser.add_argument(
        "--cumulative",
        help="cumulative commits from repo creation",
        action="store_true",
    )

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    # attribute validatation and enhancement

    return parsed_args
