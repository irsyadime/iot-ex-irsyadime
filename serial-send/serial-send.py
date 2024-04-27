import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

broker_address = "broker.hivemq.com"
broker_port = 1883
mqtt_topic = "irsyad/led-control"

client = mqtt.Client("Python-Transmitter")
client.connect(broker_address,broker_port)

while True:
    # client.publish("irsyad/led-control","1")
    publish.single(mqtt_topic,"1",hostname=broker_address)
    time.sleep(5)