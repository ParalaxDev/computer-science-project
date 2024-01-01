from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import osc, core, utils, ui, ui.widgets

class Fader(QtWidgets.QWidget):
    def __init__(self, i, OSC: osc.controller, source: core.channel or core.bus or core.matrix, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.OSC = OSC
        self.SOURCE = source

        self.muted = False
        self.soloed = False
        self.selected = False
        self.faderId = i

        self.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()

        # Add label
        self._nameLabel = QtWidgets.QLabel()
        self._nameLabel.setText(self.SOURCE.NAME)
        self._nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._nameLabel)

        self._editButton = QtWidgets.QPushButton()
        self._editButton.setText('Edit')
        self._editButton.clicked.connect(self.editPressed)
        # self._selectButton.setCheckable(True)
        layout.addWidget(self._editButton)

        self._bar = ui.widgets.Meter(["#00ff00", "#00ff00", "#fca503", "#fca503", "#fca503", "#ff0000"])
        layout.addWidget(self._bar, alignment=Qt.AlignmentFlag.AlignCenter)

        self._gainSlider = QtWidgets.QSlider()
        self._gainSlider.setRange(-90, 10)
        self._gainSlider.setMinimumHeight(300)
        self.helperSetSliderIntValue(self._gainSlider, self.SOURCE.GAIN)
        self._gainSlider.valueChanged.connect(self.faderUpdate)
        layout.addWidget(self._gainSlider, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add volume label
        self._gainLabel = QtWidgets.QLabel()
        self._gainLabel.setText('0db')
        self._gainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._gainLabel)
        self.setLayout(layout)

        # Add mute button
        self._muteButton = QtWidgets.QPushButton()
        self._muteButton.setText('Mute')
        self._muteButton.clicked.connect(self.muteToggle)
        self._muteButton.setCheckable(True)
        layout.addWidget(self._muteButton)

        self._selectButton = QtWidgets.QPushButton()
        self._selectButton.setText('Select')
        self._selectButton.clicked.connect(self.selectToggle)
        self._selectButton.setCheckable(True)
        layout.addWidget(self._selectButton)

        self._muteButton.setChecked(self.SOURCE.MUTE)
        self._muteButton.setText('Muted' if self.SOURCE.MUTE else 'Mute')

        self._gainLabel.setText(f'{"-∞" if utils.FloatToDb(self.SOURCE.GAIN) == -90 else utils.FloatToDb(self.SOURCE.GAIN)}db')
        self._gainSlider.setValue(int(utils.FloatToFader(self.SOURCE.GAIN)))

        self.setLayout(layout)

        # self.mainWindow:ui.MainWindow = self.parent().parent().parent().parent().parent().parent()


    def selectToggle(self):
        mainWindow: ui.MainWindow = self.parent().parent().parent().parent().parent().parent()

        if mainWindow.selectedFader != None and mainWindow.selectedFader.UID == self.SOURCE.UID:
            mainWindow.setSelectedFader(None)
            self._selectButton.setChecked(False)
            self._selectButton.setText('Select')

        else:
            mainWindow.setSelectedFader(self.SOURCE)
            assert(mainWindow.selectedFader)
            self._selectButton.setChecked(True if mainWindow.selectedFader.UID == self.SOURCE.UID else False)
            self._selectButton.setText('Selected' if mainWindow.selectedFader.UID == self.SOURCE.UID else 'Select')

        mainWindow.redraw()

    def redraw(self, type=''):
        print('FADER REDRAW CALLED')

        mainWindow: ui.MainWindow = self.parent().parent().parent().parent().parent().parent()
        selected = mainWindow.selectedFader

        self._nameLabel.setText(self.SOURCE.NAME)

        match self.SOURCE.TYPE:
            case 'bus':
                self._gainSlider.valueChanged.disconnect()
                self._muteButton.clicked.disconnect()
                if mainWindow.selectedFader != None and mainWindow.mode == "sof":
                    busId = self.SOURCE.ID - 1
                    self._gainSlider.valueChanged.connect(self.sofUpdate)
                    self._muteButton.clicked.connect(self.sofMute)

                    self._muteButton.setChecked(selected.BUS_SENDS[busId].ON)
                    self._muteButton.setText('Muted' if selected.BUS_SENDS[busId].ON else 'Mute')

                    self._gainLabel.setText(f'{"-∞" if utils.FloatToDb(selected.BUS_SENDS[busId].LEVEL) == -90 else utils.FloatToDb(selected.BUS_SENDS[busId].LEVEL)}db')
                    self._gainSlider.setValue(int(utils.FloatToFader(selected.BUS_SENDS[busId].LEVEL)))
                else:
                    self._gainSlider.valueChanged.connect(self.faderUpdate)
                    self._muteButton.clicked.connect(self.muteToggle)
                    self._nameLabel.setText(self.SOURCE.NAME)

                    self._muteButton.setChecked(self.SOURCE.MUTE)
                    self._muteButton.setText('Muted' if self.SOURCE.MUTE else 'Mute')

                    self._gainLabel.setText(f'{"-∞" if utils.FloatToDb(self.SOURCE.GAIN) == -90 else utils.FloatToDb(self.SOURCE.GAIN)}db')
                    self._gainSlider.setValue(int(utils.FloatToFader(self.SOURCE.GAIN)))

        if selected != None:
            self._selectButton.setChecked(True if selected.UID == self.SOURCE.UID else False)
            self._selectButton.setText('Selected' if selected.UID == self.SOURCE.UID else 'Select')

    def sofMute(self):
        busId = self.SOURCE.ID - 1
        selected: core.channel = self.parent().parent().parent().parent().parent().parent().selectedFader
        selected.updateBusSendMutes(busId, not selected.BUS_SENDS[busId].ON)
        self._muteButton.setChecked(selected.BUS_SENDS[busId].ON)
        self._muteButton.setText('Muted' if selected.BUS_SENDS[busId].ON else 'Mute')

    def sofUpdate(self, newVal):
        busId = self.SOURCE.ID - 1
        selected: core.channel = self.parent().parent().parent().parent().parent().parent().selectedFader
        selected.updateBusSendLevels(busId, utils.DbToFloat(newVal))
        # print(utils.FloatToDb(selected.BUS_SENDS[busId].LEVEL), selected.BUS_SENDS[busId].LEVEL)
        self._gainLabel.setText(f'{"-∞" if newVal == -90 else newVal}db')

    def meterUpdate(self, val):
        self.meter = val
        self._bar._trigger_refresh()

    def faderUpdate(self, val):
        self._gainLabel.setText(f'{"-∞" if val == -90 else val}db')
        self._gainSlider.setValue(val)
        self.SOURCE.updateGain(utils.DbToFloat(val))

    def muteToggle(self):
        self.SOURCE.updateMute(not self.SOURCE.MUTE)
        self._muteButton.setChecked(self.SOURCE.MUTE)
        self._muteButton.setText('Muted' if self.SOURCE.MUTE else 'Mute')

    def editPressed(self):
        if self.SOURCE.TYPE == 'ch':
            self.edit = ui.EditChannelWindow(self.OSC, self.SOURCE, self)
            self.edit.show()
        else:
            utils.log.warn('Other types have not been implemented yet')

    def helperSetSliderIntValue(self, slider, x):
            slider.tracking = True
            slider.value = int(x)
            slider.sliderPosition = int(x)
            slider.update()
            slider.repaint()
