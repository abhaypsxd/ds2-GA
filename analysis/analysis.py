import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

df = pd.read_csv("../csvs/JPN[1].csv")
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

# print(category_list_index)

for i in range(len(category_list_index)-1):
    df1 = df.iloc[category_list_index[i]:category_list_index[i+1], :]
    category_wise_df.append(df1)

for i in category_wise_df:
    x = i['Maker/Brand'].tolist()
    y = i['Total'].tolist()
    dict1 = {}
    for i in range(len(x)):
        if x[i] not in dict1.keys():
            dict1[x[i]]=y[i]
    y1=list(dict1.values())
    for i in range(len(y1)):
        y1[i]=y1[i].replace(',','')
        if y1[i] =='-':
            y1[i]=0
    y2=list(map(int, y1))
    x = x[:-1]
    y2 = y2[:-1]
    

    fig = plt.figure(figsize=(10,6))
    gs = GridSpec(1,1)
    ax1 = fig.add_subplot(gs[0,0])
    ax1.bar(x,y2)
    ax1.set_xticklabels(x, rotation=90)
    ax1.set_title('category wise plots for 2018')
    plt.savefig('../images/category_wise_plot.png')