from enum import Enum
from abc import abstractproperty, abstractmethod

class BaseClass():
    @abstractmethod
    def display(self):
        pass
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

class TempFormat(Enum):
    C = 1
    F = 2

class DisplayModel:
    def __init__(self, message, speed, font, background):
        # super().__init__()
        self.message = message
        self.speed = speed
        self.font = font
        self.background = background

