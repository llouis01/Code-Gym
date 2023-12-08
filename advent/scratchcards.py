# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:39 2023

@author: RoiMinuit
"""

import re
import pandas as pd

# import text data
with open("puzzle4.txt", 'r') as f:
    lines = f.readlines()

# extract data
data = []
for line in lines:
    x = re.sub('Card +\d+: ', "", line).strip()
    x = re.sub("  ", " ", x)
    x = re.sub(" ", ", ", x)
    x = re.sub(",? +\| ?+,", " |", x)
    x = x.split("|")
    data.append(x)

clean = []
for sublist in range(0, len(data)):
    for element in range(0, 2):
        clean.append(re.findall('\d+', data[sublist][element]))
        

win = []
play = []
for lst in clean:
    if len(lst) < 25:
        win.append(lst)
    else:
        play.append(lst)

data = {'win':win, 'play':play}
df = pd.DataFrame(data)
print(df)

win2 = []
play2 = []
for listx in df.win:
    for el in listx:
        win2.append(int(el))
for listx in df.play:
    for el in listx:
        play2.append(int(el))