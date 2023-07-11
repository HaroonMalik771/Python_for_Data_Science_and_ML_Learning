# Import cars data
import pandas as pd
cars = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/2_Dictionaries_and_pandas/cars.csv",index_col = 0)

# Print out drives_right value of Morocco

print(cars.loc['MOR','drives_right'])
# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
