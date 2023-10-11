from PyQt6 import QtCore, QtWidgets, QtGui
import osc
import core, utils
import ui, ui.widgets, database

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, osc: osc.controller, db: database.controller):
        super().__init__(parent=None)

        self.OSC = osc
        self.DB = db

        self.userData = -1

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

        self.channels = []
        self.busses = []
        self.matrices = []
        self._faders = []

        for i in range(32):
            ch = core.channel(self.OSC, i + 1)
            self.channels.append(ch)
            FADER = ui.widgets.Fader(self.OSC, ch)
            faderLayout.addWidget(FADER)
            self._faders.append(FADER)

        # for i in range(16):
        #     bus = core.bus(self.OSC, i + 1)
        #     self.busses.append(bus)

        # for i in range(6):
        #     matrix = core.matrix(self.OSC, i + 1)
        #     self.matrices.append(matrix)

        self._scrollArea.setWidget(faderWidget)
        self._scrollArea.setWidgetResizable(True)
        self.setLayout(self._rootLayout)

        self._createMenuBar()

    def resizeEvent(self, event):
        self._scrollArea.setFixedWidth(self.width())
        self._scrollArea.setFixedHeight(self.height())
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def openSettings(self):
        settings = ui.SettingsWindow(self.OSC)
        settings.exec()

    def _createMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')

        changeIP = QtGui.QAction('Change IP', self)
        changeIP.triggered.connect(self.openSettings)
        editMenu.addAction(changeIP)

        save = QtGui.QAction('Save', self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.saveState)
        fileMenu.addAction(save)

        open = QtGui.QAction('Open', self)
        open.setShortcut('Ctrl+O')
        open.triggered.connect(self.openState)
        fileMenu.addAction(open)

    def saveState(self,):
        save = ui.SaveWindow(self.DB, self.userData, self)
        save.show()

    def openState(self):
        open =  ui.OpenWindow(self.DB, self.userData, self)
        open.show()

    def closeEvent(self, *args, **kwargs):
        # self.OSC.send(ConstructOSCMessage('/shutdown'))
        pass
