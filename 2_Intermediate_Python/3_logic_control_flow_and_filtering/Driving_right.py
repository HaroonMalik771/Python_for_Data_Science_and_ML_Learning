# Import cars data
import pandas as pd
cars = pd.read_csv('D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/3_logic_control_flow_and_filtering/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel

sel = cars[dr]
# Print sel
print(sel)