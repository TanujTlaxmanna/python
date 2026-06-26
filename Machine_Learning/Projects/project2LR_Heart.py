# ==========================================
# HEART DISEASE DATA PREPROCESSING PROJECT
# ==========================================

# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("csv's\heart.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# ==========================================
# Check Missing Values & Duplicates
# ==========================================

print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# ==========================================
# Target Variable Distribution
# ==========================================

plt.figure(figsize=(6,4))
df['HeartDisease'].value_counts().plot(kind='bar')
plt.title("Heart Disease Distribution")
plt.show()

# ==========================================
# Numerical Feature Distribution
# ==========================================

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.histplot(df['Age'], kde=True)

plt.subplot(2,2,2)
sns.histplot(df['RestingBP'], kde=True)

plt.subplot(2,2,3)
sns.histplot(df['Cholesterol'], kde=True)

plt.subplot(2,2,4)
sns.histplot(df['MaxHR'], kde=True)

plt.tight_layout()
plt.show()

# ==========================================
# Data Cleaning
# ==========================================

# Replace Cholesterol = 0

chol_mean = df.loc[df['Cholesterol'] != 0, 'Cholesterol'].mean()

df['Cholesterol'] = df['Cholesterol'].replace(
    0,
    round(chol_mean, 2)
)

# Replace RestingBP = 0

bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()

df['RestingBP'] = df['RestingBP'].replace(
    0,
    round(bp_mean, 2)
)

# ==========================================
# Recheck Distributions
# ==========================================

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.histplot(df['Age'], kde=True)

plt.subplot(2,2,2)
sns.histplot(df['RestingBP'], kde=True)

plt.subplot(2,2,3)
sns.histplot(df['Cholesterol'], kde=True)

plt.subplot(2,2,4)
sns.histplot(df['MaxHR'], kde=True)

plt.tight_layout()
plt.show()

# ==========================================
# Categorical Analysis
# ==========================================

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
sns.countplot(x='Sex', hue='HeartDisease', data=df)

plt.subplot(1,3,2)
sns.countplot(x='ChestPainType', hue='HeartDisease', data=df)

plt.subplot(1,3,3)
sns.countplot(x='FastingBS', hue='HeartDisease', data=df)

plt.tight_layout()
plt.show()

# ==========================================
# Box Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.boxplot(x='HeartDisease', y='Cholesterol', data=df)
plt.show()

# ==========================================
# Violin Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.violinplot(x='HeartDisease', y='Age', data=df)
plt.show()

# ==========================================
# Correlation Heatmap
# ==========================================

plt.figure(figsize=(10,6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)
plt.show()

# ==========================================
# One Hot Encoding
# ==========================================

df_encoded = pd.get_dummies(
    df,
    drop_first=True
)

# Convert True/False to 0/1
df_encoded = df_encoded.astype(int)

print(df_encoded.head())

# ==========================================
# Feature Scaling
# ==========================================

from sklearn.preprocessing import StandardScaler

numerical_cols = [
    'Age',
    'RestingBP',
    'Cholesterol',
    'MaxHR',
    'Oldpeak'
]

scaler = StandardScaler()

df_encoded[numerical_cols] = scaler.fit_transform(
    df_encoded[numerical_cols]
)

print(df_encoded.head())

# ==========================================
# Final Dataset Ready For ML
# ==========================================

print(df_encoded.shape)
print(df_encoded.columns)