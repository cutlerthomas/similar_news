#!/bin/python3

import sys
import json

def Jaccard(a,b):
    return len(a.intersection(b))/len(a.union(b))

for line in sys.stdin:
    pairing = json.loads(line)
    pairing['similarity'] = Jaccard(set(pairing['A']), set(pairing['B']))
    print(json.dumps(pairing))