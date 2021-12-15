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

contents = """
3,4,3,1,2
""".strip()

# Part 1

# naive

fishes = list(map(int, contents.split(",")))
# fishes = [0]
for day in range(0, 80):
    new_fish = []
    for fish in fishes:
        if fish > 0:
            new_fish.append(fish - 1)
        else:
            new_fish.append(6)
            new_fish.append(8)
    fishes = new_fish

print(len(fishes))

# Part 2


fishes = [0]
results = {}
for day in range(0, 64):
    new_fish = []
    for fish in fishes:
        if fish > 0:
            new_fish.append(fish - 1)
        else:
            new_fish.append(6)
            new_fish.append(8)
    fishes = new_fish
    results[day] = fishes.copy()
count_fisher = {k: len(v) - 1 for k, v in results.items()} # because i want to count how many new fishes made, so -1


####

total_days = 256
remaining_days = total_days
look_forward = 0

fishes = list(map(int, contents.split(",")))

while remaining_days > 64:
    look_forward += 64
    remaining_days -= 64
    new_fish = []
    for fish in fishes:
        new_fish.extend(results[63 - fish])
    fishes = new_fish




current_fish_count = len(fishes)
for fish in fishes:
    try:
        current_fish_count += count_fisher[remaining_days -1 - fish]
    except KeyError:
        pass

print(current_fish_count)



### round 3, crazy logic
meta_result_dict = {}

for total_days in range(1, 256 + 1):
    remaining_days = total_days
    look_forward = 0
    
    fishes = [0]
    
    while remaining_days > 64:
        look_forward += 64
        remaining_days -= 64
        new_fish = []
        for fish in fishes:
            new_fish.extend(results[63 - fish])
        fishes = new_fish
    
    
    
    
    current_fish_count = len(fishes)
    for fish in fishes:
        try:
            current_fish_count += count_fisher[remaining_days -1 - fish]
        except KeyError:
            pass
    
    print(current_fish_count)
    meta_result_dict[total_days] = current_fish_count

fishes = list(map(int, contents.split(",")))
totals = 0
total_days = 256
for fish in fishes:
    totals += meta_result_dict[total_days - fish]

print(totals)


## part 2, actually effin good- credits https://github.com/spenpal2000/adventofcode/blob/main/2021/day6/day6.py
from collections import Counter
def part2(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)
    
    for day in range(256):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}
        
    return sum(fishes.values())

part2(list(map(int, contents.split(","))))
