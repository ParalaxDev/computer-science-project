import math
from random import random
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc, time, core, datetime, ui.error

QLogin = uic.loadUiType("x32-controller/assets/ui/show-control-window.ui")[0]

class ShowControlWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, db: database.controller, osc: osc.controller, userId, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.DB = db
        self.OSC = osc
        self.USERID = userId

        self.CURRENTCUE = 0
        self.CUESTACK = []

        snippets = self.DB.execute(f'SELECT * FROM snippets WHERE user_id = "{self.USERID}"')
        if snippets:
            snippets = snippets.fetchall()
            for snippet in snippets:
                self.CUESTACK.append({
                    "name": snippet[2],
                    "data": [char == '1' for char in snippet[4]]
                })

        self.displayTable.setColumnCount(33)

        test = ['Snippet Number', 'Name']
        header = self.displayTable.horizontalHeader()

        for i in range(32):
            test.append(f"Ch {i + 1}")
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.displayTable.setHorizontalHeaderLabels(test)

        self.redrawTable()

        self.displayTable.cellClicked.connect(lambda row, _: self.setCurrentCue(row))
        self.previousCue.clicked.connect(lambda: self.setCurrentCue(self.CURRENTCUE - 1))
        self.nextCue.clicked.connect(lambda: self.setCurrentCue(self.CURRENTCUE + 1))
        self.newSnippetButton.clicked.connect(self.newSnippet)

    def newSnippet(self):
        newSnippetForm = ui.NewSnippetWindow(self.addSnippet)
        newSnippetForm.exec()

    def redrawTable(self):
        self.displayTable.setRowCount(0)
        for i, vals in enumerate(self.CUESTACK):
            self.writeRow(i, f"{vals['name']}", vals['data'])

    def writeRow(self, num, name, vals):
        self.displayTable.setRowCount(self.displayTable.rowCount())
        self.displayTable.insertRow(num)
        self.displayTable.setItem(num, 0, QtWidgets.QTableWidgetItem(f"{num}"))
        self.displayTable.setItem(num, 1, QtWidgets.QTableWidgetItem(f"{name}"))
        for i, _ in enumerate(vals):
            icon = '■' if _ else ' '
            self.displayTable.setItem(num, i + 2, QtWidgets.QTableWidgetItem(f"{icon}"))

    def addSnippet(self, newChannels):
        compacted = ''.join('1' if boolean else '0' for boolean in newChannels['data'])
        self.DB.execute(f'INSERT INTO snippets (user_id, name, number, bools) VALUES ("{self.USERID}", "{newChannels["name"]}", "{len(self.CUESTACK)}", "{compacted}")')
        self.CUESTACK.append(newChannels)
        self.redrawTable()

    def setCurrentCue(self, newCue):
        self.displayTable.clearSelection()
        self.CURRENTCUE = newCue
        self.currentCue.setText(f'Current Cue: {newCue}')

        self.displayTable.selectRow(newCue)

        print(self.CUESTACK[self.CURRENTCUE])

        for i, val in enumerate(self.CUESTACK[self.CURRENTCUE]['data']):
            print(val)
            self.OSC.send(osc.construct(f'/ch/{str(i + 1).zfill(2)}/mix/on', [{'i': int(val)}]))
