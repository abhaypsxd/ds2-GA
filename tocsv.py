import pandas as pd
for i in range(2017,2024):
    df = pd.read_csv(f'{i}.csv')
    fname = f'{i}.csv'
    final = ['Name','Group','Brand','Jan','Feb','Mar','Apr','May','Jun','First Half','Jul','Aug','Sep','Oct','Nov','Dec','Second Half','Adjusted Value','Total']
    initial = df.head(1).columns.tolist()
    for i in range(len(initial)):
        df.rename(columns={initial[i]:final[i]},inplace=True)
    df.to_csv(fname,index=False)