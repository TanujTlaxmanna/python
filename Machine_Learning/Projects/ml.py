import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("csv's\placement.csv")

print(df.head())
print(df.info)
print(df.shape)

df = df.iloc[:,1:]  #Get all rows from the data, but colxumns should be from 1 onwards

plt.scatter(df['cgpa'], df['iq'], c = df['placement'])
plt.show()

X = df.iloc[:,0:2]
y = df.iloc[:,-1]

print(X)
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

print("This is X training \n", X_train, "\n\n\n")
print("This is X testing \n", X_test, "\n\n\n")
print("This is y training \n", y_train, "\n\n\n")
print("This is y testing \n", y_test, "\n\n\n")



from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train) # Here we are using fit_transform because we dont know any patter and we have to fit some logic
print(X_train)
X_test = scalar.transform(X_test) # Here we use transform because now we know what the pattern is during training and theres no need to fit anything
print(X_test)


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

clf.fit(X_train, y_train) #Model Training
y_pred = clf.predict(X_test)
print(y_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test, y_pred)
print(acc)


from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, y_train.values, clf = clf, legend = 2) # Here we turn y train values into numpy arrays, however we have already put x_train in numpy array so we dont have to turn it into numpy array
plt.show()


import pickle # Import the pickle module to save and load Python objects

pickle.dump(clf, open('Machine_Learning\Models\model.pkl', 'wb'))# Save the trained machine learning model (clf) into a file named 'model.pkl',  'wb' stands for Write Binary mode, which is required for saving pickle files
