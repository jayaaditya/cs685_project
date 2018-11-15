import pandas as pd
com = {}
df1 = pd.read_csv('health_Normalization.csv', index_col = 0)
df = pd.read_csv('merge.csv', index_col = 0)
df2 = pd.read_csv('Final_Education_Normalization.csv', index_col = 0)
cols1 = set(df1)
cols2 = set(df2)
df.corr().to_csv('corr_mat.csv')
#print df.shape
corrdf = df.corr()
for x in list(corrdf):
    cm = corrdf[x].apply(lambda i: abs(i))
    temp = corrdf[cm > 0.80][x]
    for i in temp.index:
        arr = [x,i]
        arr.sort()
        s = ''.join(arr)
        if not com.has_key(s) and i.split('_')[0] != x.split('_')[0] and '19' not in x and '19' not in i:
            print x,',',i,',',temp.loc[i]
            com[s] = 0
