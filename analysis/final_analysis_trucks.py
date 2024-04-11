import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

trucks = ['Toyota','Nissan','Mitsubishi Fuso','Hino','Isuzu','UD Trucks (2008-)','UD Trucks']
trucks1 = ['Toyota','Nissan','Mitsubishi Fuso','Hino','Isuzu','UD Trucks']
yearwise_trucks = []
yearwise_trucks = []

for i in range(2017,2024):
    df=pd.read_csv(f'{i}.csv')
    l1=[]
    for i in trucks:
        df_mini = df.loc[(df['Brand'] == i)]
        index = df_mini.index.tolist()
        a = (df.loc[df['Name']=='Trucks'].index.tolist())
        b = (df.loc[df['Name']=='Buses'].index.tolist())
        for i in index:
            if i > a[0] and i < b[0]:
                l1.append(df_mini.loc[i]['Total'].tolist())
    yearwise_trucks.append(l1)
dict_list=[]
for i in yearwise_trucks:
    dict1={}
    for j in range(len(i)):
        dict1[trucks1[j]]=i[j]
    dict_list.append(dict1)

df = pd.DataFrame(dict_list, index=range(2017,2024))
df.index.name='Year'
df.to_csv('trucks.csv')

