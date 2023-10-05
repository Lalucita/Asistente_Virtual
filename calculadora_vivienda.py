import os
os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader



class Calculadora_vivienda(QMainWindow):


    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('vistas/calculadora_vivienda.ui')

        self.resize(460, 380)
        self.setCentralWidget(self.ui)
        #self.ui.button_atras.clicked.connect(self.mostrarInicio)
        self.ui.button_calcular.clicked.connect(self.calcular_monto)
        self.widget_monto=self.ui.findChild(QWidget,'widget_monto_calculado')
        self.widget_monto.hide()

    def calcular_monto(self):
        self.widget_monto.show()

    def mostrar_inicio(self):
        
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora_vivienda()
    ventana.show()
    app.exec_()
