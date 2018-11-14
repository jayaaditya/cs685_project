import os
import pandas as pd

folder = 'newdata/health3/'
files = os.listdir(folder)
index = set()
for f in files:
    df = pd.read_csv(folder+f, index_col = 0)
    index = index.union(set(df.index))
index = list(index)
index.sort()
ndf = pd.DataFrame(index = index)
ndf.to_csv('countries.csv')
