import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

# # Mean, Median, Mode 

# df = sns.load_dataset('tips')

# print(df.head())

# print(np.mean(df['total_bill']))
# print(np.median(df['total_bill']))
# print(statistics.mode(df['total_bill']))

# sns.boxplot(df['total_bill'])
# plt.show()

# sns.histplot(df['total_bill'])
# plt.show()

# sns.kdeplot(df['total_bill'])
# plt.show()


# df1 = sns.load_dataset('iris')

# print(df1.head())

# print(np.mean(df1['sepal_length']))
# print(np.median(df1['sepal_length']))
# print(statistics.mode(df1['sepal_length']))

# sns.boxplot(df1['sepal_length'])
# plt.show()
# sns.boxplot(df1['sepal_width'])
# plt.show()


# sns.histplot(df1['sepal_length'])
# plt.show()
# sns.histplot(df1['sepal_width'])
# plt.show()

# sns.kdeplot(df1['sepal_length'])
# plt.show()
# sns.kdeplot(df1['sepal_width'])
# plt.show()


# sns.countplot(df1['species'])
# plt.show()

# print(np.percentile(df['sepal_length'], [25, 99]))



# Z SCORE AND IQR 
# OUTLIERS

dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11, 14, 13, 15, 10, 15, 12, 10, 14, 13, 15, 10]

outliers = []

# ZSCORE COMPUTATION
def detect_outliers(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i - mean)/std
        if np.absolute(z_score) > threshold:
            outliers.append(i)

    return outliers

print(detect_outliers(dataset))


# IQR COMPUTATION
# STEPS
# 1. Sort the data
# 2. Calculte Q1 and Q3
# 3. IQR(Q3-Q1)
# 4. Lower Fence = Q1 - 1.5(IQR)
# 5. Upper Fence = Q3 + 1.5(IQR)

dataset = sorted(dataset)

q1,q3 = np.percentile(dataset, [25,75])
print(q1, q3)

iqr = q3 - q1

lower_fence = q1 - (1.5*iqr)
upper_fence = q3 + (1.5*iqr)

print(lower_fence, upper_fence)

iqr_outliers = []

for i in dataset:
    if i < lower_fence or i > upper_fence:
        iqr_outliers.append(i)

print("IQR Outliers:", iqr_outliers)



# Z TEST 

from statsmodels.stats.weightstats import ztest

# Enter IQ levels for 20 patients
data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
        105, 109, 109, 109, 110, 112, 112, 113, 114, 115]

# One-sample Z-test
z_stat, p_value = ztest(data, value=100)

print("Z-statistic:", z_stat)
print("P-value:", p_value)


# t-test

ages = [10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]

import numpy as np

# Population mean
ages_mean = np.mean(ages)
print(ages_mean)

# Random sample of size 10
sample_size = 10
age_sample = np.random.choice(ages, sample_size)

print(age_sample)

from scipy.stats import ttest_1samp

print(ttest_1samp(age_sample, 30))



# Consider another example
# Ages of the college students (Population)
# Test whether one class has the same average age as the college

import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import ttest_1samp
import math

# For reproducibility
np.random.seed(6)

# Generate population of college students
school_ages = stats.poisson.rvs(loc=18, mu=35, size=1500)

# Generate ages of one class (sample)
classA_ages = stats.poisson.rvs(loc=18, mu=30, size=60)

# Display population and sample
print("School Ages:")
print(school_ages)

print("\nClass A Ages:")
print(classA_ages)

# Calculate means
print("\nPopulation Mean:", school_ages.mean())
print("Class A Mean:", classA_ages.mean())

# Perform One-Sample T-Test
t_statistic, p_value = ttest_1samp(classA_ages, school_ages.mean())

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# Decision
alpha = 0.05

if p_value < alpha:
    print("\nReject the Null Hypothesis (H0)")
    print("Conclusion: Class A's average age is significantly different from the school's average age.")
else:
    print("\nFail to Reject the Null Hypothesis (H0)")
    print("Conclusion: There is no significant difference between Class A's average age and the school's average age.")



import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris Dataset
df = sns.load_dataset('iris')

# Display first 5 rows
print(df.head())

# Correlation Matrix (Pearson by default)
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Pearson Correlation
pearson_corr = df.corr(method='pearson', numeric_only=True)
print("\nPearson Correlation:")
print(pearson_corr)

# Spearman Correlation
spearman_corr = df.corr(method='spearman', numeric_only=True)
print("\nSpearman Correlation:")
print(spearman_corr)

# Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm')
plt.title("Pearson Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(df, hue='species')
plt.show()