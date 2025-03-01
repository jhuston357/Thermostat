from threading import Thread
from thermostat import thermostat
from mqttclient import MQTTClient
import time

host = "test.mosquitto.org"
subname = "JerimiahsTherm/setting"
pubname = "JerimiahsTherm/thermostat"

def select_item(dict):
    ts.setsetting( dict["setting"])

def CLI():
    while True:
        print("\n" + subname + " temp is "+ str(ts.gettemp()) + ".\n")
        text = input("Options \n1.Set Temp \n2.Check Temp \n3.Set Night Temp \n4.ShutDown \nEnter 1,2 or 3: ")

        if text == "1":
            print("Current Setting: " + str(ts.getsetting()) + "\n" )
            text = input("New Setting: ")
            ts.setsetting(int(text))

        elif text == "2":
            #DO Nothing
            print("\n\n")

        elif text == "3":
            print("Current Night Setting: " + str(ts.getnightSetting()) + "\n" )
            text = input("New Night Setting: ")
            ts.setnightSetting(int(text))

        elif text == "4":
            exit()

        else:
            print("Incorrect input please enter 1,2 or 3! \n\n")



ts = thermostat(72,70,11,pubname,host)
try:
    mqtt_client = MQTTClient(host)
mqtt_client.connect()
mqtt_client.subscribe(subname)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    ts.setsetting(data["setting"])

mqtt_client.on_message = on_message
except:
    print ("failed mqtt")
Thread(target=ts.start).start()
time.sleep(5)
CLI()
