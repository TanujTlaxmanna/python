import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Dataset Path
# ==============================
DATASET_PATH = "csv's/titanic.csv"

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv(DATASET_PATH)

print(df.head())

# ==========================================================
# Exploring the 'number' Column
# ==========================================================

print("\nUnique values in 'number' column:")
print(df["number"].unique())

fig = df["number"].value_counts().plot.bar()
fig.set_title("Passengers Travelling With")
plt.show()

# ==========================================================
# Extract Numerical & Categorical Parts from 'number'
# ==========================================================

df["number_numerical"] = pd.to_numeric(
    df["number"],
    errors="coerce",
    downcast="integer"
)

df["number_categorical"] = np.where(
    df["number_numerical"].isnull(),
    df["number"],
    np.nan
)

print("\nDataset after extracting 'number':")
print(df.head())

# ==========================================================
# Exploring Cabin Column
# ==========================================================

print("\nUnique Cabin Values:")
print(df["Cabin"].unique())

# Extract cabin number
df["cabin_num"] = df["Cabin"].str.extract("(\d+)")

# Extract cabin category (first letter)
df["cabin_cat"] = df["Cabin"].str[0]

print("\nDataset after Cabin Extraction:")
print(df.head())

print("\nCabin Category Counts:")
print(df["cabin_cat"].value_counts())

df["cabin_cat"].value_counts().plot(kind="bar")
plt.title("Cabin Categories")
plt.xlabel("Cabin Category")
plt.ylabel("Count")
plt.show()

# ==========================================================
# Exploring Ticket Column
# ==========================================================

print("\nUnique Ticket Values:")
print(df["Ticket"].unique())

# Extract ticket number
df["ticket_num"] = df["Ticket"].apply(lambda x: x.split()[-1])

df["ticket_num"] = pd.to_numeric(
    df["ticket_num"],
    errors="coerce",
    downcast="integer"
)

# Extract ticket category
df["ticket_cat"] = df["Ticket"].apply(lambda x: x.split()[0])

df["ticket_cat"] = np.where(
    df["ticket_cat"].str.isdigit(),
    np.nan,
    df["ticket_cat"]
)

print("\nFirst 20 Rows:")
print(df.head(20))

print("\nUnique Ticket Categories:")
print(df["ticket_cat"].unique())