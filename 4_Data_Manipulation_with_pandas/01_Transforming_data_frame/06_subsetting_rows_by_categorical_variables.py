import pandas as pd
import numpy as np

homelessness = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/01_Transforming_data_frame/homelessness.csv", index_col=0, header=0)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

regions = ["South Atlantic","Mid-Atlantic"]
south_mid_atlantic = homelessness["region"].isin(regions)
print(south_mid_atlantic)