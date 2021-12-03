# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"C:\paritosh\playground\AOC\AOC\2021")
import os
os.chdir(r"C:\paritosh\playground\AOC\AOC\2021\day03")
from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

# contents = """
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# """.strip()


temp = contents.split("\n")


items = list(zip(*temp))

from collections import Counter

all_most_common = []
all_least_common = []
for row in items:
    counts = Counter(row)
    most_common = counts.most_common(1)[0][0]
    least_common = sorted([k for k in counts], key= lambda k: (counts[k]))[0]
    all_most_common.append(most_common)
    all_least_common.append(least_common)


gamma = int("".join(all_most_common), 2)
epsilon = int("".join(all_least_common), 2)

print(gamma * epsilon)




oxygen_items = items.copy()
co2_items = items.copy()
for row_idx in range(len(items)):
    oxygen_row = oxygen_items[row_idx]
    co2_row = co2_items[row_idx]
    oxygen_counts = Counter(oxygen_row)
    co2_counts = Counter(co2_row)
    oxygen_bit = "1"
    co2_bit = "0"
    if oxygen_counts['0'] > oxygen_counts['1']:
        oxygen_bit = "0"

    if co2_counts['0'] < co2_counts['1']:
        co2_bit = "1"

    oxygen_idx = set(idx for idx, val in enumerate(oxygen_row) if val == oxygen_bit)
    oxygen_items = list(zip(*[col for (idx, col) in enumerate(zip(*items)) if idx in oxygen_idx]))
    co2_idx = set(idx for idx, val in enumerate(co2_row) if val == co2_bit)
    co2_items = list(zip(*[col for (idx, col) in enumerate(zip(*items)) if idx in co2_idx]))


    



import numpy as np
arr = np.array(items).astype(int).T
for idx in range(arr.shape[1]):
    zeros = (arr[:, idx] == 0).sum()
    if zeros > len(arr) / 2:
        oxygen_bit = 0
    else:
        oxygen_bit = 1
    arr = arr[arr[:, idx] == oxygen_bit]
    if len(arr) == 1:
        break

oxygen = int("".join(arr[0].astype(str)), 2)


arr = np.array(items).astype(int).T
for idx in range(arr.shape[1]):
    zeros = (arr[:, idx] == 0).sum()
    if zeros <= len(arr) / 2:
        bit = 0
    else:
        bit = 1
    arr = arr[arr[:, idx] == bit]
    if len(arr) == 1:
        break

co2 = int("".join(arr[0].astype(str)), 2)


print(oxygen * co2)

