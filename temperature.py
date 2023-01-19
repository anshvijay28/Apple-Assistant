import requests
import json
import math
import datetime 
from datetime import date
import os 

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.environ['openweathermapApiKey']
CITY = "Atlanta"

URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(URL)

def fahrenheit(kelvin):
	f = 1.8 * (kelvin - 273) + 32
	return math.ceil(f * 100) / 100

def sunset(time):
	time = str(time).split(" ")[1]
	hours = time.split(":")[0]
	minutes = time.split(":")[1]
	hours = str(int(hours) - 12)
	return hours + ':' + minutes + 'PM'

data = response.json()

current_date = date.today()
# feels_like = fahrenheit(data['main']['feels_like'])
# actual = fahrenheit(data['main']['temp'])
# low = fahrenheit(data['main']['temp_min'])
# high = fahrenheit(data['main']['temp_max'])

sunset_unix = data['sys']['sunset']
sunset_datetime = datetime.datetime.fromtimestamp(sunset_unix)
time_of_sunset = sunset(sunset_datetime)








