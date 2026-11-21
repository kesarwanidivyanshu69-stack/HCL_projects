Name:Divyanshu kesarwani
addmission no. 2026b15410136
Git link :https://github.com/kesarwanidivyanshu69-stack/HCL_projects.git



"""Retail Store Sales Analysis using 30 sample transactions."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_sales_data_30.csv", parse_dates=["Date"])
df = df.drop_duplicates().dropna(subset=["Date","Product","Category","Quantity","Sales","Profit"])
df = df[(df["Quantity"] > 0) & (df["Sales"] >= 0)]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("RETAIL STORE SALES ANALYSIS - 30 RECORDS")
print("Total Sales: ₹{:,.2f}".format(df["Sales"].sum()))
print("Total Profit: ₹{:,.2f}".format(df["Profit"].sum()))
print("Total Orders:", df["Order_ID"].nunique())
print("Unique Customers:", df["Customer_ID"].nunique())
print("Units Sold:", df["Quantity"].sum())
print("Average Order Value: ₹{:,.2f}".format(df["Sales"].sum()/df["Order_ID"].nunique()))

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()
location_sales = df.groupby("Store_Location")["Sales"].sum().sort_values(ascending=False)
payment_sales = df.groupby("Payment_Mode")["Sales"].sum().sort_values(ascending=False)

print("\\nSales by category:\\n", category_sales)
print("\\nTop products:\\n", product_sales.head(10))
print("\\nMonthly sales:\\n", monthly_sales)
print("\\nSales by location:\\n", location_sales)
print("\\nSales by payment mode:\\n", payment_sales)

category_sales.to_csv("category_sales_summary.csv", header=["Total_Sales"])
product_sales.head(10).to_csv("top_products_summary.csv", header=["Total_Sales"])
monthly_sales.to_csv("monthly_sales_summary.csv", header=["Total_Sales"])
location_sales.to_csv("location_sales_summary.csv", header=["Total_Sales"])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9,5))
category_sales.plot(kind="bar", title="Sales by Category", ylabel="Sales (₹)")
plt.tight_layout(); plt.savefig("sales_by_category.png", dpi=150); plt.show()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend", ylabel="Sales (₹)")
plt.xticks(rotation=45); plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150); plt.show()

plt.figure(figsize=(9,5))
location_sales.plot(kind="bar", title="Sales by Store Location", ylabel="Sales (₹)")
plt.tight_layout(); plt.savefig("sales_by_location.png", dpi=150); plt.show()

plt.figure(figsize=(7,5))
payment_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales by Payment Mode", ylabel="")
plt.tight_layout(); plt.savefig("payment_mode_share.png", dpi=150); plt.show()
