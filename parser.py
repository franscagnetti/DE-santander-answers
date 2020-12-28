import pandas as pd
import os
import re

os.listdir('data-engineer-test-master')

def parser(path):
    txt = open(path, encoding='UTF-16LE').read()
    preparse = re.findall('(([^\t]*\t[^\t]*){4}(\n|\Z))', txt)
    parsed = [t[0].split('\t') for t in preparse]
    return pd.DataFrame(parsed)


df = parser('data-engineer-test-master/datos_data_engineer.tsv')
df = df.replace('\n',' ', regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df.to_csv('data-engineer-test-master/datos_data_engineer.csv', index = False, encoding = 'UTF-8', sep = '|')