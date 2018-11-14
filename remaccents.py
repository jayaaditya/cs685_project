import os
import pandas as pd

folder = 'newdata/Health/'
files = os.listdir(folder)
for f in files:
    df = pd.read_csv(folder+f)
    cols = list(df)
    df.drop(columns = [cols[-1]], axis = 1, inplace = True)
    cols = list(df)
    nunique = df.apply(pd.Series.nunique)
    cols_to_drop = nunique[nunique == 1].index
    df.drop(cols_to_drop, axis=1,inplace = True)
    df.to_csv('newdata/health2/'+f,index = False)
