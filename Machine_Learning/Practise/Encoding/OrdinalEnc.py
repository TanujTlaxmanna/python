import numpy as np
import pandas as pd

df = pd.read_csv("csv's//customer.csv")

print(df.sample(5))

df = df.iloc[:, 2:]

print(df.head())


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 0:2],
                                                    df.iloc[: , -1],
                                                    test_size = 0.2)

print(X_train)
print(y_train)


from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(categories = [['Poor', 'Average', 'Good', 'Excellent'], ['School', 'UG', 'PG']])
oe.fit(X_train)

X_train = oe.transform(X_train)
X_test = oe.transform(X_test)

print(X_train)
print(X_test)

print(oe.categories_)


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y_train)
print(le.classes_)

y_train = le.transform(y_train)
y_test = le.transform(y_test)

print(y_train)
print(y_test)
