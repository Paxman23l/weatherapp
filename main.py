from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
from dotenv import load_dotenv
import os
import asyncio
from weather import getTemp, showLetter, showMessage, convertToF, setLowLight

# Load necessary modules on run
OPEN_WEATHER_APIKEY=""
MISSOULA_GPS=""
GUATEMALA_GPS=""
sense = SenseHat()
load_dotenv()

async def runWeather():
    while True:
        temp_c = getTemp()
        #temp_conv = adjustTempForCpuTemp(temp_c, .05)
        showMessage(round(temp_c, 1), .05)
        temp_f = convertToF(temp_c)
        showMessage(round(temp_f, 1), .05)

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
    #showMessage("Starting WeatherPI!", .02)

    #LOAD ENV VARIABLES
    OPEN_WEATHER_APIKEY= os.environ.get("OPEN_WEATHER_APIKEY")
    MISSOULA_GPS=os.environ.get("MISSOULA_GPS")
    GUATEMALA_GPS=os.environ.get("GUATEMALA_GPS")
    #showMessage(OPEN_WEATHER_APIKEY)
    #showMessage(MISSOULA_GPS)
    #showMessage(GUATEMALA_GPS)
    
    #Run weather
    # while True:
    #     temp_c = getTemp()
    #     #temp_conv = adjustTempForCpuTemp(temp_c, .05)
    #     showMessage(round(temp_c, 1), .05)
    #     temp_f = convertToF(temp_c)
    #     showMessage(round(temp_f, 1), .05)
    loop = asyncio.get_event_loop()
    runWeatherTask = loop.run_in_executor(None, runWeather())
    #input("Press Enter to continue...")
    #asyncio.run(runWeatherTask)
    input("Press Enter to quit...")
    runWeatherTask.close()

    
if __name__ == "__main__":
    main()
