import io
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

import time

s = """
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny"""


# print(s)

# ----------------------------------------------------


df = pd.read_csv(io.StringIO(s))

print(df)

print('-------------------------------------')

# ----------------------------------------------------
url = "https://github.com/khala1391/U_PY_100DayOfCode/raw/refs/heads/main/day25/new_data.csv"
df = pd.read_csv(url)
print(df)

print('-------------------------------------')
# ----------------------------------------------------

url = "https://github.com/khala1391/U_PY_100DayOfCode/raw/refs/heads/main/day25/new_data.csv"
# url ='https://github.com/khala1391/U_PY_100DayOfCode/raw/refs/heads/main/day25/weather_data.csv'
r = requests.get(url)

print("by request.get(url), then print(r.text)")
print(r.text)

print("by request.get(url), then print(r.text)[:1] ==> slicing string")
print(r.text[:30])

print('-------------------------------------')

df = pd.read_csv(io.StringIO(r.text))
print("by read_csv(io.StringIO(r.text))")
print(df)

print("by df[:1] ==> slicing df")
print(df[:1])

print('-------------------------------------')



response = requests.get('https://charts-spotify-com-service.spotify.com/public/v0/charts')
print(response.status_code)
data =response.json()
# print(data)   # some case, unable to read ==>  write dict to json string by json.dump
data_dict= json.dumps(data, indent=4)
# print(data_dict)

with open('day31/spotify_charts.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# ----------------------------------------------------

