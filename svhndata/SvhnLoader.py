import wget
import os

class SvhnData:
    def __init__(self):
        self.directory = 'dataSvhn'
        self.file_list = ['train_32x32.mat', 'test_32x32.mat' , 'extra_32x32.mat']
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
            file_path = './'+self.directory+'/'+file
            if not os.path.exist(file_path):
                url = 'http://ufldl.stanford.edu/housenumbers/' + file
                print('Downloadind ' + file)
                wget.download(url, file_path)
                print(' Downloaded')
            else:
                print('File ' + file + ' already exists!')

    def change_dim(self,self.X_data,self.framework):
        if self.framework == "pytorch" or self.framework=="caffe":
            X_new_data = self.X_data.transpose(3,2,0,1)
        elif self.framework == "tensorflow" or self.framework=="keras":
            X_new_data = self.X_data.transpose(3,0,1,2)
        else:
            print("Invalid option")

        print("New shape " + str(X_new_data.shape))

        return X_new_data

    def change_range(self,x_array,y_array,self.range_num):
        x_array = x_array[:self.range_num,]
        y_array = y_array[:self.range_num,]
        print("New shape for x " + str(x_array.shape))
        print("New shape for y "+ str(y_array.shape))
