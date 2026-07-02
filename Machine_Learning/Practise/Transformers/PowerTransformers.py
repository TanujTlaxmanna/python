import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as stats

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PowerTransformer

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("csv's\\concrete_data.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDescription:")
print(df.describe())

# ==========================
# Splitting Dataset
# ==========================

X = df.drop(columns=["Strength"])
y = df["Strength"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# Linear Regression WITHOUT Transformation
# =====================================================

print("\n---------------- WITHOUT TRANSFORMATION ----------------")

lr = LinearRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))

cv_score = np.mean(cross_val_score(lr, X, y, scoring='r2', cv=10))
print("Cross Validation Score:", cv_score)

# =====================================================
# Distribution Before Transformation
# =====================================================

for col in X_train.columns:

    plt.figure(figsize=(14,4))

    plt.subplot(121)
    sns.histplot(X_train[col], kde=True)
    plt.title(col + " Distribution")

    plt.subplot(122)
    stats.probplot(X_train[col], dist="norm", plot=plt)
    plt.title(col + " QQ Plot")

    plt.tight_layout()
    plt.show()

# =====================================================
# BOX COX TRANSFORMATION
# =====================================================

print("\n---------------- BOX COX TRANSFORMATION ----------------")

pt = PowerTransformer(method="box-cox")

# Box-Cox only accepts positive values
X_train_box = pt.fit_transform(X_train + 0.000001)
X_test_box = pt.transform(X_test + 0.000001)

lambda_df = pd.DataFrame({
    "Columns": X_train.columns,
    "Box-Cox Lambda": pt.lambdas_
})

print("\nBox-Cox Lambdas")
print(lambda_df)

# =====================================================
# Linear Regression After Box-Cox
# =====================================================

lr = LinearRegression()

lr.fit(X_train_box, y_train)

y_pred_box = lr.predict(X_test_box)

print("\nR2 Score After Box-Cox:", r2_score(y_test, y_pred_box))

# Cross Validation

X_box = pt.fit_transform(X + 0.000001)

cv_box = np.mean(
    cross_val_score(
        lr,
        X_box,
        y,
        scoring="r2",
        cv=10
    )
)

print("Cross Validation Score:", cv_box)

# =====================================================
# Before and After Distribution (Box-Cox)
# =====================================================

X_train_box = pd.DataFrame(
    X_train_box,
    columns=X_train.columns
)

for col in X_train.columns:

    plt.figure(figsize=(14,4))

    plt.subplot(121)
    sns.histplot(X_train[col], kde=True)
    plt.title(col + " Before Box-Cox")

    plt.subplot(122)
    sns.histplot(X_train_box[col], kde=True)
    plt.title(col + " After Box-Cox")

    plt.tight_layout()
    plt.show()

# =====================================================
# YEO-JOHNSON TRANSFORMATION
# =====================================================

print("\n---------------- YEO JOHNSON TRANSFORMATION ----------------")

pt2 = PowerTransformer(method="yeo-johnson")

X_train_yeo = pt2.fit_transform(X_train)
X_test_yeo = pt2.transform(X_test)

lambda_df2 = pd.DataFrame({
    "Columns": X_train.columns,
    "Yeo-Johnson Lambda": pt2.lambdas_
})

print("\nYeo-Johnson Lambdas")
print(lambda_df2)

# =====================================================
# Linear Regression After Yeo-Johnson
# =====================================================

lr = LinearRegression()

lr.fit(X_train_yeo, y_train)

y_pred_yeo = lr.predict(X_test_yeo)

print("\nR2 Score After Yeo-Johnson:", r2_score(y_test, y_pred_yeo))

# Cross Validation

X_yeo = pt2.fit_transform(X)

cv_yeo = np.mean(
    cross_val_score(
        lr,
        X_yeo,
        y,
        scoring="r2",
        cv=10
    )
)

print("Cross Validation Score:", cv_yeo)

# =====================================================
# Before and After Distribution (Yeo-Johnson)
# =====================================================

X_train_yeo = pd.DataFrame(
    X_train_yeo,
    columns=X_train.columns
)

for col in X_train.columns:

    plt.figure(figsize=(14,4))

    plt.subplot(121)
    sns.histplot(X_train[col], kde=True)
    plt.title(col + " Before Yeo-Johnson")

    plt.subplot(122)
    sns.histplot(X_train_yeo[col], kde=True)
    plt.title(col + " After Yeo-Johnson")

    plt.tight_layout()
    plt.show()

# =====================================================
# Lambda Comparison
# =====================================================

comparison = pd.DataFrame({
    "Columns": X_train.columns,
    "Box-Cox Lambda": pt.lambdas_,
    "Yeo-Johnson Lambda": pt2.lambdas_
})

print("\nLambda Comparison")
print(comparison)