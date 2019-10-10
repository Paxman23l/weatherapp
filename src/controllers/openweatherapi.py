import requests
import os
import json

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
    
        print(json.loads(result))
        return formatResponse(result)
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