import ui, osc, database
from PyQt6 import QtWidgets
import sys
import utils.log

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    db = database.controller()
    osc = osc.controller('10.4.36.242')
    mainWindow = ui.MainWindow(osc, db)
    mainWindow.setGeometry(500, 300, 800, 550)
    loginWindow = ui.LoginWindow(mainWindow, db)
    loginWindow.show()
    app.exec()
