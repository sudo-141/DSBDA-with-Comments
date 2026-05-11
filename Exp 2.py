### Data Wrangling II
# Create an “Academic performance” dataset of students and perform the following operations using
# Python.
# 1. Scan all variables for missing values and inconsistencies. If there are missing values and/or
# inconsistencies, use any of the suitable techniques to deal with them.
# 2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable
# techniques to deal with them.
# 3. Apply data transformations on at least one of the variables. The purpose of this
# transformation should be one of the following reasons: to change the scale for better
# understanding of the variable, to convert a non-linear relation into a linear one, or to
# decrease the skewness and convert the distribution into a normal distribution.
# Reason and document your approach properly

import numpy as np
import pandas as pd

df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Sci'] = df['Sci'].fillna(df['Sci'].mean())
df['Att'] = df['Att'].fillna(df['Att'].mean())

# Handling inconsistencies
df['Math'] = df['Math'].clip(upper=100)
df['Sci'] = df['Sci'].clip(upper=100)
df['Att'] = df['Att'].clip(upper=100)

# Outlier Detection and Handling using IQR
for col in ['Math', 'Sci', 'Att']:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = np.where(df[col] > upper, upper, df[col])
    df[col] = np.where(df[col] < lower, lower, df[col])

# Data Transformation (Scaling)
df['Math'] = df['Math'] / 10
df['Sci'] = df['Sci'] / 10
df['Att'] = df['Att'] / 10

print("\nCleaned and Transformed Dataset:\n")
print(df)