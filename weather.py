from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
from dotenv import load_dotenv
import os

# Load necessary modules on run
OPEN_WEATHER_APIKEY=""
MISSOULA_GPS=""
GUATEMALA_GPS=""
sense = SenseHat()
load_dotenv()

def getTemp():
    return sense.get_temperature()

def getCPUTemp():
    cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    array = cpu_temp.split("=")
    array2 = array[1].split("'")
    return float(array2[0])

def adjustTempForCpuTemp(temp_c):
    cpu_temp_c = getCPUTemp()
    #print(temp_c)
    #print(cpu_temp_c)
    temp_calibrated_c = temp_c - ((cpu_temp_c - temp_c)/5.466)
    return temp_calibrated_c

def convertToF(temp_c):
    return temp_c * 1.8 + 32

def getHumidity():
    return sense.get_humidity()

def getPressure():
    return sense.get_pressure()

def getOrientationDegrees():
    return sense.get_orientation_degrees()

def getOrientation():
    return sense.get_orientation()

def getCompass():
    return sense.get_compass()

def getGyroscope():
    return sense.get_gyroscope()

def getAccelerometer():
    return sense.get_accelerometer()

def showMessage(message, scroll_speed=.06, text_colour=[255, 0, 0], back_colour=[0, 0, 0]):
    message="{0}".format(message)
    return sense.show_message(message, scroll_speed=scroll_speed, text_colour=text_colour, back_colour=back_colour)

def showLetter(letter,text_colour=[255,0,0],back_colour=[0,0,0]):
    sense.show_letter(letter, text_colour=text_colour, back_colour=back_colour)
    return

def setLowLight(setting=True):
    sense.low_light=setting
    return


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
    showMessage("Starting WeatherPI!", .05)

    #LOAD ENV VARIABLES
    OPEN_WEATHER_APIKEY= os.environ.get("OPEN_WEATHER_APIKEY")
    MISSOULA_GPS=os.environ.get("MISSOULA_GPS")
    GUATEMALA_GPS=os.environ.get("GUATEMALA_GPS")
    showMessage(OPEN_WEATHER_APIKEY)
    showMessage(MISSOULA_GPS)
    showMessage(GUATEMALA_GPS)
    #showMessage("Hello Daniela!!!", .05)
    while True:
        temp_c = getTemp()
        #temp_conv = adjustTempForCpuTemp(temp_c, .05)
        showMessage(round(temp_c, 1), .05)
        temp_f = convertToF(temp_c)
        showMessage(round(temp_f, 1), .05)

    
if __name__ == "__main__":
    main()
