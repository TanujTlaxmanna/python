from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generate dataset
X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=20,
    random_state=13
)

# Visualize dataset
plt.scatter(X, y)
plt.title("Generated Dataset")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# ------------------ Linear Regression ------------------
lr = LinearRegression()
lr.fit(X_train, y_train)

print("Linear Regression")
print("Slope (m):", lr.coef_[0])
print("Intercept (b):", lr.intercept_)

y_pred = lr.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))

# ------------------ Gradient Descent ------------------
class GDRegressor:

    def __init__(self, learning_rate, epochs):
        self.m = 100
        self.b = -120
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self, X, y):

        for i in range(self.epochs):

            loss_slope_b = -2 * np.sum(y - self.m * X.ravel() - self.b)
            loss_slope_m = -2 * np.sum((y - self.m * X.ravel() - self.b) * X.ravel())

            self.b = self.b - (self.lr * loss_slope_b)
            self.m = self.m - (self.lr * loss_slope_m)

        print("\nGradient Descent")
        print("Slope (m):", self.m)
        print("Intercept (b):", self.b)

    def predict(self, X):
        return self.m * X + self.b


gd = GDRegressor(learning_rate=0.001, epochs=50)
gd.fit(X_train, y_train)

y_pred = gd.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))

# ------------------ Comparison Plot ------------------
plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, lr.predict(X_test), color="red", label="Linear Regression")
plt.plot(X_test, gd.predict(X_test), color="green", linestyle="--", label="Gradient Descent")

plt.title("Linear Regression vs Gradient Descent")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()