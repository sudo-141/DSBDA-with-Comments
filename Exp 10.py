### Data Visualization III
# Download the Iris flower dataset or any other dataset into a DataFrame. (e.g.,
# https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
# 1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
# 2. Create a histogram for each feature in the dataset to illustrate the feature distributions.
# 3. Create a boxplot for each feature in the dataset.
# 4. Compare distributions and identify outliers.

import pandas as pd
import seaborn as sns
import matplot.pyplot as plt

df = pd.read_csv("iris.csv")
df.info()
df.describe()

df.hist(figsize=(10,6))
plt.suptitle("Histograms of all")
plt.show()

plt.figure(figsize=(12,8))
for i, column in enumerate(df.columns[:,-1],1):
    plt.subplot(2,2,i)
    sns.boxplot(y=df[column])
    plt.title(column)
plt.tight_layout()
plt.show()
