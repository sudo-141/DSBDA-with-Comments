### Descriptive Statistics - Measures of Central Tendency and variability
# Perform the following operations on any open source dataset (e.g., data.csv)
# 1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for
# a dataset (age, income etc.) with numeric variables grouped by one of the qualitative
# (categorical) variable. For example, if your categorical variable is age groups and
# quantitative variable is income, then provide summary statistics of income grouped by the
# age groups. Create a list that contains a numeric value for each response to the categorical
# variable.
# 2. Write a Python program to display some basic statistical details like percentile, mean,
# standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
# of iris.csv dataset.

import numpy as np
import pandas as pd

df = pd.read_csv("student.csv")
print(df)
df.info()

print(df.loc[:,'Age'].mean())
print(df.loc[:,'Age'].mode())
print(df.loc[:,'Age'].std())
print(df.loc[:,'Gender'].mean())
print(df.loc[:,'Age'].mode())

print(df.groupby(df['Gender']).Age.mean())
df.min()
df.max()
df.mode()

from sklearn import preprocessing

enc = preprocessing.OneHotEncoder()
enc_df = df.DataFrame(enc.fit_transform(df[['Gender']]).toarray())
print(enc_df)

import np 
import pd 

df = pd.read_csv("iris.csv")
print(df)
df.info()

irisSet = (df['species'] == 'setosa')
print(df[irisSet].describe())

irisVers = (df['species'] == 'versicolor')
print(df[irisVers].describe())
    
irisVerg = (df['species'] == 'virginica')
print(df[irisVerg].describe())
