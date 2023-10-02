import os
os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys
from PySide6 import QtWidgets, QtMultimediaWidgets, QtMultimedia, QtCore, QtUiTools
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.window = self.loader.load("widget.ui", None)
        self.window.setWindowTitle("User data")
        self.window.submit_button.clicked.connect(self.load_image)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.view = self.window.graphicsView
        self.scene = QtWidgets.QGraphicsScene()
        self.view.setScene(self.scene)
        layout.addWidget(self.window)
        self.setLayout(layout)

    def load_image(self):
        image_path = 'C:/PYTHON_PYSIDE6/QDesigner_QUiLoader/garfield.jpg'
        try:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                item = QtWidgets.QGraphicsPixmapItem(pixmap)
                self.scene.clear()
                self.scene.addItem(item)
            else:
                print("Failed to load image: pixmap is null.")
        except Exception as e:
            print("Error loading image:", str(e))

def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
