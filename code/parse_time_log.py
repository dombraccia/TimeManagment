import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

'''
DESCRIPTION
'''

## take input from standard input
time_file = sys.argv[1] ## ex:

## load dataset(s)
df = pd.read_csv(time_file, sep = ',')

## process data

### creating a separate column with just date created
date_time = df['Created At'].str.split(' ', expand = True)
date_time.columns = ['date', 'time']
df['date'] = date_time['date']
df['time'] = date_time['time']

### converting Elapsed Time column to datetime format
df['elapsed_time'] = pd.to_datetime(df['Elapsed Time'])
df['hours_elapsed'] = (df.elapsed_time.dt.hour + df.elapsed_time.dt.minute/60 + df.elapsed_time.dt.second / 3600)

### grouping data by relevant variables
mat = df.groupby(['date', 'Text'])['hours_elapsed'].sum().unstack().fillna(0)
# print(mat)

## plot data
# pal = sns.color_palette("Set2", as_cmap = False)
pal = sns.color_palette("pastel", mat.shape[1])

mat.plot(kind = 'bar', stacked = True, color = pal)
# mat.plot(kind = 'bar', stacked = True)
plt.legend(loc = 'best', bbox_to_anchor = (1.0, 1.00))
plt.title('Hours spent on different projects')
plt.ylabel('hours spent')
plt.xticks(rotation = 45, ha = 'center')
plt.tight_layout()

## output data to excel or plotting software
time_period = time_file.split('/')[1].split('.')[0]
# print(time_period)
plot_path = 'plots/' + time_period + '.png'
plt.savefig(plot_path)
print('plot saved to: ' + plot_path)
