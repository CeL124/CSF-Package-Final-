"""
Functions to format the SVHN data.
Contains:
    - Function to change dimensions for different frameworks requirements.
    - Function to change the amount of data used.
    - Function to one hot encode the labels.
"""
import numpy as np


def change_dim(x_data, framework="tensorflow"):
    # change image dimension to specified framework
    if framework == "pytorch" or framework == "caffe":
        # [h, w, channel, num_images] --> [num_images,channel, h, w]
        x_new_data = x_data.transpose(3, 2, 0, 1)
    elif framework == "tensorflow" or framework == "keras":
        # [h, w, channel, num_images] --> [num_images, h, w, channel]
        x_new_data = x_data.transpose(3, 0, 1, 2)
    else:
        print("change_dim only takes pytorch, caffe, keras, or tensorflow")

    print('dimension for ' + str(framework) + ': ' + str(x_new_data.shape))
    print('--' * 12)
    return x_new_data


def change_range(range_num, x_array, y_array):
    x_array = x_array[:range_num, ]
    y_array = y_array[:range_num, ]
    print('\nData range has been changed. New shape below')
    print('--' * 10)
    print("New shape for x " + str(x_array.shape))
    print('--' * 10)
    print("New shape for y " + str(y_array.shape))
    print('**'*12)
    return x_array, y_array


def onehot_encoder(y):
    y = y.flatten()
    y = (np.arange(10) == y[:, np.newaxis]).astype(np.float32)
    return y


def svhn_max_min(x):
    x = x/255
    return x
