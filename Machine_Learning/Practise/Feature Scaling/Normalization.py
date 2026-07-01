import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("csv's\\wine_data.csv", usecols = [1,2,3])
df.columns = ['Class label', 'Alcohol', 'Malic acid']
print(df.head())

# MIN - MAX SCALING

sns.kdeplot(df['Alcohol'])
plt.show()

sns.kdeplot(df['Malic acid'])
plt.show()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('Class label', axis = 1),
                                                    df['Class label'],
                                                    test_size = 0.3,
                                                    random_state = 0)

print(X_train.shape)
print(X_test.shape)



from sklearn.preprocessing import MinMaxScaler
scalar = MinMaxScaler()
scalar.fit(X_train)

X_train_scaled = scalar.transform(X_train) # We take every value of X_train and transform them using the formula
X_test_scaled = scalar.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns = X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns = X_test.columns)

rounds = np.round(X_train.describe(), 1)
print(rounds)

rounds2 = np.round(X_train_scaled.describe(), 1)
print(rounds2)


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
ax1.scatter(X_train['Alcohol'], X_train['Malic acid'])
ax1.set_title("Before Scaling")
ax2.scatter(X_train_scaled['Alcohol'], X_train_scaled['Malic acid'], color='red')
ax2.set_title("After Scaling")
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['Alcohol'], ax=ax1)
sns.kdeplot(X_train['Malic acid'], ax=ax1)
# after scaling
ax2.set_title('After Standard Scaling')
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()

# COMPARISION OF DISTRIBUITON 
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Age Distribution Before Scaling')
sns.kdeplot(X_train['Alcohol'], ax=ax1)
# after scaling
ax2.set_title('Age Distribution After Standard Scaling')
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Age Distribution Before Scaling')
sns.kdeplot(X_train['Malic acid'], ax=ax1)
# after scaling
ax2.set_title('Age Distribution After Standard Scaling')
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()


# ROBUST SCALING 

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

print(np.round(X_train.describe(), 1))
print(np.round(X_train_scaled.describe(), 1))
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.scatter(X_train['Alcohol'], X_train['Malic acid'])
ax1.set_title("Before Scaling")
ax2.scatter(X_train_scaled['Alcohol'], X_train_scaled['Malic acid'], color='red')
ax2.set_title("After Robust Scaling")
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Before Scaling")
sns.kdeplot(X_train['Alcohol'], ax=ax1)
sns.kdeplot(X_train['Malic acid'], ax=ax1)
ax2.set_title("After Robust Scaling")
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Alcohol Distribution Before Scaling")
sns.kdeplot(X_train['Alcohol'], ax=ax1)
ax2.set_title("Alcohol Distribution After Robust Scaling")
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Malic Acid Distribution Before Scaling")
sns.kdeplot(X_train['Malic acid'], ax=ax1)
ax2.set_title("Malic Acid Distribution After Robust Scaling")
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()


# MAX ABSOLUTE SCALING 

from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

print(np.round(X_train.describe(), 1))
print(np.round(X_train_scaled.describe(), 1))

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.scatter(X_train['Alcohol'], X_train['Malic acid'])
ax1.set_title("Before Scaling")
ax2.scatter(X_train_scaled['Alcohol'], X_train_scaled['Malic acid'], color='red')
ax2.set_title("After MaxAbs Scaling")
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Before Scaling")
sns.kdeplot(X_train['Alcohol'], ax=ax1)
sns.kdeplot(X_train['Malic acid'], ax=ax1)
ax2.set_title("After MaxAbs Scaling")
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Alcohol Distribution Before Scaling")
sns.kdeplot(X_train['Alcohol'], ax=ax1)
ax2.set_title("Alcohol Distribution After MaxAbs Scaling")
sns.kdeplot(X_train_scaled['Alcohol'], ax=ax2)
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,5))
ax1.set_title("Malic Acid Distribution Before Scaling")
sns.kdeplot(X_train['Malic acid'], ax=ax1)
ax2.set_title("Malic Acid Distribution After MaxAbs Scaling")
sns.kdeplot(X_train_scaled['Malic acid'], ax=ax2)
plt.show()