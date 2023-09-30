import ui, osc
from PyQt6 import QtWidgets
import sys
import utils.log

if __name__ == "__main__":
    utils.log.setLogging(True)
    osc = osc.controller('192.168.0.54')
    app = QtWidgets.QApplication(sys.argv)
    window = ui.MainWindow(osc)
    window.setGeometry(500, 300, 800, 550)
    window.show()
    app.exec()