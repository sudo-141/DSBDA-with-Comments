### Data Analytics II
# 1. Implement logistic regression using Python/R to perform classification on
# Social_Network_Ads.csv dataset.
# 2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall
# on the given dataset.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")
df
df.info()

x = df[['Age','EstimatedSalary']]
y = df['Purchased']

xtr,xt,ytr,yt = train_test_split(x,y,test_size=0.25,random_state=0)

model = LogisticRegression()
model.fit(xtr,ytr)
ypred = model.predict(xt)

sc = StandardScaler()
xtr = sc.fit_transform(xtr)
xt = sc.transform(xt)

cm = confusion_matrix(yt,ypred)
TP,TN,FP,FN = cm.ravel()
print("Confusion Matrix:\n",cm)

acc = tp +tn / additon of all
err = tp + tn / additon of all
prec = tp /tp + FP
rec = tp / tp+FN

print("Accuracy:",acc)      
print("Error Rate:",err)
print("Precision:",prec)
print("Recall:",rec)