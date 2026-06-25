import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("csv's/lr1.csv")

# Display the dataset
print(df)

# Plot the data
plt.scatter(df["area"], df["price"], color="blue", marker="+")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("Area vs Price")

# Create and train the model
reg = LinearRegression()
reg.fit(df[["area"]], df["price"])

# Plot the regression line
plt.plot(df["area"], reg.predict(df[["area"]]), color="red")
plt.show()

# Print model parameters
print("Slope (Coefficient):", reg.coef_[0])
print("Intercept:", reg.intercept_)

# Predict price for one house
new_data = pd.DataFrame({"area": [3300]})
predicted_price = reg.predict(new_data)

print("Predicted Price for 3300 sq ft:", predicted_price[0])

# Load new areas
d = pd.read_csv("csv's/lr1a.csv")
print(d.head())

# Predict prices for all areas
p = reg.predict(d)

# Add predictions to the DataFrame
d["price"] = p

# Display the DataFrame
print(d)

# Save to a new CSV file
d.to_csv("csv's/lr1b.csv", index=False)

print("File saved successfully!")