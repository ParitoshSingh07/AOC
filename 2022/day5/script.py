# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")
import re

from utils import get_actual

contents = get_actual(day=5, year=2022)

contents = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""[1:-1]


boxes = []

for line in contents.split("\n"):
    if "[" in line:
        row_items = []
        for idx in range(0, len(line), 4):
            row_items.append(line[idx + 1])
        boxes.append(row_items)
        


boxes_T = [[item for item in stack if item != " "] for stack in zip(*boxes)]

for line in contents.split("\n"):
    if "move" in line:
        m = re.match("move (\d+) from (\d+) to (\d+)", line)
        n, start, end = map(int, m.groups())
        to_move = boxes_T[start - 1][:n]
        boxes_T[start - 1] = boxes_T[start - 1][n:]
        boxes_T[end - 1] = to_move + boxes_T[end - 1]

print("".join(stack[0] for stack in boxes_T))
