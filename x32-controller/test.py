import ui.routing, database, osc, sys
from PyQt6 import QtWidgets

db = database.controller()
osc = osc.controller('10.4.37.56')

app = QtWidgets.QApplication(sys.argv)

routing = ui.ShowControlWindow(db, osc, 1)
routing.show()

routing.raise_()

app.exec()
