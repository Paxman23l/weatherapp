from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
import cloudant
from dotenv import load_dotenv
import os
from controllers.weather import getTemp, showLetter, showMessage, convertToF
from controllers.weather import setLowLight, tempSetBackground
import threading
from queue import Queue
from models.WeatherModel import WeatherModel, WeatherModelDisplay
from models.DisplayModel import DisplayModel
from controllers.openweatherapi import openWeatherApiCall
from models.Enums import TempFormat
import sys
from services.couchdb import addInternalWeather,addExternalWeather

# Load necessary modules on run
sys.path.insert(1, '.')
OPEN_WEATHER_APIKEY = ""
MISSOULA_GPS = ""
GUATEMALA_GPS = ""
CANCELLATION_TOKEN = True
TIME_OUT = 15
ENABLE_STORAGE = False
sense = SenseHat()
load_dotenv()

def runInsideWeather(q):
    print("Getting weather")
    
    while True:
        if q.full() != True:
            try:
                temp_c = getTemp()
                background_color = tempSetBackground(temp_c)
                if os.environ.get('METRIC_UNITS'):
                    # WeatherModelDisplay(temp_c, TempFormat.C, .05, [255,255,255], background_color, "Inside Temp")                
                    q.put(DisplayModel("Inside: " + str(round(temp_c, 1)) + TempFormat.C.name, .05, [255,255,255], background_color))    
                if os.environ.get('IMPERIAL_UNITS'):
                    temp_f = convertToF(temp_c)
                    # queue.put(WeatherModelDisplay(temp_f, TempFormat.F, .05, [255,255,255], background_color, "Inside Temp"))
                    q.put(DisplayModel("Inside: " + str(round(temp_f, 1)) + TempFormat.F.name, .05, [255,255,255], background_color))    
                # add internal weather data to database
                if ENABLE_STORAGE:
                    addInternalWeather(datetime.datetime.now(), temp_c)
            except Exception as e:
                print("An exception occured")
                print(e)
            
        sleep(TIME_OUT)
    

def runOutsideWeather(q):
    while True:
        if q.full() != True:
            try:
                result = openWeatherApiCall(ENABLE_STORAGE)
                for item in result:
                    q.put(item)
            except Exception as e:
                print("An exception occured")
                print(e)
        sleep(TIME_OUT)

def printMessages(queue):
    while True:
        i = queue.get()
        
        if i is None:
            print("no messages to display")
        else:
            showMessage(i.message, i.speed, i.font, i.background)

def _loadSettings():
    # Load timeout
    timeOut = os.environ.get("QUERY_TIMEOUT")
    if timeOut is not None:
        TIME_OUT = timeOut
    enableStorage = os.environ.get("ENABLE_STORAGE")
    if enableStorage is not None:
        ENABLE_STORAGE = enableStorage

def main():
    setLowLight()
    showLetter("<", [0,0,204], [255,255,255]) #blue with white
    sleep(.5)
    showLetter(">", [0,255,0], [160,160,160]) #green with grey
    sleep(.5)
    showLetter("<", [255,255,0], [32,32,32]) #yellow with black
    sleep(.5)
    showLetter(">", [255,128,0], [0,0,51]) #orange with dark blue
    sleep(.5)

    _loadSettings()

    # Set working Object
    weatherData = Queue(10)
    t1 = threading.Thread(target=runInsideWeather, args=(weatherData,))
    t2 = threading.Thread(target=runOutsideWeather, args=(weatherData,))
    t3 = threading.Thread(target=printMessages, args=(weatherData,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()
