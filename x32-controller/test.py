import ui.routing, database, osc, sys
from PyQt6 import QtWidgets

db = database.controller()
osc = osc.controller('192.168.0.2')

app = QtWidgets.QApplication(sys.argv)

routing = ui.RoutingWindow(db, osc)
routing.show()

routing.raise_()

app.exec()
