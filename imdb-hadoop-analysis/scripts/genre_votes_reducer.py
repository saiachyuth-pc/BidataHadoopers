#!/usr/bin/env python3
import sys
from collections import defaultdict

genre_votes = defaultdict(int)

for line in sys.stdin:
    try:
        genre, votes = line.strip().split('\t')
        genre_votes[genre] += int(votes)
    except:
        continue

for genre, votes in sorted(genre_votes.items(), key=lambda x: x[1], reverse=True):
    print(f"{genre}\t{votes}")
