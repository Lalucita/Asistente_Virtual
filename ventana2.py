import os
#os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtUiTools import QUiLoader

from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)

from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide6.QtCore import Slot

class MiVentana2(QMainWindow):

    nombre_cliente=""

    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('ventana2.ui')

        self.resize(800, 600)
        self.setCentralWidget(self.ui)

        

        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._video_widget = QVideoWidget()

        self.mi_widget = self.ui.findChild(QWidget, 'widget_ventana2')

        layout = QVBoxLayout()
        layout.addWidget(self._video_widget)  # Agregar el QVideoWidget al diseño
        self.mi_widget.setLayout(layout)  
        

        
        self._player.setVideoOutput(self._video_widget)

        # Conectar el evento de clic del botón
        self.cargar_video()


        self.ui.pushButton.clicked.connect(self.on_submit_button_clicked)

        

    def cargar_video(self):
        ruta_del_archivo = 'Outputs/person.avi'
        url = QtCore.QUrl.fromLocalFile(ruta_del_archivo)

        self._player.setSource(url)
        self._player.play()


    def on_submit_button_clicked(self):
        print("click")
        ruta_del_archivo = 'Outputs/person.avi'
        url = QtCore.QUrl.fromLocalFile(ruta_del_archivo)

        self._player.setSource(url)
        self._player.play()

    def mostrar_ventana(self, nombre):
        self.set_nombre(nombre)
        self.show()

    def set_nombre(self, nombre):
        self.nombre_cliente=nombre
        self.ui.nombre_label.setText("Hola, "+self.nombre_cliente+" En que te puedo ayudar?")



def run_window_(nombre):
    """app = QApplication.instance()  # Obtiene la instancia existente si existe
    if not app:  # Si no hay una instancia existente, crea una nueva
        app = QApplication(sys.argv)"""
    
    ventana = MiVentana2()
    print("entra por acaa "+nombre)
    ventana.set_nombre(nombre)
    ventana.show()
    #sys.exit(app.exec_())




"""
def run_window_(nombre):
    #app = QApplication(sys.argv)  # Crea una nueva instancia de QApplication
    ventana = MiVentana2()
    ventana.set_nombre(nombre)
    ventana.show()  # Inicia el bucle de eventos de la aplicación

"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiVentana2()
    sys.exit(app.exec_())
