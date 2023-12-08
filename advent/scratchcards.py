# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:39 2023

@author: RoiMinuit
"""

import re
import pandas as pd
fname = "puzzle4.txt"

# import text data
def scratchcard(fname):
    with open(fname, 'r') as f:
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
    hand = []
    for lst in clean:
        x = [int(i) for i in lst if i]
        if len(x) < 25:
            win.append(x)
        else:
            hand.append(x)
    return win, hand


## get scores
win, hand = scratchcard(fname)

# create df
cards = ['card_' + str(i) for i in range(1, len(win) + 1)]
data = {'cards': cards, 'win':win, 'play':hand}
df = pd.DataFrame(data)

# intersect
inter = []
for i in range(0, len(df)):
    sett = list(set(df.win[i]) & set(df.play[i]))
    inter.append(sett)
    
# append to df
df['sets'] = inter

# score
def get_scores(col):
    scores = []
    for element in df[col]:
        if len(element) < 1:
            x = 0
        elif len(element) == 1:
            x = 1
        elif len(element) == 2:
            x = 2
        else:
            x = 1 * (2 ** (len(element) - 1))
        scores.append(x)
    return scores

# append to df
df['scores'] = get_scores('sets')
print(f'Sum of scores: {sum(df.scores)}')
