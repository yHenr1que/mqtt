import requests
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("topico_mqtt")

def on_message(client, userdata, msg):
    #envia o post
    print(msg.topic+" "+str(msg.payload))
    requests.post('http://localhost:8000/inserir', data=(json.dumps({ "message":str(msg.payload.decode())})))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
