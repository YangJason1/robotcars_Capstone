from MQTTClient import MQTTClient
from typing import override

class LeaderClient(MQTTClient):
    @override
    def handle_message(self, client, topic, msg):
        print(f'{self.id} received: {topic} - {msg}')

lc = LeaderClient('leader', "localhost")
lc.start()
lc.publish_to_robot('follower', {'message':'hello world'})

while True:
    inp = input('Enter a message to send\n')
    lc.publish_to_robot('follower', {'message':inp})
