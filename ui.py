from PyQt5 import QtCore, QtGui, QtWidgets, uic
from fader import Fader
from OSC import OSC, ConstructOSCMessage
import os

QSettings = uic.loadUiType("pyqt/settings.ui")[0]

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

        self._scrollArea = QtWidgets.QScrollArea(self)
        self._scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self._scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._scrollArea.setMinimumHeight(500)
        faderLayout = QtWidgets.QHBoxLayout(self)
        faderWidget = QtWidgets.QWidget()
        faderWidget.setLayout(faderLayout)

        self._faders = []

        # for i in range(32):
        FADER = Fader(self.OSC, 0)
        FADER.setObjectName(f'fader-{1}')
        FADER.faderUpdate(0)

        FADER1 = Fader(self.OSC, 1)
        FADER1.setObjectName(f'fader-{0}')
        FADER1.faderUpdate(0)
        faderLayout.addWidget(FADER)
        faderLayout.addWidget(FADER1)


            # self._faders.append(FADER)



        self._scrollArea.setWidget(faderWidget)
        self._scrollArea.setWidgetResizable(True)
        self.setCentralWidget(self._scrollArea)
        self._createMenuBar()
        
        
    
    def resizeEvent(self, event):
        print("resize")
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def openSettings(self):
        settings = QSettingsClass(self.OSC)
        settings.exec_()

    def _createMenuBar(self):
        menubar = self.menuBar()
        changeIP = QtWidgets.QAction('Change IP', self)
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(changeIP)
        changeIP.triggered.connect(self.openSettings)
        



if __name__ == "__main__":
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    app = QtWidgets.QApplication([])
    window = Window()
    window.setGeometry(500, 300, 800, 500)
    window.show()
    app.exec_()