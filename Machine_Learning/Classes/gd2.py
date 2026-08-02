from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generate Dataset
X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    noise=20,
    random_state=13
)

# Visualize Dataset
plt.scatter(X, y)
plt.title("Generated Dataset")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# ---------------------- Ordinary Least Squares ----------------------

lr = LinearRegression()
lr.fit(X_train, y_train)

print("------ Linear Regression ------")
print("Slope (m):", lr.coef_[0])
print("Intercept (b):", lr.intercept_)

y_pred = lr.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))

# ---------------------- Gradient Descent ----------------------

class GDRegressor:

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.m = 0
        self.b = 0
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self, X, y):

        X = X.ravel()
        n = len(X)

        for i in range(self.epochs):

            # Prediction
            y_pred = self.m * X + self.b

            # Derivatives
            dm = (-2 / n) * np.sum((y - y_pred) * X)
            db = (-2 / n) * np.sum(y - y_pred)

            # Update Parameters
            self.m = self.m - self.lr * dm
            self.b = self.b - self.lr * db

            # Print every 100 epochs
            if (i + 1) % 100 == 0:
                print(f"Epoch {i+1}: m = {self.m:.4f}, b = {self.b:.4f}")

    def predict(self, X):
        return self.m * X + self.b


# Train Gradient Descent Model
gd = GDRegressor(learning_rate=0.01, epochs=1000)
gd.fit(X_train, y_train)

print("\n------ Gradient Descent ------")
print("Slope (m):", gd.m)
print("Intercept (b):", gd.b)

y_pred_gd = gd.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred_gd))

# ---------------------- Comparison Plot ----------------------

plt.scatter(X_test, y_test, color="blue", label="Actual Data")

plt.plot(
    X_test,
    lr.predict(X_test),
    color="red",
    linewidth=2,
    label="Linear Regression"
)

plt.plot(
    X_test,
    gd.predict(X_test),
    color="green",
    linestyle="--",
    linewidth=2,
    label="Gradient Descent"
)

plt.title("Linear Regression vs Gradient Descent")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()