import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("csv's\\Social_Network_Ads.csv")

df = df.iloc[: , 2:]
a = df.sample(5)
print(a)

# TRAIN TEST SPLIT 

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.drop('Purchased', axis = 1),
                                                    df['Purchased'],
                                                    test_size = 0.3,
                                                    random_state = 0)

print(X_train.shape)
print(X_test.shape)



# STANDARD SCALAR 

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
scalar.fit(X_train) # We fit x_train and understand what type of values are present and store mean and std, here we calculate mean of both the feature columns (age, salary)

X_train_scaled = scalar.transform(X_train) # We take every value of X_train and transform them using the formula
X_test_scaled = scalar.transform(X_test)

# We learn(fit) only from train data  but we will transform both teh X_train and X_test data

mean = scalar.mean_
print(mean)


# Converting into dataframes rather than numpy array for better readability 
X_train_scaled = pd.DataFrame(X_train_scaled, columns = X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns = X_test.columns)

print(X_train_scaled)
print(X_test_scaled)

rounds = np.round(X_train.describe(), 1)
print(rounds)

rounds2 = np.round(X_train_scaled.describe(), 1)
print(rounds2)



# EFFECTS OF SCALING 

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
ax1.scatter(X_train['Age'], X_train['EstimatedSalary'])
ax1.set_title("Before Scaling")
ax2.scatter(X_train_scaled['Age'], X_train_scaled['EstimatedSalary'], color='red')
ax2.set_title("After Scaling")
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['Age'], ax=ax1)
sns.kdeplot(X_train['EstimatedSalary'], ax=ax1)
# after scaling
ax2.set_title('After Standard Scaling')
sns.kdeplot(X_train_scaled['Age'], ax=ax2)
sns.kdeplot(X_train_scaled['EstimatedSalary'], ax=ax2)
plt.show()


# COMPARISION OF DISTRIBUITON 
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Age Distribution Before Scaling')
sns.kdeplot(X_train['Age'], ax=ax1)
# after scaling
ax2.set_title('Age Distribution After Standard Scaling')
sns.kdeplot(X_train_scaled['Age'], ax=ax2)
plt.show()


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
# before scaling
ax1.set_title('Salary Distribution Before Scaling')
sns.kdeplot(X_train['EstimatedSalary'], ax=ax1)
# after scaling
ax2.set_title('Salary Distribution After Standard Scaling')
sns.kdeplot(X_train_scaled['EstimatedSalary'], ax=ax2)
plt.show()


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Logistic Regression
lr = LogisticRegression()
lr_scaled = LogisticRegression()

lr.fit(X_train, y_train)
lr_scaled.fit(X_train_scaled, y_train)

y_pred = lr.predict(X_test)
y_pred_scaled = lr_scaled.predict(X_test_scaled)

print("Logistic Regression")
print("Actual:", accuracy_score(y_test, y_pred))
print("Scaled:", accuracy_score(y_test, y_pred_scaled))

# Decision Tree
dt = DecisionTreeClassifier()
dt_scaled = DecisionTreeClassifier()

dt.fit(X_train, y_train)
dt_scaled.fit(X_train_scaled, y_train)

y_pred = dt.predict(X_test)
y_pred_scaled = dt_scaled.predict(X_test_scaled)

print("\nDecision Tree")
print("Actual:", accuracy_score(y_test, y_pred))
print("Scaled:", accuracy_score(y_test, y_pred_scaled))


print(df.describe())