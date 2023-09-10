from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import math, random, time
from OSC import OSC, ConstructOSCMessage
from edit import QEditClass
from utils import FloatToDb, DbToFloat, TypeToName
from channel import Channel

class _Bar(QtWidgets.QWidget):
    def __init__(self, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )

        if isinstance(steps, list):
            # list of colors.
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps, int):
            # int number of bars, defaults to red.
            self.n_steps = steps
            self.steps = ['red'] * steps

        else:
            raise TypeError('steps must be a list or int')

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._background_color.setAlpha(0)
        self._padding = 3.0  # n-pixel gap around edge.


    def sizeHint(self):
        return QtCore.QSize(30,60)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state.
        meter = self.parent().meter

        # Define our canvas.
        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        # Draw the bars.
        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent
        bar_spacer = step_size * (1 - self._bar_solid_percent) / 2

        # Calculate the y-stop position, from the value in range.
        n_steps_to_draw = int(meter * self.n_steps)

        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            rect = QtCore.QRect(
                int(self._padding),
                int(self._padding + d_height - ((1 + n) * step_size) + bar_spacer),
                int(d_width),
                int(bar_height)
            )
            painter.fillRect(rect, brush)

        painter.end()

    def _trigger_refresh(self):
        self.update()


class Fader(QtWidgets.QWidget):

    def __init__(self, OSC: 'OSC', channel: 'Channel', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.OSC = OSC
        self.CHANNEL = channel
        
        self.muted = False
        self.soloed = False
        self.selected = False

        self.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()

        # Add label
        self._nameLabel = QtWidgets.QLabel()
        self._nameLabel.setText(self.name)
        self._nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._nameLabel)

        self._selectButton = QtWidgets.QPushButton()
        self._selectButton.setText('Select')
        self._selectButton.clicked.connect(self.selectToggle)
        # self._selectButton.setCheckable(True)
        layout.addWidget(self._selectButton)

        self._bar = _Bar(["#00ff00", "#00ff00", "#fca503", "#fca503", "#fca503", "#ff0000"])
        layout.addWidget(self._bar, alignment=Qt.AlignmentFlag.AlignCenter)

        self._volumeSlider = QtWidgets.QSlider()
        self._volumeSlider.setRange(-90, 10)
        self._volumeSlider.setMinimumHeight(300)
        self.helperSetSliderIntValue(self._volumeSlider, self.volume)
        self._volumeSlider.valueChanged.connect(self.faderUpdate)
        layout.addWidget(self._volumeSlider, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add volume label
        self._volumeLabel = QtWidgets.QLabel()
        self._volumeLabel.setText('0db')
        self._volumeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._volumeLabel)
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

        self.setLayout(layout)

    def meterUpdate(self, val):
        self.meter = val
        self._bar._trigger_refresh()


    def faderUpdate(self, val):
        self._volumeLabel.setText(f'{"-∞" if val == -90 else val}db')
        self.volume = DbToFloat(val)
        self._volumeSlider.setValue(val)
        self.meterUpdate(DbToFloat(val))
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/mix/fader', [{'f': self.volume}]))

    def muteToggle(self):
        self.muted = not self.muted
        self._muteButton.setText('Muted' if self.muted else 'Mute')
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/mix/on', [{'f': 1 if self.muted else 0}]))

    def soloToggle(self):
        self.soloed = not self.soloed
        self._soloButton.setText('Soloed' if self.soloed else 'Solo')
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/mix/on', [{'f': 1 if self.muted else 0}]))

    def selectToggle(self):
        self.selected = not self.selected
        if self.selected:
            self.edit = QEditClass(self.OSC, self.ID, self.TYPE)
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
