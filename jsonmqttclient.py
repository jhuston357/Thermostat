import json
import paho.mqtt.client as mqtt

# functions that manages mqtt client

def jsonmqttclient(server,subname,function,object):

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(subname)

    def on_message(client, userdata, msg):
        #runs the passed fucntion on incoming data
        function(json.loads(msg.payload))

    client = mqtt.Client() # initialize
    client.on_connect = on_connect # attach function
    client.on_message = on_message # attach function
    client.connect(server, 1883, 60) # initialize server info
    client.loop_start() # start client loop
