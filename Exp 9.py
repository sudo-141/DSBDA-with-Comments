### Data Visualization II
# 1. Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for distribution
# of age with respect to each gender along with the information about whether they survived
# or not. (Column names : 'sex' and 'age')
# 2. Write observations on the inference from the above statistics.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
df.info()

df = df.dropna(subset=['age'])

plt.figure(figsize=(10,6))
sns.boxplot(data=df,x='sex',y='age',hue='survived')
plt.title("")
plt.xlable("Gender")
plt.ylabel("Age")
plt.show()