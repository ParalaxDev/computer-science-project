from PyQt6 import QtCore, QtWidgets
import osc
import core
import ui, ui.widgets, database

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, osc: osc.controller, db: database.controller):
        super().__init__(parent=None)

        self.OSC = osc

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
            ch = core.channel(self.OSC, i + 1)
            FADER = ui.widgets.Fader(self.OSC, ch)
            faderLayout.addWidget(FADER)
            self._faders.append(FADER)

        self._scrollArea.setWidget(faderWidget)
        self._scrollArea.setWidgetResizable(True)
        self.setLayout(self._rootLayout)

    def resizeEvent(self, event):
        self._scrollArea.setFixedWidth(self.width())
        self._scrollArea.setFixedHeight(self.height())
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def openSettings(self):
        settings = ui.SettingsWindow(self.OSC)
        settings.exec()

    def _createMenuBar(self):
        menubar = self.menuBar()
        changeIP = QtWidgets.QAction('Change IP', self)
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(changeIP)
        changeIP.triggered.connect(self.openSettings)

    def closeEvent(self, *args, **kwargs):
        # self.OSC.send(ConstructOSCMessage('/shutdown'))
        pass
