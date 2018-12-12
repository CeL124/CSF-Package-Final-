"""
Functions to format the SVHN data.
Contains:
    - Function to change dimensions for tensorflow requirements
    - Function to change the amount of data used.
    - Function to one hot encode the labels.
"""
import numpy as np


def change_dim(x_data):

    # [h, w, channel, num_images] --> [num_images, h, w, channel]
    x_new_data = x_data.transpose(3, 0, 1, 2)

    print('Image dimensions changed: ' + str(x_new_data.shape))
    print('--' * 25)
    return x_new_data


def change_range(range_num, x_array, y_array):
    try:
        x_array_new = x_array[:range_num, ]
        y_array_new = y_array[:range_num, ]
        if range_num > len(x_array):
            print('Input range is larger than amount of data available\n')
        else:
            print('\nData range has been changed. New shape below')
            print('--' * 20)
            print("New shape for images " + str(x_array_new.shape))
            print('--' * 20)
            print("New shape for labels " + str(y_array_new.shape))
            print('**'*20)
        return x_array_new, y_array_new
    except ValueError:
        print('Please check Image Dimensions! Something is wrong there')


def onehot_encoder(y):
    y = y.flatten()
    y = (np.arange(10) == y[:, np.newaxis]).astype(np.float32)
    return y


def svhn_max_min(x):
    x = x/255
    return x
