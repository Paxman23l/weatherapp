from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
while True:
     t = sense.get_temperature()*1.8+32
     p = sense.get_pressure()
     h = sense.get_humidity()

     t = round(t,1)
     p = round(p,1)
     h = round(h,1)

     if t > 85 and t <200:
          bg = [100,0,0] #red
     if t >40 and t <85:
          bg = [0,100,0] #Green
     if t <40:
          bg =[0,0,100] #blue

     #msg = "Temp: {0} F Pres.: {1} in Humid.: {2}%".format(t,p,h)
     temp = "T: {0}F".format(t)
     pres = "P: {0}in".format(p)
     hum = "H: {0}%".format(h)
     #sense.show_message(msg, scroll_speed=.065, back_colour=bg)
     sense.show_message(temp, scroll_speed=.07, back_colour=bg)
     sleep(.01)
     sense.show_message(pres, scroll_speed=.07, back_colour=bg)
     sleep(.01)
     sense.show_message(hum, scroll_speed=.07, back_colour=bg)

