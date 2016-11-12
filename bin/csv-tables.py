#!/usr/bin/env python3

"""
Panflute filter to parse CSV in fenced YAML code blocks
"""

import io
import csv
import panflute as pf


def fenced_action(options, data, element, doc):
    # We'll only run this for CodeBlock elements of class 'csv'
    title = options.get('title', 'Untitled Table')
    title = [pf.Str(title)]
    has_header = options.get('has-header', False)

    with io.StringIO(data) as f:
        reader = csv.reader(f)
        body = []
        for row in reader:
            cells = [pf.TableCell(pf.Plain(pf.Str(x))) for x in row]
            body.append(pf.TableRow(*cells))

    header = body.pop(0) if has_header else None
    table = pf.Table(*body, header=header, caption=title)
    return table


if __name__ == '__main__':
    pf.toJSONFilter(pf.yaml_filter, tag='csv', function=fenced_action)
