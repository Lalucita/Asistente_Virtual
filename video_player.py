import os
os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys
import time
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtUiTools import QUiLoader

from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)

from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide6.QtCore import Signal

from ventana2 import MiVentana2



class MiVentana(QMainWindow):

    signal_abrir_ventana2 = Signal()
    

    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('cargar_video.ui')

        self.resize(800, 600)
        self.setCentralWidget(self.ui)

        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._video_widget = QVideoWidget()

        self.mi_widget = self.ui.findChild(QWidget, 'widget')

        layout = QVBoxLayout()
        layout.addWidget(self._video_widget)  # Agregar el QVideoWidget al diseño
        self.mi_widget.setLayout(layout)  
        

        
        self._player.setVideoOutput(self._video_widget)

        # Conectar el evento de clic del botón
        self.cargar_video()
        self.ui.submit_button.clicked.connect(self.on_submit_button_clicked)

    def cargar_video(self):
        ruta_del_archivo = 'Outputs/person.avi'
        url = QtCore.QUrl.fromLocalFile(ruta_del_archivo)

        self._player.setSource(url)
        self._player.play()


    def on_submit_button_clicked(self):
        texto = self.ui.lineEdit.text()
        print("Texto en el QLineEdit:", texto)


        self.signal_abrir_ventana2.emit()
        self.close()
        
        # Cerrar esta ventana
        
        # Crear una nueva instancia de QApplication si no tienes una ya
        #app = QApplication.instance()
        #if app is None:
         #   app = QApplication([])
        
        #self.close()
    
        #run_window_(texto)

        # Abrir una nueva ventana
        #self.close()
        
        



def run_window():
    app = QApplication(sys.argv)
    ventana = MiVentana()

    ventana2 = MiVentana2()

    ventana.signal_abrir_ventana2.connect(ventana2.mostrar_ventana)

    ventana.show()
    sys.exit(app.exec_())
    




