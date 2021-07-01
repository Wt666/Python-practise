from numpy.compat import py3k
from numpy.core.fromnumeric import transpose
from scipy.stats.stats import PearsonRConstantInputWarning
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np
iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=4)
# knn=KNeighborsClassifier(n_neighbors=5) # the fifth nearest
# knn.fit(X_train,y_train)
# knn=KNeighborsClassifier(n_neighbors=5)
# scores=cross_val_score(knn,X,y,cv=5,scoring='accuracy')
# # y_pred=knn.predict(X_test)
# # print(knn.score(X_test,y_test)) 
# print(scores.mean())
k_range=range(1,31)
k_scores=[]
for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    # scores=cross_val_score(knn,X,y,cv=10,scoring='accuracy') #for classification
    loss=-cross_val_score(knn,X,y,cv=10,scoring='neg_mean_squared_error') #for regression
    k_scores.append(loss.mean())
plt.plot(k_range,k_scores)
new_ticks=np.linspace(0,30,31)
plt.xticks(new_ticks)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Acuuracy')
plt.show()
