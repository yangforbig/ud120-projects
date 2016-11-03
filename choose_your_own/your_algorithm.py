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

'''
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
'''

### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
"""KNN algorithm"""
from sklearn.neighbors import KNeighborsClassifier


clf_knn = KNeighborsClassifier(n_neighbors =9, weights='distance')
clf_knn.fit(features_train, labels_train)
acc = clf_knn.score(features_test, labels_test)
print "KNN(k = 9, distance) acc = %f" %acc

"""SVM algorithm"""
from sklearn.svm import SVC
C = [1, 10, 100]
for c in C:
    clf_svm = SVC(C = c, kernel='rbf')
    clf_svm.fit(features_train, labels_train)
    acc = clf_svm.score(features_test, labels_test)
    print "SVM(C = %d) acc=%f" %(c, acc)








try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
