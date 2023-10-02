from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PySide6.QtCore import QRect
import osc, core, utils

class GateGraph(QtWidgets.QWidget):
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
        thresh = utils.FloatToFader(thresh, 0, 1, 0, -80)

        pen = QtGui.QPen()
        pen.setWidth(4)
        pen.setColor(QtGui.QColor('white'))

        painter.setPen(pen)

        w = painter.device().width()
        h = painter.device().height()

        line1 = QtCore.QLineF(0 + (thresh * w), h - (thresh * h), w, 0)
        line2 = QtCore.QLineF(0 + (thresh * w), h - (thresh * h), 0 + (thresh * w), h)

        


        painter.drawLines([line1, line2])

        painter.drawLines

        painter.end()

    def _trigger_refresh(self):
        self.update()

