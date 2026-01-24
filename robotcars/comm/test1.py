import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    print("Leader connected")
    client.subscribe("follower_update")

def on_message(client, userdata, msg):
    print("Leader received:", msg.topic, msg.payload.decode())

client = mqtt.Client(client_id="leader")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_start()

while True:
    msg = input('Enter a message to send\n')
    client.publish("control_command", json.dumps({"message": msg}))
