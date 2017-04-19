#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score


rf_clf = RandomForestClassifier(n_estimators=50)
ada_clf = AdaBoostClassifier(n_estimators=100)
nn_clf = KNeighborsClassifier(n_neighbors=10)

# clf = clf.fit(features_train, labels_train)
rf_clf = rf_clf.fit(features_train, labels_train)
rf_preds = rf_clf.predict(features_test)
print('Accuracy RF ', accuracy_score(rf_preds, labels_test))


ada_scores = cross_val_score(ada_clf, features_train, labels_train)
print('Accuracy ?? ', ada_scores.mean())


nn_clf.fit(features_train, labels_train)
nn_preds = nn_clf.predict(features_test)
print('Accuracy NN ', accuracy_score(nn_preds, labels_test))


# predictions = clf.predict(features_test)

# print('Accuracy ', accuracy_score(labels_test, predictions))




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
