# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
sys.path.append(r"../..")
import numpy as np
from utils import get_actual

contents = get_actual(day=8, year=2022)

contents = """
30373
25512
65332
33549
35390
"""[1:]

val = [list(map(int, row)) for row in contents.strip().split("\n")]

arr = np.array(val)

# tops
maxes = np.maximum.accumulate(arr)
to_compare = np.zeros_like(maxes)
to_compare[0] = to_compare[0] - 1
to_compare[1:] = maxes[:-1]

tops = (to_compare < arr).astype(int)


# lefts
maxes = np.maximum.accumulate(arr, axis=1)
to_compare = np.zeros_like(maxes)
to_compare[:, 0] = to_compare[:, 0] - 1
to_compare[:, 1:] = maxes[:, :-1]
lefts = (to_compare < arr).astype(int)

# bottoms
rev_arr = arr[::-1]
maxes = np.maximum.accumulate(rev_arr)
to_compare = np.zeros_like(maxes)
to_compare[0] = to_compare[0] - 1
to_compare[1:] = maxes[:-1]

bottoms = (to_compare < rev_arr).astype(int)[::-1]

# rights
flipped_arr = arr[:, ::-1]
maxes = np.maximum.accumulate(flipped_arr, axis=1)
to_compare = np.zeros_like(maxes)
to_compare[:, 0] = to_compare[:, 0] - 1
to_compare[:, 1:] = maxes[:, :-1]
rights = (to_compare < flipped_arr).astype(int)[:, ::-1]


np.sum(((tops + lefts + bottoms + rights) > 0).astype(int))
