import wget
import os
import scipy.io as sio

class SvhnData:
    def __init__(self):
        self.directory = 'dataSvhn'
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
    def load_data(self):
        print('checking if directory exist...')
        try:
            os.mkdir(self.directory)
            print('\ndirectory ' + self.directory + ' is being created..')
        except:
            print('directory ' + self.directory + ' already exist.')

        print('\nChecking if data files exist...')

        for file in self.file_list:
            file_path = './'+self.directory+'/'+file
            if not os.path.exist(file_path):
                url = 'http://ufldl.stanford.edu/housenumbers/' + file
                print('Downloadind ' + file)
                wget.download(url, file_path)
                print(' Downloaded')
            else:
                print('File ' + file + ' already exists!')

    def get_data(self, get_extra = False):
        self.trainData = sio.loadmat("./dataSvhn/train_32x32.mat")
        self.testData = sio.loadmat("./dataSvhn/test_32x32.mat")
        self.validationData = sio.loadmat("./dataSvhn/extra_32x32.mat")
        self.x_train = self.trainData["X"]
        self.y_train = self.trainData["y"]
        self.x_test = self.testData["X"]
        self.y_test = self.testData["y"]
        self.extraImages = self.validationData["X"]
        self.extraLabels = self.validationData["y"]

        if get_extra:
            return self.x_train, self.y_train, self.x_test, self.y_test, self.extraImages, self.extraLabels
        else:
            return self.x_train, self.y_train, self.x_test, self.y_test
