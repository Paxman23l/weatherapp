import requests
import os
import json
from . weather import tempSetBackground
from models.DisplayModel import DisplayModel
from services.couchdb import addExternalWeather
import datetime

def formatResponse(data):
    print(data)
    return "Hi from openweatherapi"

def openWeatherApiCall(ENABLE_STORAGE):
    try:
        url = os.environ.get("OPEN_WEATHER_URL")
        apiKey = os.environ.get("OPEN_WEATHER_APIKEY")
        cityCodes = []
        with open("/src/cities.json", 'r') as f:
            cityCodes = json.load(f)["cities"]
            f.close()
    
        # url = addParameters(url)
        PARAMS = {'id': cityCodes, 'APPID': apiKey, 'units': 'metric'}
        print(PARAMS)
        result = requests.get(url, params=PARAMS)
    
        if result.status_code == 200:
            msg = []
            jsonResult = json.loads(result.content.decode('utf-8'))
            for item in jsonResult['list']:
                background = tempSetBackground(item['main']['temp'])
                print(item['name'] + ": " + str(round(item['main']['temp'], 1)) + "C")
                model = DisplayModel(item['name'] + ": " + str(round(item['main']['temp'], 1)) + "C", .05, [255,255,255],background)
                msg.append(model)
                print("ENABLE_STORAGE:  " + str(ENABLE_STORAGE))
                if ENABLE_STORAGE:
                        addExternalWeather(datetime.datetime.now(), item['name'], str(round(item['main']['temp'], 1)))
            return msg
        else:
            return []
    except Exception as e:
        print(e)
