import requests
import json
from datetime import time

def get_forecast(name):
    max_temp = -273
    min_temp = 100500
    clear_days = []
    rainy_days = []
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + name + '&units=metric&cnt=14&appid=d5e66d1cb8eb964911baf723359c3f8d')
    for item in r.json()['list']:
        #print item['temp']['max']
        if item['temp']['max'] > max_temp:
            max_temp = item['temp']['max']
        if item['temp']['min'] < min_temp:
            min_temp = item['temp']['min']
        if item['weather']['main'] == 'Clear':
            clear_days.append(time.strftime('%Y-%m-%d', time.localtime(item['dt'])))
        if item['weather']['main'] == 'Rain':
            rainy_days.append(time.strftime('%Y-%m-%d', time.localtime(item['dt'])))

    print 'max temp=', max_temp
    print 'min temp=', min_temp
    print 'clear days are:', clear_days
    print 'clear days are:', rainy_days

    #print (r.json())


get_forecast('London')
