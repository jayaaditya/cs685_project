from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.read_csv('mean_health.csv', index_col = 0)
scaler = MinMaxScaler(copy = False)
vals = scaler.fit_transform(df[list(df)[:-2]].values)
ndf = pd.DataFrame(vals, index = df.index, columns = list(df)[:-2])
ndf.to_csv('norm_health.csv')
