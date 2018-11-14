# -*- coding: utf-8 -*-
import pandas as pd 
import os
import pickle as pkl
import numpy as np
import csv
files = os.listdir("newdata/Health")


countries = []
regions = {}
regions['Pacific'] = []
cunt2region ={}
countries_in_edu = []
for file in files:
	if file == '.DS_Store':
		continue
	df = pd.read_csv("newdata/health2/"+file,encoding = 'utf-8')
	cols = df.columns.values
	rows = list(set(df[cols[0]].values))
	countries_in_edu = countries_in_edu +rows
countries_in_edu = (list(set(countries_in_edu)))
print len(countries_in_edu)

regions['Europe'] = []
df1 =  pd.read_csv("./UNSD-Methodology.csv", encoding = 'utf-8')
cols =  df1.columns.values
for j,i in enumerate(df1[cols[3]].values):
	if i == 'Eswatini':
		i = 'Swaziland'
	if i == 'United States of America':
		i = 'United States'
	if i == 'Cabo Verde':
		i = 'Cape Verde'
	if i == 'Czechia':
		i = 'Czech Republic'
	if i == 'United Kingdom of Great Britain and Northern Ireland':
		i = 'United Kingdom'
	if i == u"Côte d’Ivoire":
		i = "C\xc3\xb4te d'Ivoire".decode('utf-8')
	if i not in countries_in_edu:
		continue
	
	countries.append(i)
	if df1.iloc[j,1] not in regions:
		regions[df1.iloc[j,1]] = [i]
	else:
		regions[df1.iloc[j,1]].append(i)
	if df1.iloc[j,2] == df1.iloc[j,2]:
		if df1.iloc[j,2] not in regions:
			regions[df1.iloc[j,2]] = [i]
		else:
			regions[df1.iloc[j,2]].append(i)
	if df1.iloc[j,0]=='Oceania':
		regions['Pacific'].append(i)
regions ['South Asia'] =regions['Southern Asia']

del regions['Latin America and the Caribbean']
del regions['Southern Asia']
del regions['Melanesia']
del regions['Micronesia']
del regions['Sub-Saharan Africa']
del regions['Polynesia']
del regions['Australia and New Zealand']

for i in regions:
	lis = regions[i]
	for j in lis:
		cunt2region[j]=i
for file in files:
	if file == '.DS_Store':
		continue
	print file
	df = pd.read_csv("newdata/health2/"+file,encoding = 'utf-8')
	cols = df.columns.values
	print len(df[cols[0]].values)
	rows = list(set(df[cols[0]].values))
	row2index = {}
	for i,row in enumerate(rows):
		row2index[row]=i
	miss_cunt = []
	for cunt in countries_in_edu:
		if cunt in rows:
			if df.iloc[row2index[cunt],1]!=df.iloc[row2index[cunt],1] or df.iloc[row2index[cunt],1] == 0:
				miss_cunt.append(cunt)
		else:
			miss_cunt.append(cunt)
	df_new = pd.DataFrame(columns=cols)
	for i,cunt in enumerate(countries_in_edu):
		if cunt not in miss_cunt:
			df_new.loc[i] = df.iloc[row2index[cunt]].values
		else:
			vec = np.zeros(len(df.iloc[0].values[1:]))
			count = 0
			for jj in regions[cunt2region[cunt]]:
				if jj not in miss_cunt:
					vec +=[ float(k) for k in df.iloc[row2index[jj]].values[1:]]
					count +=1
			if count!=0:
				vec=vec/count
			vec = [cunt] + [str(gg) for gg in vec]
			df_new.loc[i] = vec
	print len(df_new[cols[0]].values)
	df_new = df_new.sort_values(by=cols[0])
	df_new = df_new.reset_index(drop=True)
	df_new.to_csv("newdata/health3/"+file,encoding = 'utf-8',index=False)


