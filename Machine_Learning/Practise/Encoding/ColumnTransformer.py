import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder


df = pd.read_csv("csv's\\covid_toy.csv")
print(df.head())

print(df['cough'].value_counts())
print(df['city'].value_counts())
print(df.isnull().sum())


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns = ['has_covid']),
                                                    df['has_covid'],
                                                    test_size = 0.2,
                                                    random_state = 0)


# NORMAL METHOD 

si = SimpleImputer()
X_train_fever = si.fit_transform(X_train[['fever']])
X_test_fever = si.fit_transform(X_test[['fever']])

oe = OrdinalEncoder(categories = [['Mild', 'Strong']])
X_train_cough = oe.fit_transform(X_train[['cough']])
X_test_cough = oe.fit_transform(X_test[['cough']])


ohe = OneHotEncoder(drop = 'first', sparse_output = False)
X_train_gender_city = ohe.fit_transform(X_train[['gender', 'city']])
X_test_gender_city = ohe.fit_transform(X_test[['gender', 'city']])

# Extracting Age
X_train_age = X_train.drop(columns=['gender', 'fever', 'cough', 'city']).values

# also the test data
X_test_age = X_test.drop(columns=['gender', 'fever', 'cough', 'city']).values


X_train_transformed = np.concatenate((X_train_age, X_train_fever, X_train_gender_city, X_train_cough), axis = 1)
X_test_transformed = np.concatenate((X_test_age, X_test_fever, X_test_gender_city, X_test_cough), axis = 1)

print(X_train_transformed.shape)



# USING COLUMN TRANSFORMER 

from sklearn.compose import ColumnTransformer

transformer = ColumnTransformer(transformers = [
    ('tnf1', SimpleImputer(), ['fever']),
    ('tnf2', OrdinalEncoder(categories = [['Mild', 'Strong']]), ['cough']),
    ('tnf3', OneHotEncoder(sparse_output = False, drop = 'first'), ['gender', 'city'])
], remainder = 'passthrough')

x = transformer.fit_transform(X_train)
print(x.shape)

y = transformer.transform(X_test)
print(y.shape)