from sense_hat import SenseHat
from time import sleep
import datetime
import time
import subprocess
from dotenv import load_dotenv

# Load necessary modules on run
sense = SenseHat()
load_dotenv()

def getTemp():
    return sense.get_temperature()

def getCPUTemp():
    return subprocess.check_output("vcgencmd measure_temp", shell=True)

def adjustTempForCpuTemp(temp_c):
    cpu_temp_c = getCPUTemp()
    temp_calibrated_c = temp_c - ((cpu_temp_c - temp_c)/5.466)
    return temp_calibrated_c

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
    return sense.show_message(message, scroll_speed=scroll_speed, text_colour=text_colour, back_colour=back_colour)

def setLowlight(setting=True):
    sense.low_light=setting
    return


def main():
    showMessage("Starting WeatherPI!")
    while True:
        temp_c = getTemp()
        temp_conv = adjustTempForCpuTemp(temp_c)
        showMessage(temp_conv)

    
if __name__ == "__main__":
    main()