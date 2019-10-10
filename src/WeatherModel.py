from abc import abstractproperty, abstractmethod
from BaseClass import BaseClass

class WeatherModel(BaseClass):
    def __init__(self, temperature, tempFormat):
        super().__init__(self)
        self.temperature = temperature
        self.tempFormat = tempFormat
    
    def display(self):
        return "Temperature is " + self.temperature + " " + self.tempFormat

class WeatherModelDisplay(WeatherModel):
    def __init__(self, temperature, tempFormat, displaySpeed, fontColor, backgroundColor, message):
        super().__init__(temperature, tempFormat)
        self.displaySpeed = displaySpeed
        self.fontColor = fontColor
        self.backgroundColor = backgroundColor
        self.message = message
    def display(self):
        return




