import os
os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtUiTools import QUiLoader

from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)

from PySide6.QtMultimediaWidgets import QVideoWidget



from calculadora_vivienda import Calculadora_vivienda




class Inicio_av(QMainWindow):


    nombre_opciones=True
    video_buenas_tardes='Avatar/buenas_tardes_avatar.mp4'
    video_que_te_puedo_ayudar='Avatar/ayudar_.mp4'
    nombre_cliente=""

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Inicio')
        loader = QUiLoader()
        self.ui = loader.load('vistas/inicio_av.ui')

        self.resize(460, 380)
        self.setCentralWidget(self.ui)

        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._video_widget = QVideoWidget()

        self.widget_botones=self.ui.findChild(QWidget,'widget_botones')
        self.widget_nombre=self.ui.findChild(QWidget,'widget_nombre')
        self.mi_widget = self.ui.findChild(QWidget, 'widget')

        layout = QVBoxLayout()
        layout.addWidget(self._video_widget)  # Agregar el QVideoWidget al diseño
        self.mi_widget.setLayout(layout)  
        

        
        self._player.setVideoOutput(self._video_widget)

        # Conectar el evento de clic del botón
        self.cargar_video(self.video_buenas_tardes)
        self.ui.nombre_button.clicked.connect(self.on_nombre_button_clicked)
        self.ui.button_vivienda.clicked.connect(self.calculadora_vivienda)
        self.ocultarWidget_botones()

    
        

    def cargar_video(self, ruta_video):
        url = QtCore.QUrl.fromLocalFile(ruta_video)
        self._player.setSource(url)
        self._player.play()


    def on_nombre_button_clicked(self):
        self.nombre_cliente = self.ui.nombre_edit.text()
        print("Texto en el QLineEdit:", self.nombre_cliente)
        self.mostrar_Widget_botones()
        self.widget_nombre.hide()
        self.ui.label_nombre.setText("Hola "+self.nombre_cliente+"  ")
        self.cargar_video(self.video_que_te_puedo_ayudar)


    def ocultarWidget_botones(self):
        # Ocultar el QWidget
        self.widget_botones.hide()

    def mostrar_Widget_botones(self):
        # Ocultar el QWidget
        self.widget_botones.show()

    def calculadora_vivienda(self):
        self.calculadora = Calculadora_vivienda()  # Pasar la instancia de InicioAv a CalculadoraV
        self.calculadora.show()
        self.hide()

    
        
        



def run_window():
    app = QApplication(sys.argv)
    ventana = Inicio_av()

    ventana.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    run_window()




