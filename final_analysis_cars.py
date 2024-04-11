import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

cars = ['Toyota','Nissan','Honda','Mazda','Mitsubishi','Audi']

yearwise_cars = []

for i in range(2017,2024):  
    df = pd.read_csv(f"{i}.csv")
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

print(yearwise_cars)
