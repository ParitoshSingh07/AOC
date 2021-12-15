# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

contents = """
16,1,2,0,4,2,7,1,2,14
""".strip()

# Part 1
pos = list(map(int, contents.split(",")))

minimum = min(pos)
maximum = max(pos)

results = {}
for i in range(minimum, maximum + 1):
    fuel = sum(abs(i - p) for p in pos)
    results[i] = fuel


print(min(results.items(), key=lambda x: x[1]))

# part 2
pos = list(map(int, contents.split(",")))

minimum = min(pos)
maximum = max(pos)

results = {}
for i in range(minimum, maximum + 1):
    fuel = sum((abs(i - p) * (abs(i - p) + 1) / 2) for p in pos)
    results[i] = fuel


print(min(results.items(), key=lambda x: x[1]))