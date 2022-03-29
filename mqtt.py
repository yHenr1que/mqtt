import requests
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("topico_mqtt")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    requests.post('http://127.0.0.1:5000/inserir', data=(json.dumps({"message": msg.payload.decode()})))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883)

client.loop_forever()
