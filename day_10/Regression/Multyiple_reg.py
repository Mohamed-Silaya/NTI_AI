import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#prepare data
df = pd.read_csv('Housing.csv')
# df.info()
# print(df.isnull().any())
# print(df.isnull().sum())
df_dup = df[df.duplicated]
df = df.drop_duplicates()
# print(df)


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['mainroad'] =le.fit_transform(df['mainroad'])
df['guestroom'] =le.fit_transform(df['guestroom'])
df['basement'] =le.fit_transform(df['basement'])
df['hotwaterheating'] =le.fit_transform(df['hotwaterheating'])
df['airconditioning'] =le.fit_transform(df['airconditioning'])
df['prefarea'] =le.fit_transform(df['prefarea'])

from sklearn.compose import ColumnTransformer
enc =pd.get_dummies(df,columns=['furnishingstatus'])
df =enc

print(df.head())


#MODEL
from sklearn.model_selection import train_test_split
x= df.iloc[:,1:-1].values
y= df.iloc[:,0].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred_train = lr.predict(x_train)

# Evaluate the model's performance on the train set
score_train = lr.score(x_train, y_train)

# Make predictions on the test set
y_pred_test = lr.predict(x_test)

# Evaluate the model's performance on the test set
score_test = lr.score(x_test, y_test)

# Print the results
print('Train score:', score_train)
print('Test score:', score_test)

##polynomial
from sklearn.preprocessing import PolynomialFeatures
poly_regs= PolynomialFeatures(degree= 2)
x_poly= poly_regs.fit_transform(x)
lin_reg_2 =LinearRegression()
lin_reg_2.fit(x_poly, y)

predicted = lin_reg_2.predict(x_poly)
mse = np.mean((predicted - y)**2)

print("Erorr: ",mse)
