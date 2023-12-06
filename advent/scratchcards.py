# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:39 2023

@author: RoiMinuit
"""

import re

# import text data
with open("puzzle4.txt", 'r') as f:
    lines = f.readlines()
    
# extract data
data = []
win = {}
played = {}
for line in lines:
    x = re.sub('Card +\d+: ', "", line).strip()
    x = re.sub("  ", " ", x)
    x = re.sub("\|", ",", x)
    data.append(x.strip())

clean = []
for sublist in data:
    for element in sublist:
        neat = element.split(" | ")
        clean.append(neat)
        # for w, p in neat:
        #     win.add(neat.split("|")[w])
        #     played.add(neat.split("|")[p])