### Data Analytics I
# Create a Linear Regression Model using Python/R to predict home prices using Boston Housing
# Dataset (https://www.kaggle.com/c/boston-housing). The Boston Housing dataset contains
# information about various houses in Boston through different parameters. There are 506 samples
# and 14 feature variables in this dataset.
# The objective is to predict the value of prices of the house using the given features.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("bs.csv")
df
df.info()

df = df.fillna(df.mean())
x = df.dropna('medv',axis=1)
y = df['medv']

xtr,xt,ytr,yt = train_test_split(x,y,train_size=0.2,random_state=42)

model = LinearRegression()
model.fit(xtr,ytr)
ypr = model.predict(xt)
mse = mean_squared_error(ypr,yt)
r2 = r2_score(ypr,yt)

plt.scatter(ypr,yt,alpha=0.2,color='blue')
plt.plot([yt.min(),yt.max()],[yt.min(),yt.max()],'r--',lw=2)
plt.title("Actual vs Predicted)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()