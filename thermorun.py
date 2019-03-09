from threading import Thread
from thermostat import thermostat
from jsonmqttclient import jsonmqttclient
import time
import socket

#function for parsing setting info from client message and setting thermostat setting temp
def select_item(dict):
    ts.setsetting( dict["setting"])

# A function that contains the command line interface to interact with therostat
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

# intitializing constant variables

host = socket.gethostbyname(socket.gethostname()) #ip of current device
subname = "JerimiahsTherm/setting" #subscribe location name
pubname = "JerimiahsTherm/thermostat" #publish location name

ts = thermostat(72,72,11,pubname,host) #initializes thermostat
jsonmqttclient(host,subname,select_item,ts) #runs mqtt client
Thread(target=ts.start).start() #starts the thermostat
time.sleep(5) # wait five seconds for thermostat to start
CLI() # run command line loop
