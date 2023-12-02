# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:54:57 2023

@author: RoiMinuit
"""

# puzzle one of advent of code

def trebuchet(fname):
    # imports
    import re
    
    # open, read, and close
    with open('puzzle1.txt', 'r') as f:
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

print(f"The calibration value is {trebuchet('puzzle1.txt')}.")
