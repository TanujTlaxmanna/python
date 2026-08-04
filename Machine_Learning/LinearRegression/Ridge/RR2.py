from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np

# Generate Dataset
X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=20,
    random_state=13
)

# -------------------- Scikit-Learn Models --------------------

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)

print("Linear Regression")
print("Coefficient:", lr.coef_)
print("Intercept:", lr.intercept_)

from sklearn.linear_model import Ridge

rr = Ridge(alpha=10)
rr.fit(X, y)

print("\nRidge Regression (alpha=10)")
print("Coefficient:", rr.coef_)
print("Intercept:", rr.intercept_)

rr1 = Ridge(alpha=100)
rr1.fit(X, y)

print("\nRidge Regression (alpha=100)")
print("Coefficient:", rr1.coef_)
print("Intercept:", rr1.intercept_)

# -------------------- Custom Ridge Regression --------------------

class MeraRidge:

    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.m = None
        self.b = None

    def fit(self, X_train, y_train):

        # Convert to 1D array
        X_train = X_train.ravel()

        x_mean = X_train.mean()
        y_mean = y_train.mean()

        num = 0
        den = 0

        for i in range(len(X_train)):
            num += (y_train[i] - y_mean) * (X_train[i] - x_mean)
            den += (X_train[i] - x_mean) ** 2

        self.m = num / (den + self.alpha)
        self.b = y_mean - self.m * x_mean

        print("\nCustom Ridge Regression")
        print("Slope:", self.m)
        print("Intercept:", self.b)

    def predict(self, X_test):
        X_test = X_test.ravel()
        return self.m * X_test + self.b


reg = MeraRidge(alpha=100)
reg.fit(X, y)

# -------------------- Plot --------------------

plt.figure(figsize=(10, 6))

plt.scatter(X, y, color='blue', label='Data')

# Sort values for smooth plotting
idx = np.argsort(X[:, 0])
X_sorted = X[idx]

plt.plot(X_sorted, lr.predict(X_sorted), color='red', linewidth=2, label='Linear Regression (alpha=0)')
plt.plot(X_sorted, rr.predict(X_sorted), color='green', linewidth=2, label='Ridge (alpha=10)')
plt.plot(X_sorted, rr1.predict(X_sorted), color='orange', linewidth=2, label='Ridge (alpha=100)')
plt.plot(X_sorted, reg.predict(X_sorted), color='purple', linewidth=2, linestyle='--', label='Custom Ridge (alpha=100)')

plt.title("Linear Regression vs Ridge Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()