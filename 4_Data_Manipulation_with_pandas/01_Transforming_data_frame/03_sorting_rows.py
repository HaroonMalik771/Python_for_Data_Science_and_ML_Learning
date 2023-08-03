import pandas as pd

homelessness = pd.read_csv("D:/Python/Python_for_Data_Science_and_ML_Learning/4_Data_Manipulation_with_pandas/01_Transforming_data_frame/homelessness.csv", index_col=0, header=0)
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members',ascending = False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending=[True,False])

# Print the top few rows
print(homelessness_reg_fam.head())