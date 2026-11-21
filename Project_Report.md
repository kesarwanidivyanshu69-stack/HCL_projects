NAME: divyanshu
ADMISSION NO:2026b15410136
Branch:DS-2
Program name:Data analytics
Project: Project1- Reatail sales performance analysis
Git Repository-https://github.com/kesarwanidivyanshu69-stack/HCL_projects.git



# Retail Store Sales Analysis – 30 Records

## Introduction
This project analyses a small retail dataset of exactly 30 sample transactions using Python and Excel.

## Problem Statement
Retail transaction records contain useful information, but it can be difficult to identify sales trends, profitable categories, popular products, and store performance without analysis.

## Objectives
- Calculate total sales, profit, orders, customers, and units sold.
- Compare product categories and products.
- Analyse monthly sales trends.
- Compare store locations and payment modes.
- Present findings using charts and summary tables.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Excel, and VS Code/Jupyter Notebook.

## Dataset
The CSV file contains exactly 30 synthetically generated transactions for academic demonstration. It is not real retailer or customer data.

## Important Columns
Order_ID, Date, Customer_ID, Gender, Age, Product, Category, Quantity, Unit_Price, Unit_Cost, Discount, Sales, Profit, Payment_Mode, Store_Location.

## Formulas
- Sales = Quantity × Unit Price × (1 − Discount)
- Profit = Sales − (Quantity × Unit Cost)
- Average Order Value = Total Sales ÷ Total Orders
- Profit Margin = (Total Profit ÷ Total Sales) × 100

## Methodology
1. Load the CSV using Pandas.
2. Check missing values and remove duplicate records.
3. Validate quantity and sales values.
4. Group data by category, product, month, location, and payment mode.
5. Calculate KPIs and create visualizations.
6. Export summary tables to CSV and Excel.

## Results from the 30 sample records
- Number of records: 30
- Total Sales: ₹41,723.48
- Total Profit: ₹17,301.45
- Highest-sales category: Home & Kitchen (₹19,586.34)
- Highest-sales location: Delhi (₹11,573.91)
- Top product by sales: Bedsheet (₹8,328.84)

## Recommendations
- Keep sufficient stock of products with strong sales.
- Review products and categories with low sales.
- Compare revenue and profit before offering discounts.
- Monitor monthly and location-wise performance.
- Use the findings as an initial indication, not as a final business decision, because the sample is small.

## Limitations
The dataset is synthetic and contains only 30 records. It is suitable for a small academic demonstration, but conclusions may not represent the performance of a real retail business.

## Conclusion
This project demonstrates how Python and Excel can analyse retail sales data. It calculates key business metrics, compares products and locations, and visualizes sales trends using a small dataset of 30 transactions.

## How to Run
Install dependencies:
`pip install pandas numpy matplotlib seaborn openpyxl`

Run:
`python retail_sales_analysis.py`
