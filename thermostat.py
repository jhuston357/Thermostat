#thermostat controller
from w1thermsensor import W1ThermSensor
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time
import json


class thermostat:
    def __init__(self,temp,setting,switchPin,pubName,host):

        self.temp = temp #current temperature of the room
        self.setting = setting #temperature the user set
        self.switchPin = switchPin #relay data line gpio
        self.switchPos = 0 #relay data lin position on or off
        self.pubName = pubName #location to publish thermostat status
        self.host =  host #local hosts ip to use for publishing

    def settemp(self,temp):
        self.temp = temp

    def setsetting(self,setting):
        #prevent extreme setting for a home enviroment # todo change these to class variables
        if setting>=40 and setting<=90:
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
        #json encodes class member data for publishing
        return json.dumps(self.__dict__)

    def switch(self):
        #Compare temp and setting and set relay to on or off
        if self.temp >= self.setting + 1:
            GPIO.output(self.switchPin,0)
            self.switchPos = 0
        elif self.temp <= self.setting -1:
            GPIO.output(self.switchPin,1)
            self.switchPos = 1

    def start(self):
        #initialize gpio and temp sensor
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.switchPin, GPIO.OUT)
        GPIO.output(self.switchPin,0)
        sensor = W1ThermSensor()
        #Main loop - set current temp from sensor, run switch check, publish new data
        while(True):
            self.temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
            self.switch()
            publish.single(self.pubName, self.json_encoding(), hostname=self.host)
            time.sleep(10)
