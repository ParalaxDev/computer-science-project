import ui
import osc
import database
from PyQt6 import QtWidgets
import sys
import utils.log

if __name__ == "__main__":
    utils.log.setLogging(False)
    app = QtWidgets.QApplication(sys.argv)
    db = database.controller()

    # db.reset()
    # osc = osc.controller('192.168.0.54')
    mainWindow = ui.MainWindow(db)
    loginWindow = ui.LoginWindow(mainWindow, db)
    loginWindow.show()
    app.exec()
