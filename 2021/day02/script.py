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