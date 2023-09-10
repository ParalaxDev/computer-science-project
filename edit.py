from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from OSC import OSC, ConstructOSCMessage
from PySide6.QtCore import QRect
from utils import FloatToDb, DbToFloat, TypeToName


QEdit = uic.loadUiType("ui/edit-window.ui")[0]

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


class QEditClass(QtWidgets.QWidget, QEdit):
    def __init__(self, OSC: 'OSC', id, type, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.OSC = OSC
        self.setWindowTitle(f'Edit {TypeToName(type)} {id + 1}')
        self.ID = id
        self.TYPE = type

        self.gain = 0
        self.lowcut = 20
        self.delay = 0
        self.lowcutToggle = False
        self.delayToggle = False
        self.meter = 0.5

        self.updateMeter(0.5)

        self._meter = _Bar(["#00ff00", "#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#fca503","#fca503", "#fca503", "#fca503", "#fca503", "#ff0000", "#ff0000", "#ff0000"], self)
        self._meter.setGeometry(20, 70, 31, 201)
        
        self._gainDial.valueChanged.connect(self.gainChanged)
        self._lowcutDial.valueChanged.connect(self.lowcutChanged)
        self._delayDial.valueChanged.connect(self.delayChanged)

        self._lowcutToggle.clicked.connect(self.lowcutToggled)
        self._delayToggle.clicked.connect(self.delayToggled)

    def gainChanged(self, val):
        self._gainLevel.setText(f'{"" if val < 0 else "+"}{float(val)}db')
        self.gain = val
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/preamp/trim', [{'f': self.gain}]))

    def lowcutChanged(self, val):
        self._lowcutLevel.setText(f'{val}hz')
        self.lowcut = val
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/eq/1/g', [{'f': self.lowcut}]))

    def delayChanged(self, val):
        self._delayLevel.setText(f'{float(val)}ms')
        self.delay = val
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/delay/time', [{'f': self.delay}]))

    def lowcutToggled(self):
        self.lowcutToggle = not self.lowcutToggle
        self._lowcutToggle.setText('Disable' if self.lowcutToggle else 'Enable')
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/eq/on', [{'f': 1 if self.lowcutToggle else 0}]))
    
    def delayToggled(self):
        self.delayToggle = not self.delayToggle
        self._delayToggle.setText('Disable' if self.delayToggle else 'Enable')
        self.OSC.send(ConstructOSCMessage(f'/ch/{str(self.ID+1).zfill(2)}/delay/on', [{'f': 1 if self.delayToggle else 0}]))

    def updateMeter(self, val):
        self.meter = val
        self._meterLabel.setText(f'{FloatToDb(val)}db')
        # self._meter._trigger_refresh()
