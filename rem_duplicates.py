import pandas as pd

df = pd.read_csv('merged_health.csv')
df = df.groupby(['Country']).sum()
df.to_csv('merged_health.csv')
