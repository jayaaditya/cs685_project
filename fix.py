import pandas as pd
import os

files = os.listdir('./data')
for f in files:
    df = pd.read_csv('data/'+f)
    colname = f.replace('.csv','')
    df[colname] = df['Value'].copy()
    if 'Value Footnotes' in list(df):
        df[colname + ' Footnotes'] = df['Value Footnotes'].copy()
        df.drop(columns = ['Value Footnotes'], inplace = True)
    df.drop(columns = ['Value'], inplace = True)
    df.to_csv('newdata/'+f, index = False)
