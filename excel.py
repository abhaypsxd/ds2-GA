import pandas as pd

# Read the CSV data
df = pd.read_csv('2017.csv')

# Write the DataFrame to an Excel file
df.to_excel('2017.xlsx', index=False)