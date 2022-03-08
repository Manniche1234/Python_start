import json
import requests


url = "http://api.openweathermap.org/data/2.5/weather"
query = {'q': 'Aarhus,dk', 
         'mode': 'json',                       
         'units': 'metric',
         'appid': 'd3d981b59af341a9ebaad1dd48bc2f87'}
r = requests.get(url, params=query)

print(r.json())