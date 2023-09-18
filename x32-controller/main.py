import ui
from PyQt6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ui.MainWindow()
    window.setGeometry(500, 300, 800, 520)
    window.show()
    app.exec()