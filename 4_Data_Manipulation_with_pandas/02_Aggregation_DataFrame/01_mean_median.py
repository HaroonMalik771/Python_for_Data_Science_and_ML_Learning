import pandas as pd
import numpy as np

sales = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/02_Aggregation_DataFrame/sales.csv", index_col=0, header=0)
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())