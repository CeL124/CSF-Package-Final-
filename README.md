# CSF-Package-Final-
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
