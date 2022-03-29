from ast import arg
from random import randint
from threading import Thread
from time import sleep
from PySide6 import QtWidgets, QtUiTools

app = QtWidgets.QApplication([])
ui = QtUiTools.QUiLoader().load("test_bar.ui")


def update(ui2):
    arg = randint(0, 50)
    ui2.hum_bar.setValue(arg)
    # while True:

    #     print(ui2.hum_bar.value())
    #     sleep(1)


def change():
    # for _ in range(1000):
    a = Thread(target=update, args=(ui,))
    a.start()
    # a.join()


ui.start.clicked.connect(change)

ui.show()
app.exec()
