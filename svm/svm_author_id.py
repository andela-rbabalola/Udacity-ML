#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score


clf = svm.SVC(kernel='rbf', C=10000.0)
# c_values = [10, 100, 1000, 10000]

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

# for c_value in c_values:
#   clf = svm.SVC(kernel='rbf', C=c_value)
#   clf.fit(features_train, labels_train)
#   predictions = clf.predict(features_test)
#   print('Accuracy for ', c_value, ' ', accuracy_score(labels_test, predictions))

# train_start = time()
clf.fit(features_train, labels_train)
# train_end = time()
# print('Training time', round(train_end - train_start, 3), "s")

# pred_start = time()
predictions = clf.predict(features_test)
# print(predictions[10], predictions[26], predictions[50])

print((predictions == 1).sum())

# pred_end = time()
# print('Prediction time', round(pred_end - pred_start, 3), "s")

print('Accuracy ', accuracy_score(labels_test, predictions))


#########################################################


