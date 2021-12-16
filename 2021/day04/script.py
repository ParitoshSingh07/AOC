# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"C:\paritosh\playground\AOC\AOC\2021")
import os
os.chdir(r"C:\paritosh\playground\AOC\AOC\2021\day04")
from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

# contents = """
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#   8  2 23  4 24
# 21  9 14 16  7
#   6 10  3 18  5
#   1 12 20 15 19

#   3 15  0  2 22
#   9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#   2  0 12  3  7
# """.strip()

import numpy as np
import re
contents_split = contents.split("\n")
numbers = [int(n) for n in contents.split("\n")[0].split(",")]

grids = [contents_split[idx: idx + 5] for idx in range(2, len(contents_split), 6)]
grid_ints = [[[int(item) for item in re.split("\s+", row.strip())] for row in grid] for grid in grids]

grid_arrs = [np.array(grid) for grid in grid_ints]
# part 1
for idx in range(len(numbers)):
    bingo_set = np.array(numbers[:idx + 1])
    for grid in grid_arrs:
        isin = np.isin(grid, bingo_set)
        if isin.all(axis=0).any() or isin.all(axis=1).any():
            print("bingo!", numbers[idx])
            print("unmarked score:",  grid[~isin].sum())
            print("ans:", grid[~isin].sum() * numbers[idx])
            break
    else:
        continue
    break
    
# part 2
won_boards = np.zeros(len(grid_arrs))
for idx in range(len(numbers)):
    bingo_set = np.array(numbers[:idx + 1])
    for board_idx, grid in enumerate(grid_arrs):
        isin = np.isin(grid, bingo_set)
        if isin.all(axis=0).any() or isin.all(axis=1).any():
            won_boards[board_idx] = 1
            if won_boards.all():
                print("bingo!", numbers[idx])
                print("unmarked score:",  grid[~isin].sum())
                print("ans:", grid[~isin].sum() * numbers[idx])
                break
    else:
        continue
    break
    