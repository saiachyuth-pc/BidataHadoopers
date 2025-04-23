#!/usr/bin/env python3
import sys
from collections import defaultdict

trend_map = defaultdict(list)

for line in sys.stdin:
    try:
        key, rating = line.strip().split("\t")
        trend_map[key].append(float(rating))
    except:
        continue

for key in sorted(trend_map.keys()):
    ratings = trend_map[key]
    avg = sum(ratings) / len(ratings)
    print(f"{key}\t{avg:.2f}")

