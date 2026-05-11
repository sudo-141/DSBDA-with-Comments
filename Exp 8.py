### Data Visualization I
# 1. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information
# about the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library to
# see if we can find any patterns in the data.
# 2. Write a code to check how the price of the ticket (column name: 'fare') for each passenger
# is distributed by plotting a histogram. 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
df.info()

plt.figure(figsize=(10,6))
sns.countplot(data=df,x='pclass',hue='survived',palette='viridis')
plt.title("Survived And Classwise")
plt.xlabel("Pclass")
plt.ylabel("Survived")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(df['Fare'],kde=True,bin=30,color='blue')
plt.title("Survived And Classwise")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()