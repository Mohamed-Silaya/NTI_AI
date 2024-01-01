from matplotlib import pyplot as plt
import pandas
from sklearn import linear_model
import numpy as np

data_set = pandas.read_csv("Salary_Data.csv")

x= data_set.iloc[:, 1:2].values
y= data_set.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_regs= LinearRegression()
lin_regs.fit(x,y)
predicted = lin_regs.predict(x)

mse = np.mean((predicted - y)**2)

print("Erorr: ",mse)