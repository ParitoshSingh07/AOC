# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")

from utils import get_actual

contents = get_actual(day=9, year=2022)

contents = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""[1:]


pos_head = pos_tail = 0, 0

def move_tail_to(pos_head, pos_tail):
    if abs(pos_head[0] - pos_tail[0]) <= 1 and abs(pos_head[1] - pos_tail[1]) <= 1:
        return pos_tail
    if abs(pos_head[0] - pos_tail[0]) == 0:
        assert abs(pos_head[1] - pos_tail[1]) == 2
        if (pos_head[1] - pos_tail[1]) == 2:
            new_pos_tail = pos_tail[0], pos_tail[1] + 1
        else:
            new_pos_tail = pos_tail[0], pos_tail[1] - 1
    elif abs(pos_head[1] - pos_tail[1]) == 0:
        assert abs(pos_head[0] - pos_tail[0]) == 2
        if (pos_head[0] - pos_tail[0]) == 2:
            new_pos_tail = pos_tail[0] + 1, pos_tail[1]
        else:
            new_pos_tail = pos_tail[0] - 1, pos_tail[1]
    else:
        print("diagonal", pos_head, pos_tail)
        x, y = pos_tail
        if pos_head[0] > pos_tail[0]:
            x += 1
        else:
            x -= 1
        if pos_head[1] > pos_tail[1]:
            y += 1
        else:
            y -= 1
        new_pos_tail = x, y
    return new_pos_tail

locations_tail = [pos_tail]
for line in contents.strip().split("\n"):
    direction, count = line.split()
    count = int(count)
    for _ in range(count):
        if direction == "U":
            pos_head = pos_head[0], pos_head[1] - 1
        elif direction == "D":
            pos_head = pos_head[0], pos_head[1] + 1
        elif direction == "L":
            pos_head = pos_head[0] - 1, pos_head[1]
        elif direction == "R":
            pos_head = pos_head[0] + 1, pos_head[1]
        else:
            print("bad", direction)
        pos_tail = move_tail_to(pos_head, pos_tail)
        locations_tail.append(pos_tail)
        
print(len(set(locations_tail)))
