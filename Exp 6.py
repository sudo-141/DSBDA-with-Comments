### Data Analytics III
# 1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset.
# 2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall
# on the given dataset.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")
df
df.info()

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

xtr,xt,ytr,yt = train_test_split(x,y,test_size=0.25,random_state=0)

model = GaussianNB()
model.fit(xtr,ytr)
ypred = model.predict(xt)
cm = confusion_matrix(yt,ypred)
print(cm)

ytp = (df['species']=='setosa').astype(int)
ypredp = (df['species']=='setosa').astype(int) 

cmb = confusion_matrix(ytp,ypredp)
print(cmb)

TP,TN,FP,FN = cmb.ravel()
print("Confusion Matrix:\n",cm)

acc = tp +tn / additon of all
err = tp + tn / additon of all
prec = tp /tp + FP
rec = tp / tp+FN

print("Accuracy:",acc)      
print("Error Rate:",err)
print("Precision:",prec)
print("Recall:",rec)
