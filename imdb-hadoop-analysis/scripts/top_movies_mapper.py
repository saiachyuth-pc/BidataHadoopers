#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)
for row in reader:
    try:
        title = row[1]
        year = row[2]
        rating = float(row[6])
        print(f"{title} ({year})\t{rating}")
    except:
        continue

