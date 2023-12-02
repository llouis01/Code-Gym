# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:54:57 2023

@author: RoiMinuit
"""

import re

# open, read, and close
with open('puzzle1.txt', 'r') as f:
    lines = f.readlines()

# obtain clean records of numbers
get = []
for line in lines:
    get.append(re.findall('\d*', line))
    for listx in get:
        for element in listx:
            if element == '':
                listx.remove(element)
                
def trebuchet(data):
    