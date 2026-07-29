import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load Dataset
df = pd.read_csv("csv's\\data.csv")

print(df.head())

# Features and Target
X = df.iloc[:, 0:3].values
y = df.iloc[:, -1].values

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predictions
y_pred = model.predict(X_test)

# Residuals
residual = y_test - y_pred

# =====================================================
# 1. Linear Relationship
# =====================================================

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

ax1.scatter(df["feature1"], df["target"])
ax1.set_title("Feature1 vs Target")
ax1.set_xlabel("Feature1")
ax1.set_ylabel("Target")

ax2.scatter(df["feature2"], df["target"])
ax2.set_title("Feature2 vs Target")
ax2.set_xlabel("Feature2")
ax2.set_ylabel("Target")

ax3.scatter(df["feature3"], df["target"])
ax3.set_title("Feature3 vs Target")
ax3.set_xlabel("Feature3")
ax3.set_ylabel("Target")

plt.tight_layout()
plt.show()

# =====================================================
# 2. Multicollinearity (VIF)
# =====================================================

vif = []

for i in range(X_train.shape[1]):
    vif.append(variance_inflation_factor(X_train, i))

vif_df = pd.DataFrame({
    "Feature": df.columns[:3],
    "VIF": vif
})

print("\nVariance Inflation Factor")
print(vif_df)

# Correlation Heatmap

plt.figure(figsize=(6, 5))
sns.heatmap(df.iloc[:, 0:3].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# =====================================================
# 3. Normality of Residuals
# =====================================================

sns.displot(residual, kind="kde", height=4, aspect=1.5)
plt.title("Residual Distribution")
plt.show()

# QQ Plot

fig, ax = plt.subplots(figsize=(6, 4))
sp.stats.probplot(residual, plot=ax)
plt.title("QQ Plot")
plt.show()

# =====================================================
# 4. Homoscedasticity
# =====================================================

plt.figure(figsize=(6, 4))
plt.scatter(y_pred, residual)
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")
plt.show()

# =====================================================
# 5. Autocorrelation of Residuals
# =====================================================

plt.figure(figsize=(10, 4))
plt.plot(residual, marker="o")
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Observation")
plt.ylabel("Residual")
plt.title("Residual Plot")
plt.grid(True)
plt.show()