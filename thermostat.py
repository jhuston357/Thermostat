#thermostat controller
from w1thermsensor import W1ThermSensor
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time
import json


class thermostat:
    def __init__(self,temp,setting,switchPin,pubName,host):

        self.temp = temp
        self.setting = setting
        self.switchPin = switchPin
        self.switchPos = 0
        self.pubName = pubName
        self.host =  host

    def settemp(self,temp):
        self.temp = temp

    def setsetting(self,setting):
        if setting>40 and setting<90:
            self.setting = setting

    def setswitchPin(self,switchPin):
        self.switchPin = switchPin

    def gettemp(self):
        return self.temp

    def getsetting(self):
        return self.setting

    def getswitchPos(self):
        return self.switchPos

    def json_encoding(self):
        return json.dumps(self.__dict__)

    def switch(self):
        if self.temp >= self.setting:
            GPIO.output(self.switchPin,0)
            self.switchPos = 0
        else:
            GPIO.output(self.switchPin,1)
            self.switchPos = 1

    def start(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.switchPin, GPIO.OUT)
        GPIO.output(self.switchPin,0)
        sensor = W1ThermSensor()
        while(True):
            self.temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
            self.switch()
            publish.single(self.pubName, self.json_encoding(), hostname=self.host)
            time.sleep(5)
