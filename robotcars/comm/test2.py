import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    print("Follower connected")
    client.subscribe("control_command")

def on_message(client, userdata, msg):
    loaded_msg = json.loads(msg.payload.decode())
    print("Follower received:", msg.topic, loaded_msg)
    client.publish('follower_update', json.dumps(loaded_msg))

client = mqtt.Client(client_id="robotB")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_start()

while True:
    time.sleep(2)
