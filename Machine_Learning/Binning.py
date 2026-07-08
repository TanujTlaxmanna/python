import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.compose import ColumnTransformer

# ==============================
# Load Dataset
# ==============================

df = pd.read_csv("csv's\\titanic.csv", usecols=["Age", "Fare", "Survived"])
df.dropna(inplace=True)

print("Dataset Shape:", df.shape)
print(df.head())

# ==============================
# Split Features and Target
# ==============================

X = df.iloc[:, 1:]
y = df.iloc[:, 0]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================
# Without Discretization
# ==============================

print("\n" + "=" * 50)
print("WITHOUT DISCRETIZATION")
print("=" * 50)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Test Accuracy:",
      accuracy_score(y_test, y_pred))

print("Cross Validation Accuracy:",
      np.mean(
          cross_val_score(
              DecisionTreeClassifier(random_state=42),
              X,
              y,
              cv=10,
              scoring="accuracy"
          )
      ))

# ==============================
# Apply KBinsDiscretizer
# ==============================

kbin_age = KBinsDiscretizer(
    n_bins=15,
    encode="ordinal",
    strategy="quantile"
)

kbin_fare = KBinsDiscretizer(
    n_bins=15,
    encode="ordinal",
    strategy="quantile"
)

trf = ColumnTransformer([
    ("age_bin", kbin_age, [0]),
    ("fare_bin", kbin_fare, [1])
])

X_train_trf = trf.fit_transform(X_train)
X_test_trf = trf.transform(X_test)

print("\nAge Bin Edges:")
print(trf.named_transformers_["age_bin"].bin_edges_[0])

print("\nFare Bin Edges:")
print(trf.named_transformers_["fare_bin"].bin_edges_[0])

# ==============================
# Display Transformed Data
# ==============================

output = pd.DataFrame({
    "Age": X_train["Age"],
    "Age_Bin": X_train_trf[:, 0],
    "Fare": X_train["Fare"],
    "Fare_Bin": X_train_trf[:, 1]
})

output["Age_Label"] = pd.cut(
    X_train["Age"],
    bins=trf.named_transformers_["age_bin"].bin_edges_[0]
)

output["Fare_Label"] = pd.cut(
    X_train["Fare"],
    bins=trf.named_transformers_["fare_bin"].bin_edges_[0]
)

print("\nSample Output:")
print(output.sample(5))

# ==============================
# Decision Tree After Discretization
# ==============================

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_trf, y_train)

y_pred2 = clf.predict(X_test_trf)

print("\n" + "=" * 50)
print("WITH DISCRETIZATION")
print("=" * 50)

print("Test Accuracy:",
      accuracy_score(y_test, y_pred2))

X_trf = trf.fit_transform(X)

print("Cross Validation Accuracy:",
      np.mean(
          cross_val_score(
              DecisionTreeClassifier(random_state=42),
              X_trf,
              y,
              cv=10,
              scoring="accuracy"
          )
      ))

# ==============================
# Function to Compare Strategies
# ==============================

def discretize(bins, strategy):

    kbin_age = KBinsDiscretizer(
        n_bins=bins,
        encode="ordinal",
        strategy=strategy
    )

    kbin_fare = KBinsDiscretizer(
        n_bins=bins,
        encode="ordinal",
        strategy=strategy
    )

    trf = ColumnTransformer([
        ("age", kbin_age, [0]),
        ("fare", kbin_fare, [1])
    ])

    X_trf = trf.fit_transform(X)

    score = np.mean(
        cross_val_score(
            DecisionTreeClassifier(random_state=42),
            X_trf,
            y,
            cv=10,
            scoring="accuracy"
        )
    )

    print(f"\nStrategy: {strategy}")
    print(f"Bins: {bins}")
    print(f"Cross Validation Accuracy: {score:.4f}")

    # Age Histogram
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(X["Age"])
    plt.title("Age Before")

    plt.subplot(1, 2, 2)
    plt.hist(X_trf[:, 0], color="red")
    plt.title("Age After")

    plt.tight_layout()
    plt.show()

    # Fare Histogram
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(X["Fare"])
    plt.title("Fare Before")

    plt.subplot(1, 2, 2)
    plt.hist(X_trf[:, 1], color="green")
    plt.title("Fare After")

    plt.tight_layout()
    plt.show()


# ==============================
# Try Different Strategies
# ==============================

discretize(5, "uniform")
discretize(5, "quantile")
discretize(5, "kmeans")