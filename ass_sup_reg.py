import pandas as pd
import numpy as np

maindf = pd.read_csv('merged_health_reg.csv', index_col = 0)
maindf['Region Name'] = ''
df = pd.read_csv('UNSD-Methodology.csv', index_col = 3)
regions = set(df['Sub-region Name'])
for i,v in enumerate(maindf.index):
    try:
        maindf['Region Name'].iloc[i] = df[df['Sub-region Name'] == maindf['Sub-region Name'].loc[v]]['Region Name'].iloc[0]
    except:
        pass
maindf.to_csv('merged_health_reg.csv')
