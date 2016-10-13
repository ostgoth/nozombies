import requests
#import json
#from datetime import time
import datetime


def get_forecast(name):
    max_temp = -273
    min_temp = 100500
    #clear_days = []
    #rainy_days = []
    weather = dict
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + name + '&units=metric&cnt=14&appid=d5e66d1cb8eb964911baf723359c3f8d')
    for item in r.json()['list']:
        #print item['temp']['max']
        if item['temp']['max'] > max_temp:
            max_temp = item['temp']['max']
        if item['temp']['min'] < min_temp:
            min_temp = item['temp']['min']
        """
        #curr_date = time.strftime('%Y-%m-%d', time.localtime(item['dt']))
        curr_date = datetime.datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        if item['weather']['main'] in weather.keys():
            weather[item['weather']['main']].append(curr_date)
        else:
            weather[item['weather']['main']] = [curr_date]

        if item['weather']['main'] == 'Clear':
            clear_days.append(time.strftime('%Y-%m-%d', time.localtime(item['dt'])))
        if item['weather']['main'] == 'Rain':
            rainy_days.append(time.strftime('%Y-%m-%d', time.localtime(item['dt'])))
        """
    print 'max temp=', max_temp
    print 'min temp=', min_temp
    #print 'weather=', weather
    #print 'clear days are:', clear_days
    #print 'clear days are:', rainy_days

    #print (r.json())


get_forecast('London')