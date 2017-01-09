#!/usr/bin/env python3

"""Main function"""

import sys

import hparser
import options.generate

def main():
    """Main function."""
    options.generate.create()


if __name__ == "__main__":
    if not sys.version_info >= (3,):
        raise Exception("Only Python 3 is supported.")
    main()
