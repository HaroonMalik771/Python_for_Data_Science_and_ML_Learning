# Import cars data
import pandas as pd
cars = pd.read_csv('D:/Python/Python_for_Data_Science_and_ML_Learning/2_Intermediate_Python/4_loops/cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)