import requests


r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=London&units=imperial&cnt=14&appid=d5e66d1cb8eb964911baf723359c3f8d')
r.json
print r