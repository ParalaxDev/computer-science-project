import ui, osc
from PyQt6 import QtWidgets
import sys

if __name__ == "__main__":
    osc = osc.controller('10.4.36.147')
    app = QtWidgets.QApplication(sys.argv)
    window = ui.MainWindow(osc)
    window.setGeometry(500, 300, 800, 520)
    window.show()
    app.exec()