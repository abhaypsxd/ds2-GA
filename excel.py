import pandas as pd

for i in range(2017,2024):

# Read the CSV data
df = pd.read_csv('JPN[1].csv')

# Write the DataFrame to an Excel file
df.to_excel('JPN.xlsx', index=False)