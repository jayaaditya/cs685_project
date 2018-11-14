import os
import pandas as pd

folder = 'newdata/health3/'
files = os.listdir(folder)
maindf = pd.read_csv('merged_health.csv', index_col = 0)
df = pd.read_csv('UNSD-Methodology.csv', index_col = 3)
regions = set(df['Sub-region Name'])
maindf = maindf.merge(df[['Sub-region Name']], right_index = True ,left_index = True, how = 'left')
for i,v in enumerate(maindf.index):
    if v in regions:
        maindf['Sub-region Name'].iloc[i] = v
maindf.to_csv('merged_health_reg.csv')
