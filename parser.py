import os
import re
import csv

os.listdir('data-engineer-test-master')
path = 'data-engineer-test-master/datos_data_engineer.tsv'

txt = open(path, encoding='UTF-16LE').read()
preparse = re.findall('(([^\t]*\t[^\t]*){4}(\n|\Z))', txt)
parsed = [t[0].split('\t') for t in preparse]
replaced = [[item.replace('\n',' ').strip() for item in sublist] for sublist in parsed]

file = open('datos_data_engineer.csv.csv', 'w+', newline ='', encoding = 'UTF-8') 
with file:     
    write = csv.writer(file, delimiter='|') 
    write.writerows(replaced)