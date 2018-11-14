import pandas as pd
import os
import difflib

maindf = pd.read_csv('UNSD-Methodology.csv', index_col = 3)
countries = maindf.index
old = set()
new = set()
for files in os.listdir('newdata/Health'):
    print files
    df = pd.read_csv('newdata/Health/'+files, index_col = 0)
    for x in df.index:
        try:
            if x != difflib.get_close_matches(x,countries)[0]:
                new.add(difflib.get_close_matches(x,countries)[0])
                old.add(x)
        except:
            pass
#            print x

for a,b in zip(old,new):
    print a,b
