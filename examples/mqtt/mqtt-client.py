
from simple import MQTTClient

client = MQTTClient('UNIQUEID', '172.20.10.3')
client.connect()

client.publish('temperatur', '42')