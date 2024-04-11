import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

total = []
for i in range(2017,2024):

    df = pd.read_csv(f'{i}.csv')
    total.append(df['Total'].sum())
plt.bar(range(2017,2024),total)
plt.title('Total sales from 2017 to 2023')
plt.show()