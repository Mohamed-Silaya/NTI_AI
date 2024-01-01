import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas

data_set = pandas.read_csv("iris.csv")

x= data_set.iloc[:, 1:4].values
y= data_set.iloc[:, 4].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy: ", accuracy)


# mse = np.mean((y_pred - y_test)**2)
# print("Erorr: ",mse)
