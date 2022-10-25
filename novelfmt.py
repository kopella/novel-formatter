#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys


def main(argv):
    parser = _BuildParser()
    args = parser.parse_args(argv[1:])
    files = args.files
    style = args.style
    if not files:
        parser.error('no destiny.')
    if not style:
      # TODO: Add default style.
        parser.error('no style.')
    FormatFiles(files, style)

    return 0


def FormatFiles(files, style):
    for filenames in files:
        _FormatFile(filenames, style)


def _FormatFile(filenames, style):
    pass


def _BuildParser():
    parser = argparse.ArgumentParser(
        prog='novelfmt', description='Formatter for Novel.')

    parser.add_argument(
        'files', nargs='*', help='reads from stdin.')

    parser.add_argument(
        '--style',
        action='store',
        help=('specify formatting style: either a style name, or the name of a file with style settings.'))

    return parser


if __name__ == "__main__":
    sys.exit(main(sys.argv))
