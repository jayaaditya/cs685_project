import pandas as pd
from sklearn.ensemble import RandomForestRegressor as dt

fdf = pd.read_csv('mean_health.csv')
regions = set(fdf['Region Name'])
for x in regions:
    print x
    lis =  ['Proportion of 1 year-old children immunised against DPT1','Proportion of 1 year-old children immunised against measles','Proportion of 1 year-old children fully immunised against DPT','Proportion of 1 year-old children fully immunised against Haemophilus influenzae type B','Proportion of 1 year-old children immunised against TB (BCG)','Proportion of 1 year-old children fully immunised against Hepatitis B','Proportion of 1 year-old children fully immunised against polio (OPV)']
    df = fdf[fdf['Region Name'] == x]
    Y = df['Under-five mortality rate (U5MR)_Deaths per 1000 live births_2011.0_Total'].values
    X = df[['Proportion of 1 year-old children immunised against DPT1','Proportion of 1 year-old children immunised against measles','Proportion of 1 year-old children fully immunised against DPT','Proportion of 1 year-old children fully immunised against Haemophilus influenzae type B','Proportion of 1 year-old children immunised against TB (BCG)','Proportion of 1 year-old children fully immunised against Hepatitis B','Proportion of 1 year-old children fully immunised against polio (OPV)']].values
    clf = dt(random_state = 0)
    clf.fit(X,Y)
    for i,v in zip(clf.feature_importances_,lis):
        print v,i
lis =  ['Proportion of 1 year-old children immunised against DPT1','Proportion of 1 year-old children immunised against measles','Proportion of 1 year-old children fully immunised against DPT','Proportion of 1 year-old children fully immunised against Haemophilus influenzae type B','Proportion of 1 year-old children immunised against TB (BCG)','Proportion of 1 year-old children fully immunised against Hepatitis B','Proportion of 1 year-old children fully immunised against polio (OPV)']
df = fdf.copy()
Y = df['Under-five mortality rate (U5MR)_Deaths per 1000 live births_2011.0_Total'].values
X = df[['Proportion of 1 year-old children immunised against DPT1','Proportion of 1 year-old children immunised against measles','Proportion of 1 year-old children fully immunised against DPT','Proportion of 1 year-old children fully immunised against Haemophilus influenzae type B','Proportion of 1 year-old children immunised against TB (BCG)','Proportion of 1 year-old children fully immunised against Hepatitis B','Proportion of 1 year-old children fully immunised against polio (OPV)']].values
clf = dt(random_state = 0)
clf.fit(X,Y)
for i,v in zip(clf.feature_importances_,lis):
    print v,i
