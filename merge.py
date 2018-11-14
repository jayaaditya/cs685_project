import os
import pandas as pd

folder = 'newdata/health3/'
files = os.listdir(folder)
maindf = pd.read_csv('countries.csv', index_col = 0)
index = set()
for f in files:
    df = pd.read_csv(folder+f, index_col = 0)
    maindf = maindf.merge(df, right_index = True ,left_index = True, how = 'left')
maindf.dropna(how = 'all', axis = 1, inplace = True)
maindf.to_csv('merged_health.csv')
