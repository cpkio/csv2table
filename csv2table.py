#!/usr/bin/env python3
"""
caption
header
"""

import argparse
import csv
import sys
import terminaltables

version = '0.2'


def main(args):
    data = list(csv.reader(args.infile))
    table = terminaltables.AsciiTable(data)
    table.inner_row_border = True
    if not args.noheader:
        table.CHAR_H_INNER_HORIZONTAL = '='
    if not args.caption:
        output = table.table
    else:
        output = ': {caption}\n\n{grid_table}'.format(
            caption=args.caption, grid_table=table.table)
    args.outfile.write(output)

parser = argparse.ArgumentParser()
parser.set_defaults(func=main)
# Args
parser.add_argument('--version', action='version', version=version)
parser.add_argument(
    '--caption', help='The caption in the title, which will be print as pandoc styled caption.')
parser.add_argument('--noheader', action='store_true',
                    help='If not specified, treat 1st row as header row.')
# IO
parser.add_argument('infile', nargs='?',
                    type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('outfile', nargs='?',
                    type=argparse.FileType('w'), default=sys.stdout)

if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
