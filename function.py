import requests
import json
import datetime


def summarise_forecast(city):
    max = -273
    min = 100500
    forecasts = {}
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city +
                     '&units=metric&cnt=14&appid=d5e66d1cb8eb964911baf723359c3f8d')
    for item in r.json()['list']:
        if item['temp']['max'] > max:
            max = item['temp']['max']
        if item['temp']['min'] < min:
            min = item['temp']['min']
        curr_date = datetime.datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        if item['weather'][0]['main'] in forecasts.keys():
            forecasts[item['weather'][0]['main']].append(curr_date)
        else:
            forecasts[item['weather'][0]['main']] = [curr_date]
    return json.dumps({'city': city, 'max': max, 'min': min, 'forecasts': forecasts},
                      sort_keys=True, indent = 2, separators=(',', ':'))

print(summarise_forecast('Barcelona'))
