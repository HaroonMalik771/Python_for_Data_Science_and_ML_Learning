# Import cars data
import pandas as pd
cars = pd.read_csv('D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/3_logic_control_flow_and_filtering/cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500

medium = cars[np.logical_and(cars['cars_per_cap'] > 100,cars['cars_per_cap'] < 500)]


# Print medium
print(medium)