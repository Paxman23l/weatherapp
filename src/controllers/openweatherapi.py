import requests
import os
import json

def formatResponse(data):
    print(data)
    return "Hi from openweatherapi"

def openWeatherApiCall():
    url = os.environ.get("OPEN_WEATHER_URL")
    
    url = addParameters(url)
    result = requests.get(url)
    return formatResponse(result)

def addParameters(url):
    cityCodes = []
    with open("/src/cities.json", 'r') as f:
        cityCodes = json.load(f)["cities"]
        f.close()
    # cityCodes = os.environ.get("CITIES")
    apiKey = os.environ.get("OPEN_WEATHER_APIKEY")
    i = 0
    for item in cityCodes:
        if i == len(cityCodes):
            url = url + item
        elif len(cityCodes) == 1:
            url = url + item
        else:
            url = url + item + ","
            
    if len(cityCodes) > 0:
        url + "&APPID=" + apiKey
    else:
        url + "APPID=" + apiKey
    return url