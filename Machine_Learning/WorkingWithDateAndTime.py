import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# ==========================================
# Dataset Paths
# ==========================================

ORDERS_PATH = "csv/orders.csv"
MESSAGES_PATH = "csv/messages.csv"

# ==========================================
# Load Datasets
# ==========================================

date = pd.read_csv(ORDERS_PATH)
time = pd.read_csv(MESSAGES_PATH)

print("Orders Dataset")
print(date.head())

print("\nMessages Dataset")
print(time.head())

# ==========================================
# Dataset Information
# ==========================================

print("\nOrders Info")
print(date.info())

print("\nMessages Info")
print(time.info())

# ==========================================
# Working with Dates
# ==========================================

date["date"] = pd.to_datetime(date["date"])

print("\nAfter Converting to Datetime")
print(date.info())

# ==========================================
# Extract Date Features
# ==========================================

# Year
date["date_year"] = date["date"].dt.year

# Month Number
date["date_month_no"] = date["date"].dt.month

# Month Name
date["date_month_name"] = date["date"].dt.month_name()

# Day
date["date_day"] = date["date"].dt.day

# Day of Week Number
date["date_dow"] = date["date"].dt.dayofweek

# Day Name
date["date_dow_name"] = date["date"].dt.day_name()

# Weekend
date["date_is_weekend"] = np.where(
    date["date_dow_name"].isin(["Saturday", "Sunday"]),
    1,
    0
)

# Week Number
date["date_week"] = date["date"].dt.isocalendar().week.astype(int)

# Quarter
date["quarter"] = date["date"].dt.quarter

# Semester
date["semester"] = np.where(
    date["quarter"].isin([1, 2]),
    1,
    2
)

print("\nExtracted Date Features")
print(
    date.drop(columns=["product_id", "city_id", "orders"]).head()
)

# ==========================================
# Time Difference from Today
# ==========================================

today = datetime.datetime.today()

print("\nDays Passed")
print((today - date["date"]).dt.days.head())

print("\nMonths Passed")
print(
    np.round(
        (today - date["date"]) / np.timedelta64(1, "M"),
        0
    ).head()
)

# ==========================================
# Working with Date-Time
# ==========================================

time["date"] = pd.to_datetime(time["date"])

print("\nDatetime Conversion")
print(time.info())

# Hour
time["hour"] = time["date"].dt.hour

# Minute
time["min"] = time["date"].dt.minute

# Second
time["sec"] = time["date"].dt.second

# Time Only
time["time"] = time["date"].dt.time

print("\nExtracted Time Features")
print(time.head())

# ==========================================
# Time Difference
# ==========================================

print("\nDifference from Today")
print((today - time["date"]).head())

print("\nDifference in Seconds")
print(
    ((today - time["date"]) / np.timedelta64(1, "s")).head()
)

print("\nDifference in Minutes")
print(
    ((today - time["date"]) / np.timedelta64(1, "m")).head()
)

print("\nDifference in Hours")
print(
    ((today - time["date"]) / np.timedelta64(1, "h")).head()
)

print("\nDifference in Days")
print(
    ((today - time["date"]) / np.timedelta64(1, "D")).head()
)