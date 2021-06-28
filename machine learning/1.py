import numpy as np
import matplotlib.pyplot as plt
from numpy.testing._private.utils import KnownFailureException
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris()
iris_X=iris.data
iris_y=iris.target
# print(iris_X[:2,:])
# print(iris_y)
X_train,X_Test,y_train,y_test=train_test_split(iris_X,iris_y,test_size=0.4)
# print(y_train)

knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
print(knn.predict(X_Test))
print(y_test)
print(np.sum((knn.predict(X_Test)==y_test)==True)/y_test.size)