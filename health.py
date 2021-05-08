import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling

data_file_path = '/Users/wt/Desktop/heart.csv'
#data = pd.read_csv(data_file_path)
#pandas_profiling.ProfileReport(data)
#pfr = pandas_profiling.ProfileReport(data)
#pfr.to_file('report1.html')

data_df = pd.read_csv(data_file_path)
#overview
data_df.head()
print(data_df)
data_df.isnull().sum()
print(data_df.isnull().sum())

sns.countplot(data_df['target'])
plt.title('Countplot of Target')
plt.xlabel('target')
plt.ylabel('Patients')
plt.show()


y = data_df["target"].values
x = data_df.drop(["target"], axis = 1)

#Scaling - mandatory for knn
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = ss.fit_transform(x)

#3:7
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3) 

train_score = []
test_score = []
k_vals = []

for k in range(1, 20):
    k_vals.append(k)
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    
    tr_score = knn.score(X_train, y_train)
    train_score.append(tr_score)
    
    te_score = knn.score(X_test, y_test)
    test_score.append(te_score)

max_test_score = max(test_score)
test_scores_ind = [i for i, v in enumerate(test_score) if v == max_test_score]
print('Max test score {} and k = {}'.format(max_test_score * 100, list(map(lambda x: x + 1, test_scores_ind))))
knn = KNeighborsClassifier(3)

knn.fit(X_train, y_train)
knn.score(X_test, y_test)

y_pred = knn.predict(X_test)
#confusion_matrix(y_test,y_pred)
#pd.crosstab(y_test, y_pred, rownames = ['Actual'], colnames =['Predicted'], margins = True)
#print(pd.crosstab)
print(confusion_matrix(y_test,y_pred))
print('\n')
print(classification_report(y_test,y_pred))