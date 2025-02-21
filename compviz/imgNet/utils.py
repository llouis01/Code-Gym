""" Utils for importing images and data """

## library imports
import os
import cv2
import time
import random
import numpy as np
import matplotlib.pyplot as plt

## func to import train images
def import_train(img_dir, img_num=int):
    # libs
    import time
    """ Import images from the specified directory """
    start = time.time()
    processed_images = []
    img_paths = []
    labels = []

    def process_image_batches(img_paths, processed_images, img_num, labels):
        """ Import images from the specified directory """
    
        # build label set
        for i in range(0, img_num):
            img_path = img_paths[i]
            # label is the parent folder of current image
            label = img_path.split(os.path.sep)[-2]
            labels.append(label)
        
        # read in image, resize, grayscale, and normalize
        for i in range(0, img_num):
            img_path = cv2.imread(img_paths[i])
            img = cv2.resize(img_path, (64, 64))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = np.expand_dims(img, axis = 2)
            img = img / 255.0
            processed_images.append(img)
            completed_percentage = (i / img_num) * 100
            if completed_percentage in [25, 50, 75, 100]:
                print(f"Images processed: {i} ({round(completed_percentage)}%)")

    # collect image paths
    for root, dirs, files in os.walk(img_dir):
            for file in files:
                if file.endswith(".JPEG"):
                     img_paths.append(os.path.join(root, file))

    # shuffle images to get random images from random folders and process while generating labels
    random.shuffle(img_paths)
    process_image_batches(img_paths, processed_images, img_num, labels)

    # return run stats and data        
    end = time.time()
    print(f"Function processed {img_dir} in {round(end - start)} seconds.\n")
    return processed_images, labels


## func to import test and val images
def import_others(img_dir, img_num=int):
    """ Import images from the specified directory """
    start = time.time()
    processed_images = []
    img_paths = []

    def process_image_batches(img_paths, processed_images, img_num):
        """ Import images from the specified directory """

        # read in image, resize, grayscale, and normalize
        for i in range(0, img_num):
            img_path = cv2.imread(img_paths[i])
            img = cv2.resize(img_path, (224, 224))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = np.expand_dims(img, axis = 2)
            img = img / 255.0
            processed_images.append(img)
            completed_percentage = (i / img_num) * 100
            if completed_percentage in [25, 50, 75, 100]:
                print(f"Images processed: {i} ({round(completed_percentage)}%)")

    # collect image paths
    for root, dirs, files in os.walk(img_dir):
            for file in files:
                if file.endswith(".JPEG"):
                     img_paths.append(os.path.join(root, file))

    # shuffle images to get random images from random folders and process while generating labels
    random.shuffle(img_paths)
    process_image_batches(img_paths, processed_images, img_num)

    # return run stats and data        
    end = time.time()
    print(f"Function processed {img_dir} in {round(end - start)} seconds.\n")
    return processed_images


## func to view training images with their assigned labels
def view_train_images(x, y, n = 5):
    """ view train data """
    for img in range(0, 5):
        plt.imshow(x[img], cmap="gray")
        plt.show()
        print(y[img])


## func to get data for CV project
# def get_images(train_dir, val_dir, test_dir, train_num = int):
#     """ Get data for CV project """
#     x_train, y_train = import_train(train_dir, train_num)
#     x_val, y_val = import_train(val_dir, ((.15 * train_num)))
#     x_test, y_test = import_train(test_dir, (.15 * train_num))
#     return x_train, y_train, x_val, y_val, x_test, y_test