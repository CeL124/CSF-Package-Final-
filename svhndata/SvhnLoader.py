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
        self.framework = None
        self.X_data = None
        self.range_num = None
    def load_data(self):
        print('checking if directory exist...')
        try:
            os.mkdir(self.directory)
            print('\ndirectory ' + self.directory + ' is being created..')
        except:
            print('directory ' + self.directory + ' already exist.')

        print('\nChecking if data files exist...')

        for file in self.file_list:
            file_path = './'+self.directory+'/' + file
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

    def change_dim(X_data,framework = "tensorflow"):
        if framework == "pytorch" or framework=="caffe":
            X_new_data = X_data.transpose(3,2,0,1)
        elif framework == "tensorflow" or framework=="keras":
            X_new_data = X_data.transpose(3,0,1,2)
        else:
            print("Invalid option")

        print("New shape " + str(X_new_data.shape))

        return X_new_data

    def change_range(x_array,y_array,range_num):
        x_array = x_array[:range_num,]
        y_array = y_array[:range_num,]
        print("New shape for x " + str(x_array.shape))
        print("New shape for y "+ str(y_array.shape))
