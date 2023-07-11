# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/2_Dictionaries_and_pandas/cars.csv",index_col = 0)

# Print out cars
print(cars)