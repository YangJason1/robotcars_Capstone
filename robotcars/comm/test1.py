import paho.mqtt.client as mqtt
import time
import os

BROKER = "localhost"
TOPIC = "stress/test"

payload_size = 100_000  # 100 KB
payload = os.urandom(payload_size)

client = mqtt.Client()
client.connect(BROKER, 1883)
client.loop_start()

count = 0
start = time.time()

while time.time() - start < 10:  # run for 10 seconds
    client.publish(TOPIC, payload, qos=0)
    count += 1

duration = time.time() - start
print(f"Sent {count} messages")
print(f"Throughput ≈ {(count * payload_size) / duration / 1e6:.2f} MB/s")