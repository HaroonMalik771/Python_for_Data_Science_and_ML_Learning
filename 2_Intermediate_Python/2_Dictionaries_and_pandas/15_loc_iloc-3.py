# Import cars data
import pandas as pd
cars = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/2_Dictionaries_and_pandas/cars.csv",index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame

print(cars.loc[:,['drives_right']])
# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])