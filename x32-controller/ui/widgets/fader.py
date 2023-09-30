from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import osc, core, utils, ui, ui.widgets

class Fader(QtWidgets.QWidget):
    def __init__(self, OSC: osc.controller, source: core.channel, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.OSC = OSC
        self.SOURCE = source
        
        self.muted = False
        self.soloed = False
        self.selected = False

        self.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()

        # Add label
        self._nameLabel = QtWidgets.QLabel()
        self._nameLabel.setText(self.SOURCE.NAME)
        self._nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._nameLabel)

        self._selectButton = QtWidgets.QPushButton()
        self._selectButton.setText('Select')
        self._selectButton.clicked.connect(self.selectToggle)
        # self._selectButton.setCheckable(True)
        layout.addWidget(self._selectButton)

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

        # Add solo button
        # self._soloButton = QtWidgets.QPushButton()
        # self._soloButton.setText('Solo')
        # self._soloButton.setCheckable(True)
        # self._soloButton.clicked.connect(self.soloToggle)
        # layout.addWidget(self._soloButton)

        self._muteButton.setChecked(self.SOURCE.MUTE)
        self._muteButton.setText('Muted' if self.SOURCE.MUTE else 'Mute')

        self._gainLabel.setText(f'{"-∞" if utils.FloatToDb(self.SOURCE.GAIN) == -90 else utils.FloatToDb(self.SOURCE.GAIN)}db')
        self._gainSlider.setValue(int(utils.FloatToFader(self.SOURCE.GAIN)))
        print(self.SOURCE.GAIN)



        self.setLayout(layout)

    def meterUpdate(self, val):
        self.meter = val
        self._bar._trigger_refresh()

    def faderUpdate(self, val):
        self._gainLabel.setText(f'{"-∞" if val == -90 else val}db')
        self._gainSlider.setValue(val)
        self.SOURCE.updateGain(utils.DbToFloat(val))

    def muteToggle(self):
        self.SOURCE.updateMute(not self.SOURCE.MUTE)
        print(self.SOURCE.MUTE)
        self._muteButton.setChecked(self.SOURCE.MUTE)
        self._muteButton.setText('Muted' if self.SOURCE.MUTE else 'Mute')

    def selectToggle(self):
        self.selected = not self.selected
        if self.selected:
            self.edit = ui.EditWindow(self.OSC, self.SOURCE)
            self.edit.show()
            # self.edit
            # self.edit.closeEvent
        else:
            self.edit = None

        # self._selectButton.setText('Selected' if self.selected else 'Select')

    def helperSetSliderIntValue(self, slider, x):
            slider.tracking = True
            slider.value = int(x)
            slider.sliderPosition = int(x)
            slider.update()
            slider.repaint()
