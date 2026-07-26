from sklearn.datasets import make_regression
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X, y = make_regression(
    n_samples=100,
    n_features=2,
    n_informative=2,
    noise=50,
    random_state=42
)

df = pd.DataFrame({
    "feature1": X[:, 0],
    "feature2": X[:, 1],
    "target": y
})

fig = px.scatter_3d(df, x="feature1", y="feature2", z="target")
fig.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=3
)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

x = np.linspace(df["feature1"].min(), df["feature1"].max(), 20)
y = np.linspace(df["feature2"].min(), df["feature2"].max(), 20)

xGrid, yGrid = np.meshgrid(x, y)

final = np.c_[xGrid.ravel(), yGrid.ravel()]
z = lr.predict(final).reshape(xGrid.shape)

fig = px.scatter_3d(df, x="feature1", y="feature2", z="target")

fig.add_trace(
    go.Surface(
        x=x,
        y=y,
        z=z,
        opacity=0.6
    )
)

fig.show()

print("Coefficients:", lr.coef_)
print("Intercept:", lr.intercept_)