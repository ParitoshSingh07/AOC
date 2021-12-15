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
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()

# Part 1
points = []
for line in contents.split("\n"):
    start, end = line.split(" -> ")
    start = tuple(map(int, start.split(",")))
    end = tuple(map(int, end.split(",")))
    if start[0] == end[0]:
        minimum, maximum = sorted([start[1], end[1]])
        for i in range(minimum, maximum + 1):
            points.append((start[0], i))
    elif start[1] == end[1]:
        minimum, maximum = sorted([start[0], end[0]])
        for i in range(minimum, maximum + 1):
            points.append((i, start[1]))
    else:
        pass

from collections import Counter

c = Counter(points)

print(len([p for p, count in c.items() if count >=2]))

# part 2

points = []
for line in contents.split("\n"):
    start, end = line.split(" -> ")
    start = tuple(map(int, start.split(",")))
    end = tuple(map(int, end.split(",")))
    if start[0] == end[0]:
        minimum, maximum = sorted([start[1], end[1]])
        for i in range(minimum, maximum + 1):
            points.append((start[0], i))
    elif start[1] == end[1]:
        minimum, maximum = sorted([start[0], end[0]])
        for i in range(minimum, maximum + 1):
            points.append((i, start[1]))
    else: # 45% diagonal
        if end[0] > start[0]:
            x_sign = +1
        else:
            x_sign = -1
        if end[1] > start[1]:
            y_sign = +1
        else:
            y_sign = -1
        for (idx, x) in enumerate(range(start[0], end[0] + x_sign, x_sign)):
            points.append((x, start[1] + y_sign * idx))

from collections import Counter

c = Counter(points)

print(len([p for p, count in c.items() if count >=2]))