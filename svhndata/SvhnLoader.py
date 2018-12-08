"""
CLASS to get SVHN training and Testing data.
"""
import wget # get file from url
import os
import scipy.io as sio # To load the matlabfiles
import numpy as np


class SvhnData:
    def __init__(self):
        self.directory = 'data-Svhn'
        self.file_list = ['train_32x32.mat', 'test_32x32.mat' , 'extra_32x32.mat']
        self.trainData = None
        self.testData = None
        self.validationData = None
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.extraImages = None
        self.extraLabels = None

    # get data from website and load it into a directory
    def load_data(self):
        # try Creating directory data-Svhn. Catch if already exists
        print('checking if directory exists...')
        try:
            os.mkdir(self.directory)
            print('\ndirectory ' + self.directory + ' is being created..')
        except FileExistsError:
            print('directory ' + self.directory + ' already exists.')

        print('\nChecking if data files exist...')

        for file in self.file_list:
            file_path = './'+self.directory+'/' + file
            if not os.path.exists(file_path):
                url = 'http://ufldl.stanford.edu/housenumbers/' + file
                print('\nDownloading ' + file)
                wget.download(url, file_path)
                print(' Downloaded')
            else:
                print('File ' + file + ' already exists!')

    def get_data(self, one-hot = False, get_extra = False):

        self.trainData = sio.loadmat("./data-Svhn/train_32x32.mat")
        self.testData = sio.loadmat("./data-Svhn/test_32x32.mat")
        self.validationData = sio.loadmat("./data-Svhn/extra_32x32.mat")
        ##############################################################
        self.x_train = self.trainData["X"]
        self.y_train = self.trainData["y"]
        self.y_train[self.y_train == 10] = 0 # fixing label index issue
        ##############################################################
        self.x_test = self.testData["X"]
        self.y_test = self.testData["y"]
        self.y_test[self.y_test == 10] = 0 # fixing label index issue
        ##############################################################
        self.extraImages = self.validationData["X"]
        self.extraLabels = self.validationData["y"]
        self.extraLabels[self.extraLabels == 10] = 0 # fixing label index issue

        if one-hot:
            self.y_train = self.y_train.flatten()
            self.y_train = (np.arange(10) == self.y_train[:, np.newaxis]).astype(np.float32)

            self.y_test = self.y_test.flatten()
            self.y_test = (np.arange(10) == self.y_test[:, np.newaxis]).astype(np.float32)

        if get_extra:
            return self.x_train, self.y_train, self.x_test, self.y_test, self.extraImages, self.extraLabels
        else:
            return self.x_train, self.y_train, self.x_test, self.y_test


    # change image dimension to specified framework
    @staticmethod
    def change_dim(x_data, framework):

        if framework == "pytorch" or framework == "caffe":
            # [h, w, channel, num_images] --> [num_images,channel, h, w]
            x_new_data = x_data.transpose(3, 2, 0, 1)
        elif framework == "tensorflow" or framework == "keras":
            # [h, w, channel, num_images] --> [num_images, h, w, channel]
            x_new_data = x_data.transpose(3, 0, 1, 2)
        else:
            print("please enter pytorch, caffe, keras, or tensorflow")

        print('dimension for ' + str(framework) + ': ' + str(x_new_data.shape))
        print('--'*12)
        return x_new_data

    @staticmethod
    def change_range(range_num, x_array, y_array):
        x_array = x_array[:range_num, ]
        y_array = y_array[:range_num, ]
        print('\ndata size range has been changed. New shape below')
        print("New shape for x " + str(x_array.shape))
        print("New shape for y " + str(y_array.shape))
