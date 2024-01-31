from PyQt6 import QtCore, QtWidgets, QtGui
import osc
import core, utils
import ui, ui.widgets, database
from types import UnionType

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, db: database.controller):
        super().__init__(parent=None)

        self.DB = db

        self.userData = -1

        self._rootLayout = QtWidgets.QHBoxLayout()

        self._tabGroup = QtWidgets.QTabWidget(self)
        self._tabGroup.setDocumentMode(True)
        self._tabGroup.setFixedWidth(800)
        self._tabGroup.setMinimumHeight(550)
        self._tabGroup.setCurrentIndex(1)

        self._rootLayout.addWidget(self._tabGroup)

        self._channels = self.generateFaderBank()
        self._buses = self.generateFaderBank()
        self._matrices = self.generateFaderBank()
        self._dcas = self.generateFaderBank()

        self._tabGroup.addTab(self._channels, 'Channels')
        self._tabGroup.addTab(self._buses, 'Buses')
        self._tabGroup.addTab(self._matrices, 'Matrices')
        self._tabGroup.addTab(self._dcas, 'DCAs')

        self.channels = []
        self.buses = []
        self.matrices = []
        self.dcas = []

        self.channelFaders: list[ui.widgets.Fader] = []
        self.busFaders: list[ui.widgets.Fader] = []
        self.matrixFaders: list[ui.widgets.Fader] = []
        self.dcaFaders: list[ui.widgets.Fader] = []

        self.mode = 'normal'
        self.selectedFader: None | core.channel | core.bus | core.matrix = None

        self.setLayout(self._rootLayout)

        self._createMenuBar()

    def generateFaderBank(self):
        scrollArea = QtWidgets.QScrollArea(self._tabGroup)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scrollArea.setMinimumHeight(550)
        scrollArea.setMinimumWidth(800)
        scrollArea.setWidgetResizable(True)

        faderBankLayout = QtWidgets.QHBoxLayout(self)
        faderBankWidget = QtWidgets.QWidget()
        faderBankWidget.setLayout(faderBankLayout)
        scrollArea.setWidget(faderBankWidget)

        return scrollArea

    def loadData(self, osc):
        self.OSC = osc
        if self.OSC:
            for i in range(32):
                ch = core.channel(self.OSC, i + 1)
                ch.updateName(f'Channel {i+1}')
                self.channels.append(ch)
                FADER = ui.widgets.Fader(i, self.OSC, ch)

                self._channels.findChildren(QtWidgets.QWidget)[0].findChildren(QtWidgets.QHBoxLayout)[0].addWidget(FADER)
                self.channelFaders.append(FADER)

            for i in range(16):
                bus = core.bus(self.OSC, i + 1)
                bus.updateName(f'Bus {i+1}')
                self.buses.append(bus)
                FADER = ui.widgets.Fader(i, self.OSC, bus)

                self._buses.findChildren(QtWidgets.QWidget)[0].findChildren(QtWidgets.QHBoxLayout)[0].addWidget(FADER)
                self.busFaders.append(FADER)

            for i in range(8):
                matrix = core.bus(self.OSC, i + 1)
                matrix.updateName(f'Matrix {i+1}')
                self.matrices.append(matrix)
                FADER = ui.widgets.Fader(i, self.OSC, matrix)

                self._matrices.findChildren(QtWidgets.QWidget)[0].findChildren(QtWidgets.QHBoxLayout)[0].addWidget(FADER)
                self.matrixFaders.append(FADER)

    def redraw(self, type='all'):
        print('REDRAW CALLED')
        faders: list[ui.widgets.Fader] = []
        match type:
            case 'ch':
                faders += self.channelFaders
            case 'bus':
                faders += self.busFaders
            case 'mtx':
                faders += self.matrixFaders
            case 'dca':
                faders += self.matrixFaders
            case _:
                faders += self.channelFaders + self.busFaders + self.matrixFaders + self.dcaFaders

        for fader in faders:
            fader.redraw()

    def resizeEvent(self, event):
        self._tabGroup.setFixedWidth(self.width())
        self._tabGroup.setFixedHeight(self.height())
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def openSettings(self):
        settings = ui.SettingsWindow(self.DB, user=self.userData, oldOsc=self.OSC)
        settings.exec()

    def _createMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')

        changeIP = QtGui.QAction('Edit Settings', self)
        changeIP.triggered.connect(self.openSettings)
        editMenu.addAction(changeIP)

        save = QtGui.QAction('Save', self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.saveState)
        fileMenu.addAction(save)

        saveAs = QtGui.QAction('Save As', self)
        saveAs.setShortcut('Ctrl+Alt+S')
        saveAs.triggered.connect(self.saveAsState)
        fileMenu.addAction(saveAs)

        open = QtGui.QAction('Open', self)
        open.setShortcut('Ctrl+O')
        open.triggered.connect(self.openState)
        fileMenu.addAction(open)

        sendOnFaders = QtGui.QAction('Send on Faders', self)
        sendOnFaders.setShortcut('Ctrl+F')
        sendOnFaders.triggered.connect(self.changeMode)
        fileMenu.addAction(sendOnFaders)


    def setSelectedFader(self, newFader: core.channel | core.bus | core.matrix | None):
        self.selectedFader = newFader

    def changeMode(self):
        if self.mode == 'normal' and self.selectedFader != None:
            self.mode = 'sof'
            self._sofWarning = QtWidgets.QLabel(self)
            self._sofWarning.setText(f"WARNING: YOU'RE EDITING THE SENDS FOR {self.selectedFader.NAME}")
            self._sofWarning.setGeometry(0, 0, self.frameGeometry().width(), 25)
            self._sofWarning.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self._sofWarning.show()
            self._sofWarning.setStyleSheet('background-color: #e64843')
            self._tabGroup.setCurrentIndex(1)
        elif self.mode == 'sof' and self._sofWarning:
            self.mode = 'normal'
            self._sofWarning.hide()
            self._tabGroup.setCurrentIndex(0)
        else:
            error = ui.ErrorWindow('There was an error entering SOF mode, try selecting a channel.')
            error.show()

        self.redraw('bus')

    def saveAsState(self):
        save = ui.SaveAsWindow(self.DB, self.userData, self)
        save.show()

    def saveState(self):
        save = ui.SaveWindow(self.DB, self.userData, self)
        save.show()

    def openState(self):
        open =  ui.OpenWindow(self.DB, self.userData, self)
        open.show()

    def closeEvent(self, *args, **kwargs):
        # self.OSC.send(ConstructOSCMessage('/shutdown'))
        pass
