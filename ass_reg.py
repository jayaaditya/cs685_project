import os
import pandas as pd

folder = 'newdata/health3/'
files = os.listdir(folder)
maindf = pd.read_csv('merged_health.csv', index_col = 0)
df = pd.read_csv('UNSD-Methodology.csv', index_col = 3)
maindf = maindf.merge(df[['Region Name']], right_index = True ,left_index = True, how = 'left')
maindf.to_csv('merged_health_reg.csv')
