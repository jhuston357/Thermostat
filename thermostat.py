#thermostat controller
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time
import socket

class thermostat:
    def __init__(self,temp,setting,switchPin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.temp = temp
        self.setting = setting
        self.switchPin = switchPin
        self.switchPos = 0
        GPIO.output(self.switchPin,0)
        sensor = W1ThermSensor()

    def settemp(temp):
        self.temp = temp

    def setsetting(setting):
        self.setting = setting

    def setswitchPin(switchPin):
        self.switchPin = switchPin

    def gettemp():
        return self.temp

    def getsetting():
        return self.setting

    def getswitchPos():
        return self.switchPos

    def checktemp():
        self.temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
        switch()

    def switch():
        if self.temp >= self.setting:
            GPIO.output(self.switchPin,0)
            self.switchPos = 0
        else:
            GPIO.output(self.switchPin,1)
            self.switchPos = 1
