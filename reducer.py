#!/bin/python3
import sys
from collections import defaultdict


articles_by_source = defaultdict(list)

for line in sys.stdin:
    if line.strip():
        try:
            source, content = line.strip().split(':::', 1)
            articles_by_source[source].append(content)
        except ValueError:
            continue

for source, contents in articles_by_source.items():
    combined_content = ' '.join(contents)
    print(f"{source}:::{combined_content}")