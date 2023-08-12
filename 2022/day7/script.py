# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:26:03 2021

@author: paritoshsingh1
"""

import sys
from pathlib import Path
sys.path.append(r"..")
sys.path.append(r"../..")

from utils import get_actual

contents = get_actual(day=7, year=2022)

# contents = """
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """[1:]


file_structure = {}

groups = contents.split("$ ")

for group in groups:
    if not group.strip():
        continue
    if group.startswith("cd"):
        location = group[3:].strip()
        if location == "/":
            curr_path = Path("/")
        elif location == "..":
            curr_path = curr_path.parent
        else:
            curr_path = curr_path / location
        # print(curr_path, location)
    elif group.startswith("ls"):
        t = file_structure
        for part in curr_path.parts[:-1]:
            t = t[part]
        t[curr_path.parts[-1]] = {}
        t = t[curr_path.parts[-1]]
        lines = group.split("\n")[1:]
        for line in lines:
            if not line.strip():
                continue
            if line.startswith("dir"):
                continue # im not creating empty folder atm. why? heck if i know
            size, name = line.split()
            size = int(size)
            t[name] = size


def get_directories(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield k
            yield from get_directories(v)

directories = list(get_directories(file_structure))

sizes = {}
def get_dir_sizes(d, keys=None):
    if keys == None:
        keys = []
    for k, v in d.items():
        if isinstance(v, dict):
            keys.append(k)
            sizes[tuple(keys)] = 0
            get_dir_sizes(v, list(keys))
            keys = keys[:-1]
        else:
            for idx in range(len(keys)):
                sizes[tuple(keys[:idx + 1])] += v

get_dir_sizes(file_structure)


print(sum(v for k, v in sizes.items() if v<=100000))


total = 70000000
needed_unused = 30000000

current = sizes[("\\",)]
to_free = current - (total - needed_unused)

print(min(v for v in sizes.values() if v >= to_free))
    

# seen = set()
# def all_nums(d):
#     for k, v in d.items():
#         if k not in seen:
#             seen.add(k)
#         else:
#             print("oh shit", k)
#         if isinstance(v, dict):
#             yield from all_nums(v)
#         else:
#             yield v

# res = sum(all_nums(file_structure))
