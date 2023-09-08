from PyQt6 import QtCore, QtGui, QtWidgets, uic
from fader import Fader
from OSC import OSC, ConstructOSCMessage
import os
import sys
import time

QSettings = uic.loadUiType("ui/settings.ui")[0]

class QSettingsClass(QtWidgets.QDialog, QSettings):
    def __init__(self, OSC: 'OSC', parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.OSC = OSC
        self.lineEdit.setText(self.OSC.IP if self.OSC.IP else 'Unknown')
        self.buttonBox.accepted.connect(self._submitSettings)

    def _submitSettings(self):
        print(f'submitted {self.lineEdit.text()}')
        # TODO: IP validation
        self.OSC.setIP(self.lineEdit.text())

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.OSC = OSC('127.0.0.1')

        self._rootLayout = QtWidgets.QHBoxLayout()

        self._scrollArea = QtWidgets.QScrollArea(self)
        self._scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self._scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._scrollArea.setMinimumHeight(500)
        self._scrollArea.setFixedWidth(800)


        faderLayout = QtWidgets.QHBoxLayout(self)
        faderWidget = QtWidgets.QWidget()
        faderWidget.setLayout(faderLayout)

        self._scrollArea.setWidget(faderWidget)
        self._rootLayout.addWidget(self._scrollArea)

        self._faders = []

        for i in range(32):
            FADER = Fader(self.OSC, i)
            FADER.setObjectName(f'fader-{i}')
            FADER.faderUpdate(0)
            faderLayout.addWidget(FADER)
            self._faders.append(FADER)

        self._scrollArea.setWidget(faderWidget)
        self._scrollArea.setWidgetResizable(True)
        self.setLayout(self._rootLayout)
        # self._createMenuBar()
        
        
    
    def resizeEvent(self, event):
        self._scrollArea.setFixedWidth(self.width())
        self._scrollArea.setFixedHeight(self.height())
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def openSettings(self):
        settings = QSettingsClass(self.OSC)
        settings.exec()

    def _createMenuBar(self):
        menubar = self.menuBar()
        changeIP = QtWidgets.QAction('Change IP', self)
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(changeIP)
        changeIP.triggered.connect(self.openSettings)
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 520)
    window.show()
    app.exec()