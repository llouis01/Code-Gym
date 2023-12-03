# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:54:57 2023

@author: RoiMinuit
"""

## puzzle one of advent of code
# imports
import re

def trebuchet(fname):
    # open, read, and close
    with open(fname, 'r') as f:
        lines = f.readlines()

    # obtain clean records of numbers
    nums = []
    clean = []
    for line in lines:
        nums.append(re.findall('\d', line))
        for sublist in nums:
            for element in sublist:
                element = int(element) if element.isdigit() else 0
    
    # process values for addition
    for sublist in nums:
        if len(sublist) == 1:
            for element in sublist:
                if int(element) < 10:
                    clean.append(int(element) * 11)
        elif len(sublist) > 1:
                clean.append(int(sublist[0] + sublist[-1]))
    return sum(clean)

# print(f"The calibration value is {trebuchet('puzzle1.txt')}.")


## part II

digits = r"one|two|three|four|five|six|seven|eight|nine|\d+"
num_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
            'seven':7, 'eight':8, 'nine':9}
clean2 = []
clean3 = []

with open('puzzle1.txt', 'r') as f:
    lines = f.readlines()
    
for line in lines:
    clean2.append(re.findall(digits, line))
    for sublist in clean2:
        for element in sublist:
            element = int(element) if element.isdigit() else num_dict[element]