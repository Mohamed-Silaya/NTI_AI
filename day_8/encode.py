import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

my_data = pd.read_csv("survey_lung_cancer.csv")
male_fam= my_data[my_data.columns[0]]
enc = LabelEncoder()
my_data[my_data.columns[0]] = enc.fit_transform(male_fam)
enc = LabelEncoder()

my_data['LUNG_CANCER']= enc.fit_transform(my_data['LUNG_CANCER'])

print(my_data.head())

#####KNN
# x= my_data.iloc[:,1:-1].values
# y= my_data.iloc[:, -1].values

# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(x_train, y_train)
# y_pred = knn.predict(x_test)

# from sklearn.metrics import accuracy_score

# accuracy = accuracy_score(y_test, y_pred)

# print("Accuracy: ", accuracy)

# ###Decision tree