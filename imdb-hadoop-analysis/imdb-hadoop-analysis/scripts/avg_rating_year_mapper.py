#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)
for row in reader:
    try:
        year = row[2]
        rating = float(row[6])
        if year and rating:
            print(f"{year}\t{rating}")
    except:
        continue
