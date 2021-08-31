# import something
import sys
import numpy
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

'''
DESCRIPTION
'''

## take input from standard input
today_csv = sys.argv[1] ## ex: 

## load dataset(s)
df_today = pd.read_csv(('daily-time-logs/' + today_csv), sep = ',')

## process data

### creating a separate column with just date created
date_time = df_today['Created At'].str.split(' ', expand = True)
date_time.columns = ['date', 'time']
df_today['date'] = date_time['date']
df_today['time'] = date_time['time']

### converting Elapsed Time column to datetime format
df_today['elapsed_time'] = pd.to_datetime(df_today['Elapsed Time'])
df_today['hours_elapsed'] = (df_today.elapsed_time.dt.hour + df_today.elapsed_time.dt.minute/60 + df_today.elapsed_time.dt.second / 3600)

### grouping data by relevant variables
mat_today = df_today.groupby(['date', 'Text'])['hours_elapsed'].sum().unstack().fillna(0)

## plot data
# pal = sns.color_palette("Set2", as_cmap = False)
pal = sns.color_palette("icefire", mat_today.shape[1])

mat_today.plot(kind = 'bar', stacked = True, color = pal)
# mat_today.plot(kind = 'bar', stacked = True)
plt.legend(loc = 'best', bbox_to_anchor = (1.0, 1.00))
plt.title('Hours spent on different topics')
plt.ylabel('hours spent')
plt.xticks(rotation = 45, ha = 'center')
plt.tight_layout()

## output data to excel or plotting software
plt.savefig('plots/foo.png')
