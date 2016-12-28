#! python3
# quick-weather.py
# Prints the weather for a location from the command line.

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: quick-weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

w = weather_data['list']
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
