import sys

sys.path.append("..")

from PyQt5.QtWidgets import QApplication
from ventana_principal import VentanaInicio
from ventana_desarrollo import VentanaDesarrollo
from informaciones import VentanaInformacion
from ventana_instrucciones import VentanaInstrucciones
from ventana_area import VentanaArea
from ventana_densidad import VentanaDensidad
from ventana_caudal import VentanaCaudal








if __name__ == '__main__':
    app = QApplication([])
    '''
    TODAS LAS VENTANAS

    '''
    primera_ventana = VentanaInicio()
    segunda_ventana = VentanaDesarrollo()
    tercera_ventana = VentanaInformacion()
    cuarta_ventana = VentanaInstrucciones()
    ventana_area_ = VentanaArea()
    ventana_caudal_ = VentanaCaudal()
    ventana_densidad_ = VentanaDensidad()

    '''
    SEÑALES
    '''    
    primera_ventana.mostrar()
    primera_ventana.ir_programa.clicked.connect(segunda_ventana.mostrar)
    primera_ventana.ir_programa.clicked.connect(primera_ventana.esconder)
    segunda_ventana._volver.clicked.connect(primera_ventana.mostrar)
    segunda_ventana._volver.clicked.connect(segunda_ventana.esconder)
    segunda_ventana._volver.clicked.connect(ventana_caudal_.esconder)
    segunda_ventana._volver.clicked.connect(ventana_densidad_.esconder)
    segunda_ventana._volver.clicked.connect(ventana_area_.esconder)
    segunda_ventana.boton_datos.clicked.connect(segunda_ventana.recibir_parametros)
    segunda_ventana._presion.pressed.connect(segunda_ventana.opcion_presion)
    segunda_ventana._velocidad.pressed.connect(segunda_ventana.opcion_velocidad)
    segunda_ventana._alturas.pressed.connect(segunda_ventana.opcion_alturas)
    segunda_ventana.boton_plot.clicked.connect(segunda_ventana.comenzar_timer)
    segunda_ventana.boton_plot.clicked.connect(segunda_ventana.mostrar_opciones)
    segunda_ventana.resetear.clicked.connect(segunda_ventana.resetear_todo)
    primera_ventana.informacion.clicked.connect(tercera_ventana.mostrar)
    primera_ventana._instrucciones.clicked.connect(cuarta_ventana.mostrar)
    cuarta_ventana.volver_menu.clicked.connect(cuarta_ventana.esconder)
    segunda_ventana.signal_info_densidad.connect(ventana_densidad_.mostrar)
    segunda_ventana.signal_info_area.connect(ventana_area_.mostrar)
    segunda_ventana.signal_info_caudal.connect(ventana_caudal_.mostrar)
    segunda_ventana.signal_cerrar_todo.connect(ventana_densidad_.esconder)
    segunda_ventana.signal_cerrar_todo.connect(ventana_caudal_.esconder)
    segunda_ventana.signal_cerrar_todo.connect(ventana_area_.esconder)
    sys.exit(app.exec_())






