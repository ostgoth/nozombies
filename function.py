import requests
import json
import datetime


def get_forecast(name):
    max_temp = -273
    min_temp = 100500
    forecast = {}
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + name + \
                     '&units=metric&cnt=14&appid=d5e66d1cb8eb964911baf723359c3f8d')
    for item in r.json()['list']:
        if item['temp']['max'] > max_temp:
            max_temp = item['temp']['max']
        if item['temp']['min'] < min_temp:
            min_temp = item['temp']['min']
        curr_date = datetime.datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        if item['weather'][0]['main'] in forecast.keys():
            forecast[item['weather'][0]['main']].append(curr_date)
        else:
            forecast[item['weather'][0]['main']] = [curr_date]
    name = {'name': name}
    max_temp = {'max_temp': max_temp}
    min_temp = {'min_temp': min_temp}
    forecast = {'forecast': forecast}
    print(name)
    print(max_temp)
    print(min_temp)
    print(forecast)

get_forecast('Kyiv')
