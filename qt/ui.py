import os
import random
import threading

# from PyQt5 import QtWidgets, uic
from PySide6 import QtWidgets, QtUiTools
import paho.mqtt.client as mqtt


def hum(value):
    ui.humidity_value.setText(value)
    #   print("Value", int(value))
    ui.hum_bar.setValue(random.randint(5, 10))


topics = {"temp": lambda temp: ui.temperature_value.setText(temp), "hum": hum}


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_message(client, obj, msg):
    # print(os.getpid())
    print(threading.get_ident())
    print(msg.topic + " " + str(msg.qos) + " " + msg.payload.decode("utf-8"))
    decoded = msg.payload.decode("utf-8")
    if msg.topic == "temp":
        ui.temperature_value.setText(decoded)
    elif msg.topic == "hum":
        ui.humidity_value.setText(decoded)
        ui.hum_bar.setValue(int(decoded))
    # topics[msg.topic](msg.payload.decode("utf-8"))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


app = QtWidgets.QApplication([])
ui = QtUiTools.QUiLoader().load("ui.ui")
mqttc = mqtt.Client(clean_session=True)

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.username_pw_set("bbgxyaua", "eto1pqwFu9F2")
mqttc.connect("hairdresser.cloudmqtt.com", 15501)
mqttc.subscribe("temp", 0)
mqttc.subscribe("hum", 0)
mqttc.loop_start()

ui.show()
app.exec()
