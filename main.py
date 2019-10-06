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

# Load necessary modules on run
OPEN_WEATHER_APIKEY=""
MISSOULA_GPS=""
GUATEMALA_GPS=""
CANCELLATION_TOKEN=True
sense = SenseHat()
load_dotenv()


def runWeather():
    print("First Thread")
    try:
        while CANCELLATION_TOKEN:
            temp_c = getTemp()
            background_color = tempSetBackground(temp_c)
            print(background_color)
            #temp_conv = adjustTempForCpuTemp(temp_c, .05)
            showMessage(str(round(temp_c, 1)) + " C", .05, [255,255,255], background_color)
            temp_f = convertToF(temp_c)
            showMessage(str(round(temp_f, 1)) + " F", .05, [255,255,255], background_color)
    except:
        print("An exception occured")

def printCancellationToken():
    print("Second Thread")
    # input("Press Enter to quit...")
    # CANCELLATION_TOKEN = False
    #pending = asyncio.Task.all_tasks()
    #for task in pending:
        #task.cancel()
        # Now we should await task to execute it's cancellation.
        # Cancelled task raises asyncio.CancelledError that we can suppress:
        #with suppress(asyncio.CancelledError):
            #loop.run_until_complete(task)

def testPrint(name):
    i = 0
    while i < 5:     
        print(name + " " +str(i))
        i = i+1

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

   # Working
    t1 = threading.Thread(target=runWeather)
    t2 = threading.Thread(target=printCancellationToken)

    t1.start()
    t2.start()

    t1.join()
    
if __name__ == "__main__":
    main()
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop = asyncio.get_event_loop()    
    #loop.run_until_complete(main(loop))
