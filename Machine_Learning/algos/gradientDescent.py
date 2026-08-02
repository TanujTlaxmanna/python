from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Generate dataset
X, y = make_regression(
    n_samples=4,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=80,
    random_state=13
)

# Plot original data
plt.scatter(X, y)
plt.title("Original Data")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Ordinary Least Squares (OLS)
reg = LinearRegression()
reg.fit(X, y)

print("Slope (m):", reg.coef_[0])
print("Intercept (b):", reg.intercept_)

# Plot OLS regression line
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color="red", label="OLS")
plt.legend()
plt.show()

# Gradient Descent (Assume slope is fixed)
m = 78.35
b = 100

# Initial prediction
y_pred = (m * X + b).reshape(4)

plt.scatter(X, y)
plt.plot(X, reg.predict(X), color="red", label="OLS")
plt.plot(X, y_pred, color="green", label=f"b = {b}")
plt.legend()
plt.show()

# Learning rate
lr = 0.1

# ---------------- Iteration 1 ----------------
loss_slope = -2 * np.sum(y - m * X.ravel() - b)
step_size = loss_slope * lr
b = b - step_size

print("\nIteration 1")
print("Loss Slope:", loss_slope)
print("Step Size:", step_size)
print("New b:", b)

y_pred1 = (m * X + b).reshape(4)

plt.scatter(X, y)
plt.plot(X, reg.predict(X), color="red", label="OLS")
plt.plot(X, y_pred1, color="green", label=f"b = {b:.2f}")
plt.plot(X, y_pred, color="lightgreen", label="Initial")
plt.legend()
plt.show()

# ---------------- Iteration 2 ----------------
loss_slope = -2 * np.sum(y - m * X.ravel() - b)
step_size = loss_slope * lr
b = b - step_size

print("\nIteration 2")
print("Loss Slope:", loss_slope)
print("Step Size:", step_size)
print("New b:", b)

y_pred2 = (m * X + b).reshape(4)

plt.scatter(X, y)
plt.plot(X, reg.predict(X), color="red", label="OLS")
plt.plot(X, y_pred2, color="green", label=f"b = {b:.2f}")
plt.plot(X, y_pred1, color="lightgreen", label="Previous")
plt.plot(X, y_pred, color="#A3E4D7", label="Initial")
plt.legend()
plt.show()

# ---------------- Iteration 3 ----------------
loss_slope = -2 * np.sum(y - m * X.ravel() - b)
step_size = loss_slope * lr
b = b - step_size

print("\nIteration 3")
print("Loss Slope:", loss_slope)
print("Step Size:", step_size)
print("New b:", b)

y_pred3 = (m * X + b).reshape(4)

plt.figure(figsize=(10, 8))
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color="red", linewidth=2, label="OLS")
plt.plot(X, y_pred3, color="green", linewidth=2, label=f"Current b = {b:.2f}")
plt.plot(X, y_pred2, color="#82E0AA", label="Iteration 2")
plt.plot(X, y_pred1, color="#A9DFBF", label="Iteration 1")
plt.plot(X, y_pred, color="#D5F5E3", label="Initial")
plt.legend()
plt.title("Gradient Descent on Intercept")
plt.xlabel("X")
plt.ylabel("y")
plt.show()



b = -100
m = 78.35
lr = 0.01

epochs = 100

for i in range(epochs):
  loss_slope = -2 * np.sum(y - m*X.ravel() - b)
  b = b - (lr * loss_slope)

  y_pred = m * X + b

  plt.plot(X,y_pred)

plt.scatter(X,y)
plt.show()