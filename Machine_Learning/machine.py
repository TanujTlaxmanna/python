import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("Machine_Learning\insurance.csv")
# print(df)


# EDA 

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)
numeric_columns = ['age', 'bmi', 'children', 'charges']

for col in numeric_columns:
    plt.figure(figsize= (6, 4))
    sns.histplot(df[col], kde = True, bins = 20)
    plt.title(f"Distribution of {col}")
    plt.show()


sns.countplot(x = df['children'])
plt.show()

sns.countplot(x = df['sex'])
plt.show()

sns.countplot(x = df['smoker'])
plt.show()


for col in numeric_columns:
    plt.figure(figsize = (6, 4))
    sns.boxplot(x = df[col])
    plt.title(f"Distribution of {col}")
    plt.show()

plt.figure(figsize= (8, 6))
sns.heatmap(df.corr(numeric_only= True), annot= True)
plt.show()


# DATA CLEANING AND PREPROCESSING

