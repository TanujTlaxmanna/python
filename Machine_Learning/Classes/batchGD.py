from sklearn.datasets import load_diabetes
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Load Dataset
X, y = load_diabetes(return_X_y=True)

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# ------------------- Linear Regression -------------------

reg = LinearRegression()
reg.fit(X_train, y_train)

print("\n------ Linear Regression ------")
print("Coefficients:")
print(reg.coef_)
print("Intercept:", reg.intercept_)

y_pred = reg.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))

# ------------------- Gradient Descent -------------------

class GDRegressor:

    def __init__(self, learning_rate=0.5, epochs=1000):
        self.coef_ = None
        self.intercept_ = None
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self, X_train, y_train):

        # Initialize Parameters
        self.intercept_ = 0
        self.coef_ = np.ones(X_train.shape[1])

        # Gradient Descent
        for i in range(self.epochs):

            y_hat = np.dot(X_train, self.coef_) + self.intercept_

            # Derivative of Intercept
            intercept_der = -2 * np.mean(y_train - y_hat)

            # Derivative of Coefficients
            coef_der = -2 * np.dot((y_train - y_hat), X_train) / X_train.shape[0]

            # Update Parameters
            self.intercept_ = self.intercept_ - self.lr * intercept_der
            self.coef_ = self.coef_ - self.lr * coef_der

            # Print every 100 epochs
            if (i + 1) % 100 == 0:
                print(f"Epoch {i+1}")
                print("Intercept:", self.intercept_)
                print("Coefficients:", self.coef_)
                print()

    def predict(self, X_test):
        return np.dot(X_test, self.coef_) + self.intercept_


# Train Gradient Descent Model
gdr = GDRegressor(learning_rate=0.5, epochs=1000)
gdr.fit(X_train, y_train)

print("------ Gradient Descent ------")
print("Final Intercept:", gdr.intercept_)
print("Final Coefficients:")
print(gdr.coef_)

y_pred = gdr.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))