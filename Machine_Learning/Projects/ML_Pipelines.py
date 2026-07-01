import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_selection import SelectKBest, chi2 
from sklearn.tree import DecisionTreeClassifier
from ydata_profiling import ProfileReport

df = pd.read_csv("csv's\\titanic.csv")
print(df.head())

# prof = ProfileReport(df)
# prof.to_file(output_file = 'output.html')

df.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace = True)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns = ['Survived']),
                                                    df['Survived'],
                                                    test_size = 0.2,
                                                    random_state = 42)

print(X_train.sample(5))
print(y_train.sample(5))

# IMPUTING MISSING VALUES (imputation transformer)

trf1 = ColumnTransformer([
    ('impute_age', SimpleImputer(), [2]),
    ('impute_embarked', SimpleImputer(strategy = 'most_frequent'), [6])
], remainder = 'passthrough')


# ONE HOT ENCODING

trf2 = ColumnTransformer([
    ('ohe_gender_embarked', OneHotEncoder(sparse_output = False, handle_unknown = 'ignore'), [1, 3])
], remainder = 'passthrough')


# SCALING
trf3 = ColumnTransformer([
    ('scale', MinMaxScaler(), slice(0,10)) 
], remainder = 'passthrough')


# FEATURE SELECTION 
trf4 = SelectKBest(score_func = chi2, k = 8)

# MODEL TRAINING 
trf5 = DecisionTreeClassifier() 


# CREATING PIPELINES

pipe = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('trf3', trf3),
    ('trf4', trf4),
    ('trf5', trf5)
])


# we can also use make_pipeline
# pipe = make_pipeline(trf1,trf2,trf3,trf4,trf5)

# This is similar to make_column_transformer where instead of passing an extra argument name we only need to pass 2 arguments (object, and location)

pipe.fit(X_train, y_train)


from pprint import pprint
pprint(pipe.named_steps)

print(pipe.named_steps['trf1'])
print(pipe.named_steps['trf1'].transformers_[0][1].statistics_)
print(pipe.named_steps['trf1'].transformers_[1][1].statistics_)



# For displaying the Pipeline

from sklearn import set_config
set_config(display='diagram')  # This sadly works only on jupyter nb :(


# PREDICTIONS 

y_pred = pipe.predict(X_test)
print(y_pred)


from sklearn.metrics import accuracy_score
a = accuracy_score(y_test, y_pred)
print('\n\n\nThe accuracy of the model is :, ',a,'\n')



# CROSS VALIDATION USING PIPELINES

from sklearn.model_selection import cross_val_score
print('The Cross validation score with cv = 5 is : ',cross_val_score(pipe, X_train, y_train, cv = 5, scoring = 'accuracy').mean(),'\n')


# GRID SEARCH USING PIPELINE

params = {
    'trf5__max_depth' : [1,2,3,4,5,None]
}

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(pipe, params, cv = 5, scoring = 'accuracy')
grid.fit(X_train, y_train)

print('The grid best search score is : ',grid.best_score_,'\n')
print('The best decision tree depth is : ',grid.best_params_,'\n')


# EXPORTING THE PIPELINE 

import pickle
pickle.dump(pipe, open("Machine_Learning\\Models\\pipe.pkl", 'wb')) 

# print(df.head().to_numpy())
# print(y_train.sample(5))
