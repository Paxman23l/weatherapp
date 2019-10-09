from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
from dotenv import load_dotenv
import os
import asyncio
from weather import getTemp, showLetter, showMessage, convertToF, setLowLight, tempSetBackground
import threading
from queue import Queue
from classes.WeatherModel import WeatherModelDisplay, TempFormat, DisplayModel
# Load necessary modules on run
OPEN_WEATHER_APIKEY=""
MISSOULA_GPS=""
GUATEMALA_GPS=""
CANCELLATION_TOKEN=True
sense = SenseHat()
load_dotenv()


def runInsideWeather(queue):
    print("Getting weather")
    try:
        while True:
            temp_c = getTemp()
            background_color = tempSetBackground(temp_c)

            if os.environ.get('METRIC_UNITS'):
                #WeatherModelDisplay(temp_c, TempFormat.C, .05, [255,255,255], background_color, "Inside Temp")                
                queue.put(DisplayModel("Inside temp is: " + temp_c + " " + TempFormat.C, .05, [255,255,255], background_color))    

            if os.environ.get('IMPERIAL_UNITS'):
                temp_f = convertToF(temp_c)
                #queue.put(WeatherModelDisplay(temp_f, TempFormat.F, .05, [255,255,255], background_color, "Inside Temp"))
                queue.put(DisplayModel("Inside temp is: " + temp_f + " " + TempFormat.F, .05, [255,255,255], background_color))    

            sleep(5)
    except:
        print("An exception occured")

def runOutsideWeather(queue):
    pass

def printMessages(queue):
    while True:
        i = queue.get()
        
        if i is None:
            print("no messages to display")
        else:
            showMessage(i.message, i.speed, i.font, i.background)

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

    #LOAD ENV VARIABLES
    OPEN_WEATHER_APIKEY= os.environ.get("OPEN_WEATHER_APIKEY")
    MISSOULA_GPS=os.environ.get("MISSOULA_GPS")
    GUATEMALA_GPS=os.environ.get("GUATEMALA_GPS")

    # Set working Object
    weatherData = Queue<DisplayModel>()
   # Working
    t1 = threading.Thread(target=runInsideWeather, args=(weatherData))
    t2 = threading.Thread(target=runOutsideWeather, args=(weatherData))
    t3 = threading.Thread(target=printMessages, args=(weatherData))
    t1.start()
    t2.start()

    t1.join()
    
if __name__ == "__main__":
    main()
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop = asyncio.get_event_loop()    
    #loop.run_until_complete(main(loop))
