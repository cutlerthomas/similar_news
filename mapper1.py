#!/bin/python3

import sys
import itertools
import json

all_sources = []


for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    else:
        all_sources.append(line)

    #format is <url>:::<content>
combs = itertools.combinations(all_sources, 2)
for comb in combs:
    pairing = {'A': comb[0], 'B': comb[1]}
    print(json.dumps(pairing))