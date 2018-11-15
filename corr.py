import os
import pandas as pd
import csv
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cs

dic = {}


# df=pd.read_csv("Final_Education_Normalization.csv",encoding = 'utf-8')
df1=pd.read_csv("health_Normalization.csv",encoding = 'utf-8')
# cols = df.columns.values
cols1 = df1.columns.values
# features_edu = [i for i in xrange(1,len(cols))]
features_health = [i for i in xrange(1,len(cols1))]



# for i in features_health:
# 	for j in features_edu:
# 		if cols1[i] in cols:
# 			# print cols1[i]
# 			continue
# 		lis1 = np.array([df1[cols1[i]].values])
# 		lis2 = np.array([df[cols[j]].values])
# 		dic[(i,j)]= cs(lis1,lis2)[0][0]
# lis =  sorted(dic.keys(),key=lambda x:dic[x])[::-1]

for i in features_health:
	for j in features_health:
		if i<j:
			lis1 = np.array([df1[cols1[i]].values])
			lis2 = np.array([df1[cols1[j]].values])
			dic[(i,j)]= cs(lis1,lis2)[0][0]
lis =  sorted(dic.keys(),key=lambda x:abs(dic[x]))[::-1]

for i in lis:
	if abs(dic[i])>0.9:
		if cols1[i[0]].split('_')[0] != cols1[i[1]].split('_')[0]:
			print cols1[i[0]],',',cols1[i[1]]
