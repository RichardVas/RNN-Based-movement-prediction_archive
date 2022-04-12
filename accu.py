from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_percentage_error as MAPE
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

y = np.array([8,8,0])
y_pred = np.array([10,8,1])

x = np.array([10,10,5])
x_pred = np.array([11,10,6])

error = 0
for i in range(len(y)):
    error += abs(y[i] - y_pred[i])


print('sklearn MAE = ', MAE(y, y_pred))
print('sklearn MSE = ', MSE(y, y_pred))
print('sklearn MAPE = ', MAPE(y,y_pred))


print('sklearn MAE = ', MAE(x, x_pred))
print('sklearn MSE = ', MSE(x, x_pred))
print('sklearn MAPE = ', MAPE(x,x_pred))
xMAE = MAE(x, x_pred)
yMAE = MAE(y, y_pred)
plt.plot(xMAE,yMAE)
plt.scatter(xMAE,yMAE)
plt.show()