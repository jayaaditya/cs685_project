import os
import pandas as pd

folder = 'newdata/health2/'
files = os.listdir(folder)
for f in files:
    df = pd.read_csv(folder+f)
    cols = list(df)
    if len(cols) == 4:
        df.set_index(cols[:len(cols)-1], inplace = True)
        df = df.unstack(level=-1)
        ncols = ["_".join(map(str,col)).strip() for col in df.columns.values]
        df.columns = ncols
        df.reset_index(inplace = True)
        df.set_index(cols[0:2], inplace = True)
        df = df.unstack(level = -1)
        ncols = ["_".join(map(str,col)).strip() for col in df.columns.values]
        df.columns = ncols
        for x in ncols:
            df[x] = pd.to_numeric(df[x], errors = 'coerce')
        df.dropna(how = 'all', axis = 1, inplace = True)
    elif len(cols) == 3:
        df.set_index(cols[:len(cols)-1], inplace = True)
        df = df.unstack(level=-1)
        cols = ["_".join(map(str,col)).strip() for col in df.columns.values]
        df.columns = cols
        for x in cols:
            df[x] = pd.to_numeric(df[x], errors = 'coerce')
        df.dropna(how = 'all', axis = 1, inplace = True)
    else:
        df.set_index(cols[:1], inplace = True)
    df.to_csv('newdata/health3/'+f)
