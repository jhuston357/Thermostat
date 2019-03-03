from threading import Thread
from .thermostat import thermostat
from .jsonmqttclient import jsonmqttclient

server = "test.mosquitto.org"
subname = "JerimiahsTherm"

def select_item(dict):
    ts.setsetting( dict["setting"])

def CLI():
    while True:
        print(subname + " temp is "+ ts.gettemp()+ ".\n\n")
        text = input(" Options \n 1.Set Temp \n 2.Check Temp \n 3.ShutDown \n")

        if text == "1":
            print("Current Setting: " + getsetting() + "\n" )
            text = input("New Setting: ")

        elif text == "2":
            #DO Nothing
            print("\n\n")

        elif text == "3":
            exit()

        else
            print("Incorrect input please enter 1,2 or 3! \n\n")



ts = thermostat(72,72,11)
jsonmqttclient(server,subname,select_item,ts)
t1 = Thread(target=ts.start()).start()
CLI();
