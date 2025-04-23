#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # skip header

for row in reader:
    try:
        year = row[2].strip()
        genres = row[5].strip()
        rating = float(row[6].strip())

        if not year.isdigit():
            continue

        for genre in genres.split(','):
            print(f"{year},{genre.strip()}\t{rating}")
    except:
        continue
