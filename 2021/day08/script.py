# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
sys.path.append(r"..")
from day01.day01 import sliding_window

with open("input.txt") as f:
    contents = f.read().strip()

# contents = """
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# """.strip()

digit_mapping = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

reverse_digit_mapping = {v: k for k, v in digit_mapping.items()}
num_letters_used = {}
for k, v in digit_mapping.items():
    num_letters_used.setdefault(len(v), []).append(k)

single_length_letters = {k: v for k, v in num_letters_used.items() if len(v) == 1}


# Part 1
total_single_digit_counts = 0
for line in contents.split("\n"):
    front, last = line.split(" | ")
    output_group = last.split(" ")
    for item in output_group:
        if len(item) in single_length_letters:
            total_single_digit_counts += 1
print(total_single_digit_counts)

# Part 2
from itertools import product
meta_keys = []
for line in contents.split("\n"):
    mapping_fixer = {k: set("abcdefg") for k in "abcdefg"}
    front, last = line.split(" | ")
    output_group = front.split(" ") + last.split(" ")
    for item in output_group:
        map_set = set("".join(digit_mapping[k] for k in num_letters_used[len(item)]))
        for letter in item:
            mapping_fixer[letter] =  mapping_fixer[letter].intersection(map_set)
    # mapping done
    for possibility in product(*mapping_fixer.values()):
        if len(set(possibility)) < len(possibility):
            continue # skip bad cases
        fixed_map = dict(zip("abcdefg", possibility))
        good_case = True
        for item in output_group:
            fixed_digit = "".join(sorted(fixed_map[letter] for letter in item))
            if fixed_digit not in [digit_mapping[k] for k in num_letters_used[len(item)]]:
                good_case = False
                break
        if good_case:
            print(fixed_map)
            meta_keys.append((last.split(" "), fixed_map))
            break

total = 0
for last, fixed_map in meta_keys:
    stuff = ["".join(sorted(fixed_map[letter] for letter in item)) for item in last]
    res = int("".join(map(str, (reverse_digit_mapping[item] for item in stuff))))
    total += res

print(total)
