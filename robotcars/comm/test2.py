import paho.mqtt.client as mqtt
import time

BROKER = "10.183.37.93"
TOPIC = "stress/test"

bytes_received = 0
start_time = None

def on_message(client, userdata, msg):
    global bytes_received, start_time
    if start_time is None:
        start_time = time.time()
    bytes_received += len(msg.payload)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883)
client.subscribe(TOPIC, qos=0)

client.loop_start()

time.sleep(10)

duration = time.time() - start_time
print(f"Received {(bytes_received / duration) / 1e6:.2f} MB/s")
