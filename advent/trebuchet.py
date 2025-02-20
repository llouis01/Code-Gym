# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:54:57 2023

@author: RoiMinuit
"""

## puzzle one of advent of code
import re
fname = 'puzzle1.txt'

def trebuchet(fname):
    # open, read, and close
    with open(fname, 'r') as f:
        lines = f.readlines()

    # obtain clean records of numbers
    nums = []
    for line in lines:
        nums.append(re.findall('\d', line))
        for sublist in nums:
            for element in sublist:
                element = int(element) if element.isdigit() else 0
    
    # process values for addition
    clean = []
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

with open('puzzle1.txt', 'r') as f:
    lines = f.readlines()

# extract lines
clean2 = []
for line in lines:
    clean2.append(re.findall(digits, line))

# isolate champ nums
clean3 = []
for sublist in clean2:
    if len(sublist) == 1:
        for element in sublist:
                clean3.append(element)
    elif len(sublist) > 1:
        clean3.append(sublist[0] + sublist[-1])
        
# trim numbers down to two digits
num_dict[re.findall('[a-z]+', clean3[-1])[0]]
match = re.search('[a-z]+', clean3[-1])

for sub in clean3:
    match = re.search('[a-z]+', sub)
    if match == None:
        pass
    else:
        re.sub(match[0], num_dict[match[0]], sub)
        # won't convert