import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

df = pd.read_csv("survey_lung_cancer.csv")
enc = LabelEncoder()

df['GENDER'] =enc.fit_transform(df['GENDER'])
df['LUNG_CANCER']= enc.fit_transform(df['LUNG_CANCER'])

print(df.head())


#####SVM
sv= SVC()
x= df.iloc[:,1:-1].values
y= df.iloc[:, -1].values

sv.fit(x,y)
y_pred=sv.predict(x)

acc= accuracy_score(y,y_pred)
print(acc)