from MQTTClient import MQTTClient
from typing import override
import time

class FollowerClient(MQTTClient):
    @override
    def handle_message(self, client, topic, msg):
        print(f'{self.id} received: {topic} - {msg}')
        self.publish_to_robot('leader', msg)

FollowerClient('follower', "10.183.37.83").start()

while True:
    time.sleep(2)