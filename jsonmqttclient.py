import json
import paho.mqtt.client as mqtt

def jsonmqttclient(server,subname,function,object):

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(subname)

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        function(json.loads(msg.payload))

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(server, 1883, 60)
    client.loop_start()
