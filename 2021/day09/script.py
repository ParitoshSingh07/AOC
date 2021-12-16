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
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


# Part 1
grid = [[int(point) for point in line] for line in contents.split("\n")]

rangex = len(grid)
rangey = len(grid[0])

def get_neighbours(x, y, rangex, rangey):
    if x + 1 < rangex:
        yield x + 1, y
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < rangey:
        yield x, y + 1
    if y - 1 >= 0:
        yield x, y - 1

low_point = []
for x in range(rangex):
    for y in range(rangey):
        point = grid[x][y]
        if all(grid[x][y] > point for x, y in get_neighbours(x, y, rangex, rangey)):
            low_point.append(point)

risk = sum([point + 1 for point in low_point])
