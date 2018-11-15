import matplotlib.pyplot as plt
import pandas as pd

f = open('infeatures','r')
mdf = pd.read_csv('merge_wn_missing.csv',index_col = 0)
ndf = pd.read_csv('mean_health.csv', index_col = 0)
mdf = mdf.merge(ndf[['Region Name']], how = 'inner', left_index  = True, right_index = True)
df = mdf
rset = set(mdf['Region Name'])
colors = ['b', 'c', 'y', 'm', 'r']
rmap = {}
print len(rset)
for i,v in enumerate(rset):
    rmap[v] = i
for line in f.readlines():
    x,y,labelx,labely = line.split(',')
    a = []
    for r in rset:
        df = mdf[mdf['Region Name'] == r].copy()
        a.append(plt.scatter(df[x].values,
        df[y].values, 
        c = df['Region Name'].apply(lambda x: colors[rmap[x]]),
        label = r))
    plt.legend(a,rmap.keys())
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.savefig(x+'vs'+y+'.png')
