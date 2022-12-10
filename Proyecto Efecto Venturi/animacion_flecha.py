
import sys
import parametros as p
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtCore import pyqtSignal,QTimer, QObject, QThread, QRect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound
from PyQt5 import uic
from os import path
from time import sleep, time

class CrearFlechas(QThread):

    actualizar_pos = pyqtSignal(QLabel, int, int)

    def __init__(self, mama, velocidad):
        super().__init__(mama)
        self.velocidad_seccion = velocidad
        self.flecha_creada = QLabel(mama)
        self.ancho = p.ancho
        self.alto = p.altura
        self.path = p.path_flecha
        self.__posicion = (0, 0)
        self.posicion = (p.pos_inicio_x, p.pos_inicio_y)
        self.init_gui()
        
        
    def init_gui(self):
        self.flecha_creada.setGeometry(self.posicion[0], self.posicion[1],
            self.alto, self.ancho)
        self.flecha_creada.setPixmap(QPixmap(self.path))
        self.flecha_creada.setScaledContents(True)
        self.flecha_creada.setVisible(True)
        self.flecha_creada.show()
        self.start()


    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, movimiento):
        self.__posicion = movimiento
        self.actualizar_pos.emit(self.flecha_creada, self.posicion[0], self.posicion[1])

        


    def run(self):

        while p.FLECHAS_LIMITE >= self.posicion[0]:           
                sleep(0.01)
                if self.velocidad_seccion[0] == self.velocidad_seccion[1]:
                    avance = (p.VELOCIDAD_FLECHA / 10)  + self.posicion[0]
                elif self.posicion[0] <= p.SECCIONES and self.velocidad_seccion[0] < self.velocidad_seccion[1]: #tubo 1
                    avance = (p.VELOCIDAD_FLECHA / 15)  + self.posicion[0]
                elif self.posicion[0] > (p.SECCIONES + 90) and self.velocidad_seccion[0] < self.velocidad_seccion[1]: #tubo 1
                    avance = (p.VELOCIDAD_FLECHA / 15)  + self.posicion[0]
                elif self.posicion[0] <= p.SECCIONES and self.velocidad_seccion[0] > self.velocidad_seccion[1]:  
                    avance = (p.VELOCIDAD_FLECHA / 4)  + self.posicion[0]
                elif self.posicion[0] > p.SECCIONES and self.velocidad_seccion[0] < self.velocidad_seccion[1]: #tubo 2
                    avance = (p.VELOCIDAD_FLECHA / 4)  + self.posicion[0]
                elif self.posicion[0] > p.SECCIONES and self.velocidad_seccion[0] > self.velocidad_seccion[1]:   
                    avance = (p.VELOCIDAD_FLECHA / 15)  + self.posicion[0]
                self.posicion = (avance, self.posicion[1])



        self.flecha_creada.hide()
