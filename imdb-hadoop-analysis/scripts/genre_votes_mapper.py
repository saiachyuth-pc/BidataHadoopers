#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)
for row in reader:
    try:
        genres = row[5].split(', ')
        votes = int(row[14])
        for genre in genres:
            print(f"{genre}\t{votes}")
    except:
        continue
