from threading import Thread
from .thermostat import thermostat
from .jsonmqttclient import jsonmqttclient

server = "test.mosquitto.org"
subname = "JerimiahsTherm"

def select_item(dict):
    ts.setsetting( dict["setting"])

ts = thermostat(72,72,11)
jsonmqttclient(server,subname,select_item,ts)
t1 = Thread(target=ts.start()).start()
