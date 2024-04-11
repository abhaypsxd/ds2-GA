import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

cars = ['Toyota','Nissan','Honda','Mazda','Mitsubishi','Audi']

yearwise_cars = []

for i in range(2017,2024):  
    df = pd.read_csv(f"../csvs/{i}.csv")
    # df_mini = df.loc[df['Brand'] in cars]
    l1=[]
    for i in cars:
        df_mini = df.loc[(df['Brand'] == i)]
        index = df_mini.index.tolist()
        if len(index)==1:
            l1.append(df_mini['Total'].tolist())
        else:
            l1.append(df_mini.loc[[index[2]]]['Total'].tolist())
        
    final_cars = []
    for i in l1:
        final_cars.append(i[0])
    yearwise_cars.append(final_cars)

dict_list=[]
for i in yearwise_cars:
    dict1={}
    for j in range(len(i)):
        dict1[cars[j]]=i[j]
    dict_list.append(dict1)

df = pd.DataFrame(dict_list, index=range(2017,2024))
df.index.name='Year'
df.to_csv('../csvs/cars.csv')

