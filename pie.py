import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

df = pd.read_csv("JPN[1].csv")

category_list = df['Type'].tolist()
category_list_values = df['Type'].dropna().tolist()
category_list_index = []
for i in range(len(category_list)):
    for j in category_list_values:
        if category_list[i] == j:
            category_list_index.append(i)

values = []

for i in category_list_index:
    values.append(df.iloc[i-1]['Total'])

for i in range(len(values)):
    values[i]=values[i].replace(',','')
print(values)

plt.pie(values, labels= category_list_values)
plt.show()