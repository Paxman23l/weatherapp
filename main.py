from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
from dotenv import load_dotenv
import os
import asyncio
from weather import getTemp, showLetter, showMessage, convertToF, setLowLight
import threading

# Load necessary modules on run
OPEN_WEATHER_APIKEY=""
MISSOULA_GPS=""
GUATEMALA_GPS=""
sense = SenseHat()
load_dotenv()

def runWeather():
    while True:
        temp_c = getTemp()
        #temp_conv = adjustTempForCpuTemp(temp_c, .05)
        showMessage(round(temp_c, 1), .05)
        temp_f = convertToF(temp_c)
        showMessage(round(temp_f, 1), .05)

def printCancellationToken():
    input("Press Enter to quit...")
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
   
    #await asyncio.gather(testPrint("test1"), testPrint("test2"), testPrint("test3"))
    #several_futures = asyncio.gather(runWeather(), printCancellationToken())
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(several_futures)
    #loop.close()
    #requests = [asyncio.ensure_future(runWeather()),
    #            asyncio.ensure_future(printCancellationToken())]
    #responses = loop.run_until_complete(asyncio.gather(*requests))
    #asyncio.ensure_future(runWeather())
    #await printCancellationToken(loop)

    #loop = asyncio.get_event_loop()
    #runWeatherTask = asyncio.async(runWeather()) #.run_in_executor
    
    #loop.run_forever()
    #input("Press Enter to quit...")
    #runWeatherTask.close()
    
   # Working
    t1 = threading.Thread(target=runWeather)
    t2 = threading.Thread(target=printCancellationToken)

    t1.start()
    t2.start()

    t1.join()
    #while True:
    #    print("running")
    
if __name__ == "__main__":
    main()
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop = asyncio.get_event_loop()    
    #loop.run_until_complete(main(loop))
