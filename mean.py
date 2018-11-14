import pandas as pd
import numpy as np


sr = {}
cr = {}
df = pd.read_csv('merged_health_reg.csv', index_col = 0)
cols = df.columns
regiondf = pd.DataFrame(index = set(df['Region Name']))
for i in df.index:
    sr[df['Sub-region Name'].loc[i]] = df['Region Name'].loc[i]
    cr[i] = df['Sub-region Name'].loc[i]
regiondf = df.groupby('Region Name').mean()
sregiondf = pd.DataFrame(index = set(df['Sub-region Name']))
regiondf.loc['World'] = df[cols[:len(cols)-2]].mean()
regiondf.dropna(how = 'any', axis = 1,inplace = True)
df.drop(columns = list(set(cols[:-2]) - set(regiondf)), inplace = True)
sregiondf = df.groupby('Sub-region Name').mean()
for i in sregiondf.index:
    sregiondf.loc[i].fillna(regiondf.loc[sr[i]], axis = 0, inplace = True)
for i in df.index:
    df.loc[i] = df.loc[i].fillna(sregiondf.loc[cr[i]], axis = 0).copy()
df.to_csv('mean_health.csv')
sregiondf.to_csv('region_health.csv')
