import ui, osc, database
from PyQt6 import QtWidgets
import sys
import utils.log

if __name__ == "__main__":
    utils.log.setLogging(True)
    app = QtWidgets.QApplication(sys.argv)
    db = database.controller()
    # db.reset()
    osc = osc.controller('192.168.0.54')
    mainWindow = ui.MainWindow(osc, db)
    mainWindow.setGeometry(500, 300, 800, 550)
    loginWindow = ui.LoginWindow(mainWindow, db)
    loginWindow.show()
    app.exec()
