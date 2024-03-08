import math
from random import random
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc, time, core, datetime, ui.error

QLogin = uic.loadUiType("x32-controller/assets/ui/new-snippet-window.ui")[0]

class NewSnippetWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, addSnippet, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.addSnippet = addSnippet

        self.buttonBox.accepted.connect(self.saveSnippet)
        self.nameEdit.textChanged.connect(self.nameChanged)

        self.CHANNELS = [False] * 32
        self.NAME = ""

        for i in range(32):
            self.addRow(i)


    def addRow(self, num):
        widget = None
        check = QtWidgets.QCheckBox(f'Channel {num + 1}')
        check.stateChanged.connect(lambda newVal: self.handleCheckbox(num, newVal))
        self.formLayout.addRow(check)
        # , alignment=QtCore.Qt.AlignmentFlag.AlignCenter

    def handleCheckbox(self, channel, newVal):
        self.CHANNELS[channel] = True if newVal != 0 else False

    def nameChanged(self, newName):
        self.NAME = newName

    def saveSnippet(self):
        self.addSnippet({
            "name": self.NAME,
            "data": self.CHANNELS
        })
