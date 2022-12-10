import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtCore import pyqtSignal,QTimer, QObject, QThread, QRect, QByteArray
from PyQt5.QtGui import QPixmap, QFont, QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5 import uic
from os import path





window_juego, base_class = uic.loadUiType("FONDOS/_ventana_inicio.ui")

class VentanaInicio(window_juego, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mostrar(self):
        self.show()

    def esconder(self):
        self.hide()






if __name__ == '__main__':
    app = QApplication([])
    s = VentanaInicio()
    s.show()
    sys.exit(app.exec_())

