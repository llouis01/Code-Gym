# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:43:06 2024

@author: RoiMinuit
"""

import os
import pandas as pd

path = 'C:\\Users\\RoiMinuit\\Desktop\\data\\switrs_raw_csvs'

# find folders
folders = []
for folder in os.listdir(path):
    folder = os.path.join(path, folder)
    folders.append(folder)
    
# collect data from each folder
all_data = []
for folder in folders:
    for f in os.listdir(folder):
        if f.endswith('CollisionRecords.txt'):
            all_data.append(os.path.join(folder, f))
            
# check shape in each file
for file in all_data:
    df = pd.read_csv(file, low_memory=False)
    print(df.shape)
    
# Not fast at all :D