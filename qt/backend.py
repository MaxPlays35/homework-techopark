from asyncore import loop
import random
import time
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


mqttc = mqtt.Client(clean_session=True)

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.username_pw_set("bbgxyaua", "eto1pqwFu9F2")
mqttc.connect("hairdresser.cloudmqtt.com", 15501)
mqttc.subscribe("temp", 0)
mqttc.subscribe("hum", 0)

while True:
    time.sleep(3)
    mqttc.publish("temp", str(random.randint(0, 100)), 0)
    mqttc.loop()
    time.sleep(3)
    mqttc.publish("hum", str(random.randint(50, 100)), 0)
    mqttc.loop()
