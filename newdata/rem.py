import os

files = os.listdir('Health/')
for f in files:
    os.system('rm '+"\'"+f+"\'")
