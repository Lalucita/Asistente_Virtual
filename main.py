import os
os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

def do_something():
    print(window.full_name_lineEdit.text(), "is a", window.occupation_lineEdit.text())
    window.setWindowTitle("User data")

app = QtWidgets.QApplication(sys.argv)
loader = QUiLoader()
window = loader.load("widget.ui", None)

window.submit_button.clicked.connect(do_something)
window.show()
sys.exit(app.exec_())
