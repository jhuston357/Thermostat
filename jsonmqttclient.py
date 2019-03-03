import json
import paho.mqtt.client

class jsonmqttclient:
    def __init__(self,server,subname,function,object):
        # Create an MQTT client and attach our routines to it.
        self.server = server
        self.function = function()
        self.object = object
        self.subname = subname

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(subname)

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        function(json.loads(msg.payload)["setting"])

    def start():
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(server, 1883, 60)
        client.loop_forever()
