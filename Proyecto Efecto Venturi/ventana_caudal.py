import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtCore import pyqtSignal,QTimer, QObject, QThread, QRect
from animacion_flecha import CrearFlechas
import parametros as p
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound
from PyQt5 import uic
from os import path



window_caudal, base_class = uic.loadUiType("FONDOS/Caudal.ui")

class VentanaCaudal(window_caudal, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mostrar(self):
        self.show()

    def esconder(self):
        self.hide()