# -*- coding: utf-8 -*-
import pandas as pd 
import os
import pickle as pkl
import csv
files = os.listdir("newdata/Health")


countries_in_edu = []
for file in files:
	if file == '.DS_Store':
		continue
	df = pd.read_csv("newdata/Health/"+file,encoding = 'utf-8')
	cols = df.columns.values
	rows = list(set(df[cols[0]].values))
	countries_in_edu = countries_in_edu +rows
countries_in_edu = list(set(countries_in_edu))




countries = []
cunt2id = {}
regions = {}
regions['Least Developed Countries (LDC)'] = []
regions['Pacific'] = []


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
	cunt2id[i]=j
	if df1.iloc[j,1] not in regions:
		regions[df1.iloc[j,1]] = [i]
	else:
		regions[df1.iloc[j,1]].append(i)
	if df1.iloc[j,4] == 'x':
		regions['Least Developed Countries (LDC)'].append(i)
	if df1.iloc[j,0] == 'Europe':
		regions['Europe'].append(i)
	if df1.iloc[j,2] == df1.iloc[j,2]:
		if df1.iloc[j,2] not in regions:
			regions[df1.iloc[j,2]] = [i]
		else:
			regions[df1.iloc[j,2]].append(i)
	if df1.iloc[j,0]=='Oceania':
		regions['Pacific'].append(i)
regions['Eastern and Southern Africa'] = regions ['Eastern Africa'] + regions ['Southern Africa']
regions['Western and Central Africa'] = regions['Western Africa'] + regions['Middle Africa']
regions['Middle East and North Africa'] =  regions['Northern Africa'] + regions['Western Asia']
regions['East Asia and Pacific'] = regions['South-eastern Asia'] + regions['Eastern Asia'] +regions['Pacific']
regions['CEE/CIS'] =regions['Europe'] + regions['Central Asia']
regions ['South Asia'] =regions['Southern Asia']
regions['Least Developed Countries/Territories']=regions['Least Developed Countries (LDC)']
regions['Latin America and Caribbean']=regions['Latin America and the Caribbean']

for file in files:
	if file == '.DS_Store':
		continue
	print file
	df = pd.read_csv("newdata/Health/"+file,encoding = 'utf-8')
	cols = df.columns.values
	rows = list(set(df[cols[0]].values))
	cunt = [i for i in rows if i in countries]
	rgns = [i for i in rows if i in regions.keys()]
	chut = [i for i in rows if i not in rgns and i not in cunt]
	print len(df.index.values)
	for region in rgns:
		region_arr = df.loc[df["Country or Area"]==region].values
		region_arr = region_arr[0][1:]
		for value in regions[region]:
			if value in cunt:
				continue
			cunt.append(value)
			new_Ar = [value]
			for v in region_arr:
				new_Ar.append(v)
			df.loc[len(df.index.values)] = new_Ar
	df = df.sort_values(by=cols[0])
	df = df.reset_index(drop=True)
	rows =df[cols[0]].values
	final = []
	todrop = []
	for j,row in enumerate(rows):
		if row not in countries or row in final:
			todrop.append(j)
		else:
			final.append(row)
	df = df.drop(todrop)
	print len(df.index.values),'done'
	df.to_csv("newdata/health2/"+file,encoding = 'utf-8',index=False)





# countries = sorted(countries,key=str.lower)[9:]
# for i in countries:
# 	print i
