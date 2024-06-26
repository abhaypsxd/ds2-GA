import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import statistics
from scipy import stats

df1 = pd.read_csv("../csvs/trucks.csv")
df2 = pd.read_csv("../csvs/cars.csv")

# mechanic:
# scale:
# 1. Very Low = <50,000
# 2. Low = 50,000 - 100,000
# 3. High = 100,000 - 250,000
# 4. High = 250,000 - 500,000
# 5. Very High = >500,000

combined_data_entities = []
df1_mini = df1['Toyota'].tolist()
df2_mini = df2['Toyota'].tolist()
combined_data_entities = df1_mini + df2_mini
#Sales Indicator
dict_frequency_scale = {1:0,2:0,3:0,4:0,5:0}
dict_percentage_scale = {1:0,2:0,3:0,4:0,5:0}
dict_cumulative_scale = {1:0,2:0,3:0,4:0,5:0}
data_entities_scale = []

for i in combined_data_entities:
    if i < 20000:
        dict_frequency_scale[1] += 1
        data_entities_scale.append(1)
    elif i >= 20000 and i < 50000:
        dict_frequency_scale[2] += 1
        data_entities_scale.append(2)
    elif i >= 50000 and i < 100000:
        dict_frequency_scale[3] += 1
        data_entities_scale.append(3)
    elif i >= 100000 and i < 250000:
        dict_frequency_scale[4] += 1
        data_entities_scale.append(4)
    else:
        dict_frequency_scale[5] += 1
        data_entities_scale.append(5)

for i in dict_frequency_scale:
    dict_percentage_scale[i] = (dict_frequency_scale[i]/len(combined_data_entities))*100

for i in dict_percentage_scale:
    dict_cumulative_scale[i] = dict_percentage_scale[i]
    for j in range(1,i):
        dict_cumulative_scale[i] += dict_percentage_scale[j]

#Descriptive Statistics
sample_size = len(data_entities_scale)
mean = statistics.mean(data_entities_scale)
median = statistics.median(data_entities_scale)
mode = statistics.mode(data_entities_scale)
variance = statistics.variance(data_entities_scale)
stdev = statistics.stdev(data_entities_scale)
min_value = min(data_entities_scale)
max_value = max(data_entities_scale)
range_value = max_value - min_value
interquartile_range = statistics.quantiles(data_entities_scale, n=4)
skewness = stats.skew(data_entities_scale)
kurtosis = stats.kurtosis(data_entities_scale)
confidence_low = mean+(1.96*(stdev/(len(data_entities_scale)**0.5)))
confidence_high = mean-(1.96*(stdev/(len(data_entities_scale)**0.5)))
confidence_interval = confidence_high-confidence_low
print("Descriptive Statistics")
print(f"Sample Size: {sample_size}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {stdev}")
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")
print(f"Range: {range_value}")
print(f"Interquartile Range: {interquartile_range}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")
print(f"Confidence Interval: {confidence_interval}")
print(f"Confidence Low: {confidence_low}")
print(f"Confidence High: {confidence_high}")

#Frequency Table
print("Frequency Table")
print("Scale\tFrequency")
for i in dict_frequency_scale:
    print(f"{i}\t{dict_frequency_scale[i]}")


#Graphs
fig = plt.figure(figsize=(10,6))
gs = GridSpec(1,1)
data_frequency_graph = {}
scale = ['Very Low','Low','Normal','High','Very High']
for i in dict_frequency_scale:
    data_frequency_graph[scale[i-1]] = dict_frequency_scale[i]
print(data_frequency_graph)
plt.bar(*zip(*data_frequency_graph.items()))
plt.savefig('../images/toyota_hist.png')

#Pie Chart
fig = plt.figure(figsize=(10,6))
gs = GridSpec(1,1)
plt.pie(dict_frequency_scale.values(), labels=scale)
plt.savefig('../images/toyota_pie.png')

#Histogram
fig = plt.figure(figsize=(10,6))
gs = GridSpec(1,1)
bin_edges = plt.hist(data_entities_scale, bins=5, edgecolor='black')
bin_midpoints = 0.5*(bin_edges[1][1:]+bin_edges[1][:-1])
plt.plot(bin_midpoints, bin_edges[0], color='b', marker='o', linestyle='--')
plt.savefig('../images/toyota_hist_with_line.png')


