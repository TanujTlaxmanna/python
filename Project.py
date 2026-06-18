import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

sales = pd.read_csv("Sales Data Sample.csv")
# print(sales)

# Which products generate the highest revenue?
highest_Revenue = sales.groupby("PRODUCTLINE")["SALES"].sum()
print(highest_Revenue ,"\n")
print(highest_Revenue.head())


plt.figure(figsize=(10, 8))
highest_Revenue.plot(kind='pie', autopct='%1.1f%%', startangle=90, explode=[0.1] + [0]*(len(highest_Revenue)-1))
plt.title("Revenue by Product Line", fontsize=16, fontweight='bold')
plt.savefig("Pie Chart.pdf", dpi = 2000, facecolor = 'lightpink', transparent = True, bbox_inches = "tight")
# plt.show()


# Which months have the highest sales?
monthly_sales = sales.groupby("MONTH_ID")["SALES"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot( kind="line", marker="o", linewidth=3, color="royalblue", markersize=8)
plt.title("Monthly Sales Trend", fontsize=18, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales Revenue", fontsize=12)
plt.grid(linestyle="--", alpha=0.5)
plt.savefig("Monthly_Sales_Trend.pdf", dpi=2000, facecolor="white", bbox_inches="tight")
# plt.show()


# Which category performs best?
category_sales=sales.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,8))
category_sales.plot(kind="pie",autopct="%1.1f%%",startangle=90)
plt.title("Revenue Share by Product Line",fontsize=18,fontweight="bold")
plt.ylabel("")
plt.savefig("Revenue_Share_By_Product_Line.pdf",dpi=2000,facecolor="white",bbox_inches="tight")
# plt.show()

# Which city contributes the most revenue?
country_sales=sales.groupby("COUNTRY")["SALES"].sum().sort_values()

plt.figure(figsize=(12,8))
country_sales.plot(kind="barh",color="teal")
plt.title("Revenue By Country",fontsize=18,fontweight="bold")
plt.xlabel("Revenue",fontsize=12)
plt.ylabel("Country",fontsize=12)
plt.grid(linestyle="--",alpha=0.5)
plt.savefig("Revenue_By_Country.pdf",dpi=2000,facecolor="white",bbox_inches="tight")
# plt.show()

# What are the top-selling products?
top_products=sales.groupby("PRODUCTCODE")["SALES"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_products.sort_values().plot(kind="barh",color="darkorange")
plt.title("Top 10 Products By Revenue",fontsize=18,fontweight="bold")
plt.xlabel("Revenue",fontsize=12)
plt.ylabel("Product Code",fontsize=12)
plt.grid(linestyle="--",alpha=0.5)
plt.savefig("Top_10_Products_By_Revenue.pdf",dpi=2000,facecolor="white",bbox_inches="tight")
# plt.show()

# Are sales increasing or decreasing over time?
yearly_sales=sales.groupby("YEAR_ID")["SALES"].sum()

plt.figure(figsize=(12,6))
yearly_sales.plot(kind="line",marker="o",linewidth=3,color="crimson",markersize=8)
plt.title("Yearly Sales Trend",fontsize=18,fontweight="bold")
plt.xlabel("Year",fontsize=12)
plt.ylabel("Sales Revenue",fontsize=12)
plt.grid(linestyle="--",alpha=0.5)
plt.savefig("Yearly_Sales_Trend.pdf",dpi=2000,facecolor="white",bbox_inches="tight")
# plt.show()