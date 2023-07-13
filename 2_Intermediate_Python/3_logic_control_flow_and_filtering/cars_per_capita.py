# Import cars data
import pandas as pd
cars = pd.read_csv('D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/3_logic_control_flow_and_filtering/cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500

car_maniac = cars[cars['cars_per_cap'] > 500]


# Print car_maniac
print(car_maniac)