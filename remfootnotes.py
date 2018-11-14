import os
import pandas as pd

folder = 'newdata/Health/'
files = os.listdir(folder)
for f in files:
    df = pd.read_csv(folder+f, index_col = 0)
    flag = True
    j = None
    for i,v in enumerate(df.index):
        if v == 'fnSeqID':
            flag = True
            break
    if flag:
        df.drop(df.index[i:],inplace = True)
    df.to_csv(folder+f)

