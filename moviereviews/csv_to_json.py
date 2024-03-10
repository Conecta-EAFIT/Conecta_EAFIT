import pandas as pd
import json

df = pd.read_csv('disney_plus_titles.csv')
df.to_json('disney.json', orient='records')

with open('disney.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break