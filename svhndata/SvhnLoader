import wget
import os

class SvhnData:
    def __init__(self):
        self.directory = 'dataSvhn'
        self.file_list = ['train_32x32.mat', 'test_32x32.mat' , 'extra_32x32.mat']
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
