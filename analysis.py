import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("JPN[1].csv")
# print(df['Jan.'])

df_mini = df.iloc[0:18, :]
# print(df_mini)

category_list = df['Type'].dropna().tolist()
category_list_index = []
for i in range(len(category_list)):
    if category_list[i] != category_list[1]:
        category_list_index.append(i)
print(category_list_index)