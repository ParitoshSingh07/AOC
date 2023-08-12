# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
# from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

contents = """
A Y
B X
C Z
""".strip()

vals = {"X": 1,
        "Y": 2,
        "Z": 3}
vals_l = {"A": 1,
        "B": 2,
        "C": 3}
# total_result = 0
# for row in contents.split("\n"):
#     l, r = row.split()
#     result = vals[r]
#     print(vals_l[l], vals[r])
#     if vals_l[l] == vals[r]:
#         result += 3
#     elif (vals_l[l] % 3) + 1 == vals[r]:
#         result += 6
#     else:
#         pass
#     total_result += result


total_result = 0
for row in contents.split("\n"):
    l, r = row.split()
    if r == "Y":
        result = vals_l[l] + 3
    elif r == "Z":
        result = (vals_l[l] % 3) + 1 + 6
    else:
        result = vals_l[l] - 1
        if result == 0:
            result += 3
    total_result += result
print(total_result)