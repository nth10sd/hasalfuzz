#!/usr/bin/env python3

"""Parser function"""

import argparse

def addParserOptions():
    """Add parser options."""
    parser = argparse.ArgumentParser(description="Usage: Don't use this directly")

    parser.add_argument('--enable-comments',
                        dest='enableComments',
                        action='store_true',
                        default=False,
                        help='Enables comments. Defaults to "%(default)s".')

    return parser


def parseOptions(inputArgs):
    """Return a 'sikuliOptions' object, which is intended to be immutable."""
    parser = addParserOptions()
    sikuliOptions = parser.parse_args(inputArgs.split())

    return sikuliOptions

if __name__ == "__main__":
    parser = addParserOptions()
    sikuliOptions = parser.parse_args()

    print("\nRunning this file directly doesn't do anything, but here's our subparser help:\n")
    parseOptions("--help")
