from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np

data_set = pandas.read_csv("Salary_Data.csv")

x= data_set.iloc[:, 1:2].values
y= data_set.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_regs= LinearRegression()
lin_regs.fit(x,y)

from sklearn.preprocessing import PolynomialFeatures
poly_regs= PolynomialFeatures(degree= 2)
x_poly= poly_regs.fit_transform(x)
lin_reg_2 =LinearRegression()
lin_reg_2.fit(x_poly, y)

predicted = lin_reg_2.predict(x_poly)
mse = np.mean((predicted - y)**2)

print("Erorr: ",mse)

