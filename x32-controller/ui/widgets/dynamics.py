from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PySide6.QtCore import QRect
import osc, core, utils
import math

class DynamicsGraph(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )

        self._background_color = QtGui.QColor('gray')
        self._background_color.setAlpha(40)



    def sizeHint(self):
        return QtCore.QSize(210, 260)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        thresh = self.parent().parent().parent().parent().SOURCE.GATE_THRESH
        range = self.parent().parent().parent().parent().SOURCE.GATE_RANGE
        active = self.parent().parent().parent().parent().SOURCE.GATE_ON
        thresh = utils.FloatToFader(thresh, 0, 1, 0, -80)
        range = utils.FloatToFader(range, 0, 1, 60, 0)

        pen = QtGui.QPen()
        pen.setWidth(4)
        pen.setColor(QtGui.QColor('blue') if active else QtGui.QColor('white'))

        painter.setPen(pen)

        w = painter.device().width()
        h = painter.device().height()

        print(min(range, thresh))

        line1 = QtCore.QLineF()
        line1.setP1(QtCore.QPointF((thresh * w), h - (thresh * h)))
        line1.setAngle(45)
        line1.setLength(1000)
        line2 = QtCore.QLineF()
        line2.setP1(QtCore.QPointF((thresh * w), h - (thresh * h)))
        line2.setAngle(-90)
        line2.setLength(range * .75 * h)
        line3 = QtCore.QLineF()
        line3.setP1(line2.p2())
        line3.setAngle(225)
        line3.setLength(1000)

        painter.drawLines([line1, line2, line3])

        painter.drawLines

        painter.end()

    def _trigger_refresh(self):
        self.update()

