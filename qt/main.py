import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app=QtWidgets.QApplication([])
ui = uic.loadUi("gui.ui")
ui.setWindowTitle("ArduinoGUI")

serial = QSerialPort()
serial.setBaudRate(115200)

data = {
  "R": 0,
  "G": 0,
  "B": 0,
}

COMPortList = []
ports=QSerialPortInfo().availablePorts()
for port in ports:
    COMPortList.append(port.portName())
print(COMPortList)
ui.listCOM.addItems(COMPortList)

def openCOM():
    serial.setPortName(ui.listCOM.currentText())
    serial.open(QIODevice.ReadWrite)
    ui.listCOM.setEnabled(False)

def closeCOM():
    serial.close()
    ui.listCOM.setEnabled(True)

ui.openCOM.clicked.connect(openCOM)
ui.closeCOM.clicked.connect(closeCOM)

def readCOM():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    print(rxs)

serial.readyRead.connect(readCOM)

def send_data():
  print(json.dumps(data) + '/')
  return json.dumps(data) + '/'

def slider_r(val):
    global data
    data["R"] = int(val)
    send_data()

def slider_g(val):
    global data
    data["G"] = int(val)
    send_data()

def slider_b(val):
    global data
    data["B"] = int(val)
    send_data()

ui.RSlider.valueChanged.connect(slider_r)
ui.GSlider.valueChanged.connect(slider_g)
ui.BSlider.valueChanged.connect(slider_b)

ui.show()
app.exec()