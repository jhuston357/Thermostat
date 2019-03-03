from threading import Thread
from .thermostat import thermostat
from .jsonmqttclient import jsonmqttclient

server = "test.mosquitto.org"
subname = "JerimiahsTherm"

ts = thermostat(72,72,11)
client = jsonmqttclient(server,subname,ts.setsetting(),ts)
t1 = Thread(target=ts.start()).start()
t2 = Thread(target=client.start()).start()
