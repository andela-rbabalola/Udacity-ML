#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


clf = GaussianNB()

train_start = time()
clf.fit(features_train, labels_train)
train_end = time()
print("training time:", round(train_end - train_start, 3), "s")

pred_start = time()
predictions = clf.predict(features_test)
pred_end = time()
print("prediction time", round(pred_end - pred_start , 3), "s")

print('Accuracy ', accuracy_score(labels_test, predictions))

#########################################################
### your code goes here ###


#########################################################


