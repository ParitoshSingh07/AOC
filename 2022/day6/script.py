# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")

from utils import get_actual

contents = get_actual(day=6, year=2022)

contents = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""[1:]


for idx in range(len(contents)):
    if len(set(contents[idx: idx + 14])) == 14:
        break

print(idx + 14)