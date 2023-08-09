import pandas as pd

# Print the head of the homelessness Data

homelessness = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/01_Transforming_data_frame/homelessness.csv", index_col=0, header=0)

print(homelessness.head())
# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
