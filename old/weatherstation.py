#!/usr/bin/python

from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
#from datetime import datetime
import datetime
import time
import subprocess
# import MySQLdb
#import threading

#This Connection connects but gives 1044 error
# db = MySQLdb.connect(host="mysql4.gear.host",
#                      user="weatherapp",
#                      passwd="Password1!",
#                      db="weatherapp")




#AWS Server...someday when I'm less poor
#db = MySQLdb.connect(host="weatherapp
#.c2esepqbahmg.us-east-2.rds.amazon.com:3306",
#def currentInfo():
    #ts = time.time()
    #timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    #t = sense.get_temperature() * 1.8 + 32
    #p = sense.get_pressure()
    #h = sense.get_humidity()

    #t = round(t, 1)
    #p = round(p, 1)
    #h = round(h, 1)

    #return t, p, h


def weatherDisplay():
     #currentInfo()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y %H:%M')

    t = sense.get_temperature() * 1.8 + 32
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = tempFix(t)
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    if t > 80 and t < 200:
        #red
        bg = [100, 0, 0]
    if t > 40 and t < 80:
        #Green
        bg = [0, 100, 0]
    if t < 40:
        #Blue
        bg = [0, 0, 100]

    #msg = "Temp: {0} F Pres.: {1} in Humid.: {2}%".format(t,p,h)
    temp = "T: {0}F".format(t)
    pres = "P: {0}in".format(p)
    hum = "H: {0}%".format(h)
    tme = "Time: {0}".format(timestamp)

    #sense.show_message(msg, scroll_speed=.065, back_colour=bg)
    sense.show_message(tme, scroll_speed=.07, back_colour=bg)
    sleep(.01)
    sense.show_message(temp, scroll_speed=.06, back_colour=bg)
    sleep(.01)
    sense.show_message(pres, scroll_speed=.06, back_colour=bg)
    sleep(.01)
    sense.show_message(hum, scroll_speed=.06, back_colour=bg)


def databaseUpdate():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')

    t = sense.get_temperature() * 1.8 + 32
    p = sense.get_pressure()
    h = sense.get_humidity()
    temp = tempFix(t)
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    #Try to update database
    try:
        update_weather = ("INSERT INTO weather "
                          "(temp, pressure, humidity, time)"
                          "VALUES (%s, %s, %s, %s)")

        cursor = db.cursor()
        current_weather = (temp, p, h, timestamp)
        cursor.execute(update_weather, current_weather)
        #emp_no = cursor.lastrowid

        db.commit()
        cursor.close()
        #sleep(600)

    #if update fails, continue on
    except:

        pass

def tempFix(temp):
    cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    array = cpu_temp.split("=")
    array2 = array[1].split("'")

    cpu_tempf = float(array2[0]) * 9.0 / 5.0 + 32.0
    #cpu_tempf = float("{0:.2f}".format(cpu_tempf))
    
    temp_calibrated = temp - ((cpu_tempf - temp)/5.466)
    
    return temp_calibrated


while True:
    databaseUpdate()
    t_end = time.time() + 60 * 1

    while time.time() < t_end:
        weatherDisplay()

#thread1 = weatherDisplay()
#thread2 = databaseUpdate()