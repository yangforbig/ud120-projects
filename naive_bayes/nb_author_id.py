#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
import os
os.chdir('C:\\Users\\lavender\\Desktop\\Udacity\\ud120-projects\\naive_bayes')
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#print features_train[304:309]
#print features_test[0:5]
#print labels_train[0:5]
#print labels_test[0:5]



#########################################################
### your code goes here ###

import numpy
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "traning time: %f s" %(round(time() - t0))
t1 = time()
ac = clf.score(features_test, labels_test)
t1 = time() - t1
print "predicing time: %f s  Naive Bayes accuracy: %f" %(t1, ac)





#########################################################
