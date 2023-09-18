from PyQt6 import QtCore, QtGui, QtWidgets, uic
import osc

QSettings = uic.loadUiType("x32-controller/assets/ui/settings.ui")[0]

class SettingsWindow(QtWidgets.QDialog, QSettings):
    def __init__(self, OSC: osc.controller, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.OSC = OSC
        self.lineEdit.setText(self.OSC.IP if self.OSC.IP else 'Unknown')
        self.buttonBox.accepted.connect(self._submitSettings)

    def _submitSettings(self):
        print(f'submitted {self.lineEdit.text()}')
        # TODO: IP validation
        self.OSC.setIP(self.lineEdit.text())