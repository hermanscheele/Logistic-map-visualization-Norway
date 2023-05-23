import json
import pandas as pd


file = pd.read_excel('kommune_ordre.xlsx')

d = {}

for index, row in file.iterrows():
    navn = row['navn']
    ordre = row['ordre']
    
    d[navn] = ordre




# Specify the path to the JSON file
file_path = 'data.json'

# Write the dictionary to the JSON file
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(d, json_file, ensure_ascii=False)

print('Dictionary converted to JSON file successfully.')