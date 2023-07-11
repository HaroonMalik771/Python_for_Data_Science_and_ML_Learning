# Import cars data
import pandas as pd
cars = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/2_Dictionaries_and_pandas/cars.csv",index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])