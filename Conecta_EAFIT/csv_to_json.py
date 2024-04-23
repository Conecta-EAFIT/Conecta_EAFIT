import pandas as pd
import json

df = pd.read_csv('profesores_initial.csv')

df.to_json('profesores.json', orient='records')

with open('profesores.json', 'r') as file:
    profesores = json.load(file)

for i in range(100):
    profesor = profesores[i]
    print(profesor)
    break

