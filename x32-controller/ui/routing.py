import math
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc, time, core, datetime, ui.error
# import osc, core, utils, ui.widgets

QLogin = uic.loadUiType("x32-controller/assets/ui/routing-window.ui")[0]

class RoutingWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, db: database.controller, osc: osc.controller, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.OSC = osc

        self.updateInputs(32)
        self.updateOutputs(32)

        self.IN = None
        self.OUT = None

        self.OFFSET = 0

        self.inputMatrix.itemClicked.connect(self.setInput)
        self.outputMatrix.itemClicked.connect(self.setOutput)
        self.outputSelect.currentIndexChanged.connect(self.outputsChanged)
        self.unassignButton.clicked.connect(self.unassign)

        p = self.outputMatrix.palette()
        p.setBrush(p.ColorGroup.Inactive, p.ColorRole.Highlight, p.brush(p.ColorRole.Highlight))
        self.outputMatrix.setPalette(p)

        p = self.inputMatrix.palette()
        p.setBrush(p.ColorGroup.Inactive, p.ColorRole.Highlight, p.brush(p.ColorRole.Highlight))
        self.inputMatrix.setPalette(p)

    def setInput(self, item):
        self.IN = int(item.text())
        self.checkRouteComplete()

    def setOutput(self, item):
        self.OUT = int(item.text())
        self.checkRouteComplete()

    def unassign(self):
        self.OSC.send(osc.construct(f"/config/userrout/in/{str(self.IN).zfill(2)}", [{'i': 0}]))

    def checkRouteComplete(self):
        if self.IN and self.OUT:
            self.OSC.send(osc.construct(f"/config/userrout/in/{str(self.IN).zfill(2)}", [{'i': self.OUT + self.OFFSET}]))
            self.IN = None
            self.OUT = None
        elif self.IN:
            res, = self.OSC.send(osc.construct(f"/config/userrout/in/{str(self.IN).zfill(2)}"))
            self.outputMatrix.clearSelection()
            self.unassignButton.setChecked(False)
            self.unassignButton.setText("Unassign")
            if res > 160:
                self.outputsChanged(4)
            elif res > 128:
                self.outputsChanged(3)
            elif res > 80:
                self.outputsChanged(2)
            elif res > 32:
                self.outputsChanged(1)
            elif res > 0:
                self.outputsChanged(0)
            elif res == 0:
                self.unassignButton.setText("Unassigned")
                self.unassignButton.setChecked(True)
            else:
                e = ui.error.ErrorWindow("X32 returned an unexpected value")
                e.show()

            self.setSelected(res)
        elif self.OUT:
            pass
        else:
            pass

    def setSelected(self, res):
        res -= self.OFFSET
        row = int(res / 8) if res % 8 else int(res / 8) - 1
        y = 8 if res % 8 == 0 else res % 8
        test = self.outputMatrix.item(row, y - 1)
        if test:
            test.setSelected(True)

    def outputsChanged(self, index):
        match index:
            case 0:
                self.updateOutputs(32)
                self.OFFSET = 0
            case 1:
                self.updateOutputs(48)
                self.OFFSET = 32
            case 2:
                self.updateOutputs(48)
                self.OFFSET = 80
            case 3:
                self.updateOutputs(32)
                self.OFFSET = 128
            case 4:
                self.updateOutputs(6)
                self.OFFSET = 160

        self.outputSelect.setCurrentIndex(index)

    def updateInputs(self, numOfInputs):
        total = 1

        inputRows = int(numOfInputs/8)

        self.inputMatrix.setRowCount(inputRows)

        row = 0

        for i in range(numOfInputs):
            self.inputMatrix.setItem(row, i%8, QtWidgets.QTableWidgetItem(str(total)))
            total += 1
            if i % 8 >= 7:
                row += 1

    def updateOutputs(self, numOfOutputs):
            total = 1

            inputRows = math.ceil(numOfOutputs/8)

            if numOfOutputs == 6:
                self.outputMatrix.setColumnCount(6)
            else:
                self.outputMatrix.setColumnCount(8)

            self.outputMatrix.setRowCount(inputRows)

            row = 0

            for i in range(numOfOutputs):
                self.outputMatrix.setItem(row, i%8, QtWidgets.QTableWidgetItem(str(total)))
                total += 1
                if i % 8 >= 7:
                    row += 1
