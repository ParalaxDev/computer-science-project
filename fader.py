from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math, random
from OSC import OSC, ConstructOSCMessage


def FloatToDb(float):
    if (float >= 0.5): d = float * 40 - 30
    elif (float >= 0.25): d = float * 80 - 50
    elif (float >= 0.625): d = float * 160 - 70
    elif (float >= 0.0): d = float * 480 - 90
    return d

def DbToFloat(db):
    if (db < -60): f = (db + 90) / 480
    elif (db < -30): f = (db + 70) / 160
    elif (db < -10): f = (db + 50) / 80
    elif (db <= 10): f = (db + 30) / 40
    return int(f * 1023.5) / 1023.0

class Fader(QtWidgets.QWidget):

    def __init__(self, OSC: 'OSC', i, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.OSC = OSC
        self.volume = int(FloatToDb(0.8250))
        self.ID = i

        self.name = f'test {i} {random.randint(0, 999)}'
        self.muted = False
        self.soloed = False
        self.selected = False

        self.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()

        # Add mute button
        self._selectButton = QtWidgets.QPushButton()
        self._selectButton.setText('Select')
        self._selectButton.clicked.connect(self.selectToggle)
        self._selectButton.setCheckable(True)
        layout.addWidget(self._selectButton)

        # Add label
        self._nameLabel = QtWidgets.QLabel()
        self._nameLabel.setText(self.name)
        self._nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self._nameLabel)

        self._volumeSlider = QtWidgets.QSlider()
        self._volumeSlider.setRange(-90, 10)
        self._volumeSlider.setMinimumHeight(300)
        self.helperSetSliderIntValue(self._volumeSlider, self.volume)
        # self._volumeSlider.valueChanged.connect(self.faderUpdate)
        layout.addWidget(self._volumeSlider, alignment=QtCore.Qt.AlignCenter)

        # Add volume label
        self._volumeLabel = QtWidgets.QLabel()
        self._volumeLabel.setText('0db')
        self._volumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self._volumeLabel)
        self.setLayout(layout)

        # Add mute button
        self._muteButton = QtWidgets.QPushButton()
        self._muteButton.setText('Mute')
        self._muteButton.clicked.connect(self.muteToggle)
        self._muteButton.setCheckable(True)
        layout.addWidget(self._muteButton)

        # Add solo button
        self._soloButton = QtWidgets.QPushButton()
        self._soloButton.setText('Solo')
        self._soloButton.setCheckable(True)
        self._soloButton.clicked.connect(self.soloToggle)
        layout.addWidget(self._soloButton)

        self.setLayout(layout)

    def faderUpdate(self, val):
        pass
        # self._volumeLabel.setText(f'{"-∞" if val == -90 else val}db')
        # self.volume = DbToFloat(val)
        # self._volumeSlider.setValue(val)
        # self.helperSetSliderIntValue(self._volumeSlider, val)
        # print(f'UPDATED ID {self.ID} to {self.volume}')
        # self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/mix/fader', [{'f': self.volume}]))

    def muteToggle(self):
        self.muted = not self.muted
        self._muteButton.setText('Muted' if self.muted else 'Mute')

    def soloToggle(self):
        self.soloed = not self.soloed
        self._soloButton.setText('Soloed' if self.soloed else 'Solo')

    def selectToggle(self):
        self.selected = not self.selected
        self._selectButton.setText('Selected' if self.selected else 'Select')

    def helperSetSliderIntValue(self, slider, x):
            slider.tracking = True
            slider.value = int(x)
            slider.sliderPosition = int(x)
            slider.update()
            slider.repaint()
