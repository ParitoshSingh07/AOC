# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")

from functools import reduce
from utils import get_actual
string = get_actual(day=3, year=2022)
with open("input.txt") as f:
    contents = f.read().strip()

contents = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()

common = []

# for line in contents.split("\n"):
#     vals = [item for item in line[:len(line)//2] if item in line[len(line)//2:]]
#     common.append(list(set(vals))[0])
    
# res = [ord(val) - ord("a") + 1 if val.islower() else ord(val) - ord("A") + 27 for val in common]

# print(sum(res))

lines = contents.split("\n")
for idx in range(0, len(lines), 3):
    line_group = lines[idx: idx + 3]
    common_item = list(reduce(set.intersection, map(set, line_group)))
    common.append(common_item[0])
    
res = [ord(val) - ord("a") + 1 if val.islower() else ord(val) - ord("A") + 27 for val in common]

print(sum(res))