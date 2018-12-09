# svhndata package
Building the *svhndata* package to get [The Street View House Numbers (SVHN) Dataset](http://ufldl.stanford.edu/housenumbers/) ready for machine learning modeling for different frameworks.

![alt text][svhn-image]

[svhn-image]:http://ufldl.stanford.edu/housenumbers/32x32eg.png "image from Stanford webpage"

### Features
The *svhndata* package will:

- download the SVHN Matlab files from the Stanford University website.
- load the Matlab files
- set the training and testing.
  - return x_train, y_train, x_test, y_test.
  - it has an option to add extra data.


### Libraries Needed
We used python 3.5. Therefore any future version should work.
We used a couple of libraries to create this package. 
Some already come automatically installed in python3. 

The following libraries should be install in your machine:

__Numpy__
```
pip install numpy
```
```
conda install -c anaconda numpy
```
__wget__
```
pip install wget
```

### Installation
Type the following commands in your terminal.
```
git clone https://github.com/CeL124/CSF-Package-Final-.git

cd CSF-Package-Final-

python setup.py install
```


