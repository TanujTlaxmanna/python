import numpy as np
import pandas as pd

df = pd.read_csv("csv's\\cars.csv")
print(df.head())

print(df['brand'].value_counts())
print(df['brand'].nunique())

print(df['fuel'].value_counts())
print(df['fuel'].nunique())

print(df['owner'].value_counts())
print(df['owner'].nunique())


# ONE HOT ENCODING USING PANDAS

a = pd.get_dummies(df, columns = ['fuel', 'owner'])
print(a.head())


# K - 1 ONE HOT ENCODING

b = pd.get_dummies(df, columns = ['fuel', 'owner'], drop_first = True)
print(b.head())

# ONE HOT ENCODING USING SCIKIT

from sklearn.model_selection import train_test_split

print(df.head())
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 0:4],
                                                    df.iloc[: , -1],
                                                    test_size = 0.2,
                                                    random_state = False)

print(X_train.head())
print(X_test.head())

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop = 'first', dtype = np.int32)

X_train_new = ohe.fit_transform(X_train[['fuel', 'owner']]).toarray()
print(X_train_new)

X_test_new = ohe.fit_transform(X_test[['fuel', 'owner']]).toarray()
print(X_test_new)


z = X_train[['brand', 'km_driven']].values
print(X_train[['brand', 'km_driven']].values)

y = np.hstack((z, X_train_new))
print(y.shape)


# ONE HOT ENCODING WITH TOP CATEGORIES

print(df['brand'].value_counts())
print(df['brand'].nunique())

counts = df['brand'].value_counts()
df['brand'].nunique()
threshold = 100

repl = counts[counts <= threshold].index

pd.get_dummies(df['brand'].replace(repl, 'uncommon'))
print(pd.get_dummies(df['brand'].replace(repl, 'uncommon')))

b = print(pd.get_dummies(df['brand'].replace(repl, 'uncommon'), dtype=int))
print(b)