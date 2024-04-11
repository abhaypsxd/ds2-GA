import pandas as pd


for i in range(2017,2024):
    # Read the CSV data
    df = pd.read_csv(f'{i}.csv')

    # Write the DataFrame to an Excel file
    df.to_excel(f'{i}.xlsx', index=False)