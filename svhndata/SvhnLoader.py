"""
CLASS to get SVHN training and Testing data.
"""
from svhndata.SvhnFormatter import onehot_encoder, svhn_max_min
import wget # get file from url
import os
import scipy.io as sio # To load the matlab files


class SvhnData:
    def __init__(self):
        self.directory = 'data-Svhn'
        self.file_list = ['train_32x32.mat', 'test_32x32.mat' , 'extra_32x32.mat']
        self.small_file_list = ['train_32x32.mat', 'test_32x32.mat']
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
    def load_data(self, get_extra=False):
        # try Creating directory data-Svhn. Catch if already exists
        print('checking if directory exists...')
        try:
            os.mkdir(self.directory)
            print('\ndirectory ' + self.directory + ' is being created..')
        except FileExistsError:
            print('directory ' + self.directory + ' already exists.')
        ##############################################################
        print('\nChecking if data files exist...')
        if get_extra:
            for file in self.file_list:
                file_path = './'+self.directory+'/' + file
                if not os.path.exists(file_path):
                    url = 'http://ufldl.stanford.edu/housenumbers/' + file
                    print('\nDownloading ' + file)
                    wget.download(url, file_path)
                    print(' Downloaded')
                else:
                    print('File ' + file + ' already exists!')
        ##############################################################
        else:
            for file in self.small_file_list:
                file_path = './'+self.directory+'/' + file
                if not os.path.exists(file_path):
                    url = 'http://ufldl.stanford.edu/housenumbers/' + file
                    print('\nDownloading ' + file)
                    wget.download(url, file_path)
                    print(' Downloaded')
                else:
                    print('File ' + file + ' already exists!')

    # function will load the Matlab file into a variable.
    # Then it will separate images and labels.
    # This will happen for train, test, and extra
    def get_data(self, onehot=False, get_extra=False, rescale=True):

        if get_extra:
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

            if onehot:
                self.y_train = onehot_encoder(self.y_train)
                self.y_test = onehot_encoder(self.y_test)
                self.extraLabels = onehot_encoder(self.extraLabels)

            if rescale:
                self.x_train = svhn_max_min(self.x_train)
                self.x_test = svhn_max_min(self.x_test)
                self.extraImages = svhn_max_min(self.extraImages)

        if get_extra:
            return self.x_train, self.y_train, self.x_test, self.y_test, self.extraImages, self.extraLabels
        ###################################################################################################
        else:
            self.trainData = sio.loadmat("./data-Svhn/train_32x32.mat")
            self.testData = sio.loadmat("./data-Svhn/test_32x32.mat")
            ##############################################################
            self.x_train = self.trainData["X"]
            self.y_train = self.trainData["y"]
            self.y_train[self.y_train == 10] = 0  # fixing label index issue
            ##############################################################
            self.x_test = self.testData["X"]
            self.y_test = self.testData["y"]
            self.y_test[self.y_test == 10] = 0  # fixing label index issue

            if onehot:
                self.y_train = onehot_encoder(self.y_train)

                self.y_test = onehot_encoder(self.y_test)

            if rescale:
                self.x_train = svhn_max_min(self.x_train)
                self.x_test = svhn_max_min(self.x_test)
            return self.x_train, self.y_train, self.x_test, self.y_test


if __name__ == '__main__':
    SvhnData()
