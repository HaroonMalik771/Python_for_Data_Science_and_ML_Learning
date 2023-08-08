import pandas as pd
import numpy as np

sales = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/02_Aggregation_DataFrame/sales.csv", index_col=0, header=0)


# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())