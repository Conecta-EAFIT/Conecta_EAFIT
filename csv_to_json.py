import pandas as pd
import json


df = pd.read_csv('profesor_database.csv')

df.to_json('profesores.json', orient='records')

with open('profesor/management/commands/profesores.json', 'r') as file:
    profesores = json.load(file)

for i in range(10):
    profesor = profesores[i]
    print(profesor)
    break