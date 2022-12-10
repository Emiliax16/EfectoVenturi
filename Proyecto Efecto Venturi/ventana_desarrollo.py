import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal,QTimer, QObject, QThread, QRect
from animacion_flecha import CrearFlechas
import parametros as p
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound
from PyQt5 import uic
from os import path
from efecto_venturi_ import Venturi


window_desarrollo, base_class = uic.loadUiType("FONDOS/_ventana_programa.ui")

class VentanaDesarrollo(window_desarrollo, base_class):

    signal_info_densidad = pyqtSignal()
    signal_info_area = pyqtSignal()
    signal_info_caudal = pyqtSignal()
    signal_cerrar_todo = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.condicion_d.hide()
        self.condicion_q.hide()
        self.condicion_a1.hide()
        self.condicion_a2.hide()
        self._presion.setEnabled(False)
        self._velocidad.setEnabled(False)
        self._alturas.setEnabled(False)
        self.boton_plot.setEnabled(False)
        self.densidad_escogida = 0
        self.caudal_escogido = 0
        self.iteracion = 0
        self.label = None
        self.valor_presion.hide()
        self.valor_velocidad.hide()
        self.valor_altura.hide()
        self.s1.hide()
        self.s2.hide() 
        #self.punto1_escogido = 0
        #self.punto2_escogido = 0
        self.tuberia_escogida = None
        self.area1_escogida = 1
        self.area2_escogida = 1
        self.presion_escogida = 0.98
        self.calculo_presiones = ' '
        self.calculo_velocidades = ' '
        self.calculo_alturas = ' '
        self.contador = 0
        self.programa = None
        self.rellenar_datos()
        self.tiempo = QTimer(self)

    def mostrar(self):
        self.show()

    def esconder(self):
        self.hide()

    def recibir_parametros(self):
        self.contador = 0
        self.densidad_escogida = self._densidad.currentText()
        if self.densidad_escogida[3] == ' ':
            self.densidad_escogida = self.densidad_escogida[: 3]
        elif self.densidad_escogida == 'Selecciona una densidad':
            pass
        else:
            self.densidad_escogida = self.densidad_escogida[: 4]
        self.verificar_condiciones(self.densidad_escogida, True)
        self.caudal_escogido = self._caudal.text()
        self.verificar_condiciones(self.caudal_escogido, True)
        self.area1_escogida = self._area1.currentText()
        self.verificar_condiciones(self.area1_escogida, True)
        self.area2_escogida = self._area2.currentText()
        self.verificar_condiciones(self.area2_escogida)

        

    def verificar_condiciones(self, parametro, comprobador = False):
        if parametro == self.densidad_escogida and comprobador == True:
            if parametro != 'Selecciona una densidad':
                self.condicion_d.hide()
                self.contador += 1
            else:
                self.condicion_d.show()
        elif parametro == self.caudal_escogido and comprobador == True:
            if parametro.isdigit() == True and int(parametro) not in range(1, 5):
                self.condicion_q.show()
            elif parametro.isdigit() == False:
                self.condicion_q.show()
            else: 
                self.condicion_q.hide()
                self.contador += 1
        elif parametro == self.area1_escogida and comprobador == True:
            if parametro != 'Selecciona un área':
                self.condicion_a1.hide()
                self.contador += 1
            else:
                self.condicion_a1.show()
        elif parametro == self.area2_escogida:
            if parametro != 'Selecciona un área':
                self.condicion_a2.hide()
                self.contador += 1
            else:
                self.condicion_a2.show()

        if self.contador == 4:
            self.poner_imagen(self.area1_escogida, self.area2_escogida)
            self.boton_plot.setEnabled(True)
            self.boton_datos.setEnabled(False)
            self.programa = Venturi(self.densidad_escogida, self.caudal_escogido, self.presion_escogida, 
                self.area1_escogida, self.area2_escogida)
            self.calculo_presiones = self.programa.presiones()
            self.calculo_velocidades = self.programa.velocidades()
            self.calculo_alturas = self.programa.alturas()
    
    def mousePressEvent(self, ev):
        x = ev.x()
        y = ev.y()
        if x in range(30, 46) and y in range(151, 166):
            self.signal_info_densidad.emit()
        elif x in range(30, 46) and y in range(252, 268):
            self.signal_info_caudal.emit()
        elif x in range(30, 46) and y in range(400, 416):
            self.signal_info_area.emit()


    def poner_imagen(self, a1, a2):
        self.label = QLabel(self)
        self.label.setGeometry(450, 160, 430, 200)
        self.iteracion += 1
        if a1 == '3' and a2 == '3':
            ruta_imagen = p.path_tubos['3']
        elif a1 == '5' and a2 == '5':
            ruta_imagen = p.path_tubos['4']
        elif a1 == '3' and a2 == '5':
            ruta_imagen = p.path_tubos['2']
            self.s1.show()
            self.s2.show()
        else:
            ruta_imagen = p.path_tubos['1']
            self.s1.show()
            self.s2.show()
    
        pixeles = QPixmap(ruta_imagen)
        self.label.setPixmap(pixeles)
        self.label.setScaledContents(True)
        self.label.show()

    def mostrar_opciones(self):
        self.valor_presion.setText(f'P1: {self.calculo_presiones[0]} [Pa]\nP2: {self.calculo_presiones[1]} [Pa]')
        self.valor_velocidad.setText(f'V1: {self.calculo_velocidades[0]} [m/s]\nV2: {self.calculo_velocidades[1]} [m/s]')
        self.valor_altura.setText(f'H1: {self.calculo_alturas[0]} [cm]\nH2: {self.calculo_alturas[1]} [cm]\nDiferencia H: {self.calculo_alturas[2]} [cm]')
        self._presion.setEnabled(True)
        self._velocidad.setEnabled(True)
        self._alturas.setEnabled(True)
        self.boton_plot.setEnabled(False)
        
    def comenzar_timer(self):
        self.tiempo.setInterval(1500)
        self.tiempo.timeout.connect(self.crear_flechas)
        self.tiempo.start()

    def crear_flechas(self):
        flecha = CrearFlechas(self, self.calculo_velocidades)
        flecha.actualizar_pos.connect(self.actualizar_pos_flecha)

    def actualizar_pos_flecha(self, flecha, pos_x, pos_y):
        flecha.move(pos_x, pos_y)

    def rellenar_datos(self):
        self._densidad.addItem('Selecciona una densidad')
        self._densidad.addItem('680             (gasolina)')
        self._densidad.addItem('870             (petróleo)')
        self._densidad.addItem('920     (aceite de cocina)')
        self._densidad.addItem('1000                (agua)')
        self._densidad.addItem('1030         (agua de mar)')
        self._densidad.addItem('1050              (sangre)')
        self._area1.addItem('Selecciona un área')
        self._area1.addItem('3')
        self._area1.addItem('5')
        self._area2.addItem('Selecciona un área')
        self._area2.addItem('3')
        self._area2.addItem('5')

    def opcion_presion(self):
        if self._presion.isChecked() == True:
            self.valor_presion.hide()
        else:
            self.valor_presion.show()

    def opcion_velocidad(self):
        if self._velocidad.isChecked() == True:
            self.valor_velocidad.hide()
        else: 
            self.valor_velocidad.show()

    def opcion_alturas(self):
        if self._alturas.isChecked() == True:
            self.valor_altura.hide()
        else:
            self.valor_altura.show()

    def resetear_todo(self):
        self.tiempo.stop()
        self.condicion_d.hide()
        self.condicion_q.hide()
        self.condicion_a1.hide()
        self.condicion_a2.hide()
        self._presion.setEnabled(False)
        self._velocidad.setEnabled(False)
        self._alturas.setEnabled(False)
        self.boton_plot.setEnabled(False)
        self.boton_datos.setEnabled(True)
        self._presion.setChecked(False)
        self._alturas.setChecked(False)
        self._velocidad.setChecked(False)
        self.densidad_escogida = 0
        self.caudal_escogido = 0
        if self.iteracion != 0:
            self.label.setText(' ')
        self.valor_presion.hide()
        self.valor_velocidad.hide()
        self.valor_altura.hide()
        self.s1.hide()
        self.s2.hide()  
        self.tuberia_escogida = None
        self.area1_escogida = 1
        self.area2_escogida = 1
        self.presion_escogida = 0.98
        self.calculo_presiones = ' '
        self.calculo_velocidades = ' '
        self.calculo_alturas = ' '
        self.contador = 0
        self.programa = None
        self._caudal.setText('1')
        self.remover_parametros()
        self.rellenar_datos()
        self.tiempo = QTimer(self)


    def remover_parametros(self):
        for i in range(7):
            self._densidad.removeItem(0)
        for i in range(3):
            self._area1.removeItem(0)
            self._area2.removeItem(0)


    def closeEvent(self, event):
        close = QMessageBox.question(self,
                            "SALIR",
                            "Si sales ahora, se cerrarán todas las ventanas del programa \n¿Seguro que quieres salir?",
                            QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            self.signal_cerrar_todo.emit()
            event.accept()
        else:
            event.ignore()
