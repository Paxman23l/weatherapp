import requests
import os
import json
from weather import tempSetBackground
from DisplayModel import DisplayModel

def formatResponse(data):
    print(data)
    return "Hi from openweatherapi"

def openWeatherApiCall():
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
                model = DisplayModel(item['name'] + ": " + str(item['main']['temp']) + "C", .05, [255,255,255],background)
                # msg.append(item['name'] + ": " + str(item['main']['temp']) + "C")
                msg.append(model)
            return msg
        else:
            return []
    except Exception as e:
        print(e)

# def addParameters(url):
#     # cityCodes = []
#     # with open("/src/cities.json", 'r') as f:
#     #     cityCodes = json.load(f)["cities"]
#     #     f.close()
#     # cityCodes = os.environ.get("CITIES")
#     # apiKey = os.environ.get("OPEN_WEATHER_APIKEY")
#     i = 0
#     # for item in cityCodes:
#     #     item = 'item'
#     #     if i == (len(cityCodes) - 1):
#     #         url = url + item
#     #     elif len(cityCodes) == 1:
#     #         url = url + item
#     #     else:
#     #         url = url + item + ','
#     #     i = i + 1
            
#     if len(cityCodes) > 0:
#         url + "&APPID=" + apiKey
#     else:
#         url + "APPID=" + apiKey
#     print(url)
#     return url
