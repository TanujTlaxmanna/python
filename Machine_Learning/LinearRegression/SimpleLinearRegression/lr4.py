import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("csv's\\placements.csv")

# Display first 5 rows
print(df.head())

# Scatter plot
plt.scatter(df["cgpa"], df["package"])
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")
plt.show()

# Features and target
X = df.iloc[:, 0:1]
y = df.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# Train model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Model parameters
m = lr.coef_[0]
b = lr.intercept_

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict first test sample
prediction = lr.predict(X_test.iloc[0].values.reshape(1, 1))
print("Prediction for first test sample:", prediction[0])

# Regression line
plt.scatter(df["cgpa"], df["package"], label="Data")
plt.plot(X_train, lr.predict(X_train), color="red", label="Regression Line")
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")
plt.legend()
plt.show()

# Manual predictions using y = mx + b
cgpa = 8.58
package = m * cgpa + b
print(f"Package for CGPA {cgpa}: {package:.2f} LPA")

cgpa = 9.5
package = m * cgpa + b
print(f"Package for CGPA {cgpa}: {package:.2f} LPA")

cgpa = 100
package = m * cgpa + b
print(f"Package for CGPA {cgpa}: {package:.2f} LPA")


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = lr.predict(X_test)
print(y_test.values)

print("Mean Absolute Error ", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error ", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error " , np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score ", r2_score(y_test, y_pred))

# ADJUSTED R2 SCORE

r2 = r2_score(y_test, y_pred)

print(X_test.shape)
r2_adj = 1 - ((1-r2)* (40-1)/(40-1-1))
print(r2_adj)