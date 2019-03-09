from threading import Thread
from thermostat import thermostat
from jsonmqttclient import jsonmqttclient
import time
import socket

def select_item(dict):
    ts.setsetting( dict["setting"])

def CLI():
    while True:
        print("\n" + subname + " temp is "+ str(ts.gettemp()) + ".\n")
        text = input("Options \n1.Set Temp \n2.Check Temp \n3.ShutDown \nEnter 1,2 or 3: ")

        if text == "1":
            print("Current Setting: " + str(ts.getsetting()) + "\n" )
            text = input("New Setting: ")
            ts.setsetting(int(text))

        elif text == "2":
            check = True
            while check:
                #TODO
                break

        elif text == "3":
            exit()

        else:
            print("Incorrect input please enter 1,2 or 3! \n\n")

host = socket.gethostbyname(socket.gethostname())
subname = "JerimiahsTherm/setting"
pubname = "JerimiahsTherm/thermostat"

ts = thermostat(72,72,11,pubname,host)
jsonmqttclient(host,subname,select_item,ts)
Thread(target=ts.start).start()
time.sleep(5)
CLI()
