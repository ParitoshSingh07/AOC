# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:46:16 2021

@author: paritoshsingh1
"""

import collections
from itertools import islice

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

sample_input = """
199
200
208
210
200
207
240
269
260
263
"""

with open("input.txt") as f:
    contents = f.read().strip()
    
ints_list = [int(item) for item in contents.strip().split()]

# part 1
res = [(r > l) for (l, r) in sliding_window(ints_list, 2)]
print(sum(res))

# part 2

window_sums = [sum(window) for window in sliding_window(ints_list, 3)]
res = [(r > l) for (l, r) in sliding_window(window_sums, 2)]
print(sum(res))