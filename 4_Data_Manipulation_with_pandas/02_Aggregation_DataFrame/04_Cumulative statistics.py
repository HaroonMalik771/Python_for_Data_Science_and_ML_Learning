import numpy as np
import pandas as pd


sales = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/02_Aggregation_DataFrame/sales.csv", index_col=0, header=0)

# A DataFrame called sales_1_1 which contains the sales data for department 1 of store 1
sales_1_1 = sales[(sales["store"] == 1) & (sales["department"] == 1)]

sales_1_1 = sales_1_1[['date', 'weekly_sales']]
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])