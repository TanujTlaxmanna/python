import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Binarizer


def main():

    # ==============================
    # Load Dataset
    # ==============================
    df = pd.read_csv("csv's/titanic.csv")[["Age", "Fare", "SibSp", "Parch", "Survived"]]

    # Remove missing values
    df.dropna(inplace=True)

    # ==============================
    # Feature Engineering
    # ==============================
    df["family"] = df["SibSp"] + df["Parch"]
    df.drop(columns=["SibSp", "Parch"], inplace=True)

    # ==============================
    # Split Features and Target
    # ==============================
    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # ===========================================
    # WITHOUT BINARIZATION
    # ===========================================
    print("=" * 50)
    print("WITHOUT BINARIZATION")
    print("=" * 50)

    clf = DecisionTreeClassifier(random_state=42)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print(f"Test Accuracy              : {accuracy_score(y_test, y_pred):.4f}")

    cv_score = np.mean(
        cross_val_score(
            DecisionTreeClassifier(random_state=42),
            X,
            y,
            cv=10,
            scoring="accuracy"
        )
    )

    print(f"Cross Validation Accuracy  : {cv_score:.4f}")

    # ===========================================
    # APPLYING BINARIZATION
    # ===========================================
    print("\n" + "=" * 50)
    print("WITH BINARIZATION")
    print("=" * 50)

    trf = ColumnTransformer(
        [
            ("bin", Binarizer(copy=False), ["family"])
        ],
        remainder="passthrough"
    )

    X_train_trf = trf.fit_transform(X_train)
    X_test_trf = trf.transform(X_test)

    print("\nTransformed Data (First 5 Rows):")
    print(pd.DataFrame(X_train_trf, columns=["family", "Age", "Fare"]).head())

    clf = DecisionTreeClassifier(random_state=42)

    clf.fit(X_train_trf, y_train)

    y_pred2 = clf.predict(X_test_trf)

    print(f"\nTest Accuracy              : {accuracy_score(y_test, y_pred2):.4f}")

    X_trf = trf.fit_transform(X)

    cv_score_bin = np.mean(
        cross_val_score(
            DecisionTreeClassifier(random_state=42),
            X_trf,
            y,
            cv=10,
            scoring="accuracy"
        )
    )

    print(f"Cross Validation Accuracy  : {cv_score_bin:.4f}")


if __name__ == "__main__":
    main()