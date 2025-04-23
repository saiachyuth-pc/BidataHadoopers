#!/usr/bin/env python3
import sys
from collections import defaultdict

ratings = defaultdict(list)

for line in sys.stdin:
    try:
        year, rating = line.strip().split("\t")
        ratings[year].append(float(rating))
    except:
        continue

for year in sorted(ratings.keys()):
    rlist = ratings[year]
    avg = sum(rlist) / len(rlist)
    print(f"{year}\t{avg:.2f}")
