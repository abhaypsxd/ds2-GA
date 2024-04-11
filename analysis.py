import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("JPN[1].csv")
# print(df['Jan.'])

df_mini = df.iloc[0:18, :]
# print(df_mini)

category_list = df['Type'].tolist()
category_list_values = df['Type'].dropna().tolist()
category_list_index = []
for i in range(len(category_list)):
    for j in category_list_values:
        if category_list[i] == j:
            category_list_index.append(i)
category_wise_df = []
for i in category_list_index:
    df1 = df.iloc[i:i+1, :]
    category_wise_df.append(df1)
for i in category_wise_df:
    print(i)