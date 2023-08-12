# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")

from utils import get_actual

contents = get_actual(day=4, year=2022)


contents = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""[1:]
lines = contents[:-1].split("\n")


count = 0
for line in lines:
    l, r = line.split(",")
    ls, le = map(int, l.split("-"))
    rs, re = map(int, r.split("-"))
    if re - rs > le - ls:
        ls, le, rs, re = rs, re, ls, le
    if (le >= rs and ls <= re):
        count += 1

print(count)