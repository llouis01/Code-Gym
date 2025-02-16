# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:01:41 2025

@author: RoiMinuit
"""

# Import libraries
import os
import random
import time
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt


# paths for data and processed images

train_dir = "C:/Users/RoiMinuit/Desktop/data/ILSVRC/Data/CLS-LOC/train"
test_dir = "C:/Users/RoiMinuit/Desktop/data/ILSVRC/Data/CLS-LOC/val"
val_dir = "C:/Users/RoiMinuit/Desktop/data/ILSVRC/Data/CLS-LOC/test"

train_images, test_images, val_images = [], [], []


# funcs to import images

def process_image_batches(img_paths, processed_images):
    """ Import images from the specified directory """
    
    for img_path in img_paths:
        with Image.open(img_path) as img:
            processed_images.append(img.copy())
            img.close()

def import_and_process_images(img_dir, batch_size = int):
    """ Import images from the specified directory """
    start = time.time()
    processed_images = []
    img_paths = []

    for root, dirs, files in os.walk(img_dir):
            for file in files:
                if file.endswith(".JPEG"):
                     img_paths.append(os.path.join(root, file))

                     if len(img_paths) == batch_size:
                          random.shuffle(img_paths)
                          process_image_batches(img_paths, processed_images)
                          break
    #                       img_paths = []
                          
    # if img_paths:
    #     process_image_batches(img_paths, processed_images)
    end = time.time()
    print(f"The function took {end - start} seconds to run.")
    return processed_images


train_images = import_and_process_images(train_dir, batch_size = 20000)

# show 10 images

for i in range(0, 10):
    train_images[i].show()
