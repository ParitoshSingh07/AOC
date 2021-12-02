# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:52:56 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"C:\paritosh\playground\AOC\AOC\2021")
import os
os.chdir(r"C:\paritosh\playground\AOC\AOC\2021\day02")
from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

# contents = """
# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# """.strip()
# part 1
x, y = 0, 0
for line in contents.split("\n"):
    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        x += value
    elif command == "up":
        y -= value
    elif command == "down":
        y += value
    else:
        raise ValueError(f"Bad command {command}")

# part 2
x, y = 0, 0
aim = 0
for line in contents.split("\n"):
    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        x += value
        y += aim * value
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value
    else:
        raise ValueError(f"Bad command {command}")

print(x , y)
print(x * y)
