import numpy as np
from sklearn.datasets import load_diabetes

X,y = load_diabetes(return_X_y= True)

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

from sklearn.metrics import r2_score

r2_score(y_test, y_pred)
print(reg.coef_)
print(reg.intercept_)


# MAKING OUR OWN CLASS 

class MR:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        
    def fit(self,X_train,y_train):
        X_train = np.insert(X_train,0,1,axis=1)
        
        # calcuate the coeffs
        betas = np.linalg.inv(np.dot(X_train.T,X_train)).dot(X_train.T).dot(y_train)
        self.intercept_ = betas[0]
        self.coef_ = betas[1:]
    
    def predict(self,X_test):
        y_pred = np.dot(X_test,self.coef_) + self.intercept_
        return y_pred


lr = MR()
lr.fit(X_train, y_train)

print("X_train shape:", X_train.shape)
print("Shape after adding bias column:", np.insert(X_train, 0, 1, axis=1).shape)

y_pred = lr.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))

print("\nCoefficients:")
print(lr.coef_)

print("\nIntercept:")
print(lr.intercept_)