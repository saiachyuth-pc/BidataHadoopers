#!/usr/bin/env python3
import sys

movies = []
for line in sys.stdin:
    try:
        movie, rating = line.strip().split('\t')
        rating = float(rating)
        movies.append((rating, movie))
    except:
        continue

for rating, movie in sorted(movies, reverse=True)[:10]:
    print(f"{movie}\t{rating}")
