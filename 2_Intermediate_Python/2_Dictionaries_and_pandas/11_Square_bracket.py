# Import cars data
import pandas as pd
cars = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/2_Dictionaries_and_pandas/cars.csv",index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])