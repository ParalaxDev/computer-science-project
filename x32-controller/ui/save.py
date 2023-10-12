from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc, time, core, datetime
# import osc, core, utils, ui.widgets

QLogin = uic.loadUiType("x32-controller/assets/ui/overwrite-window.ui")[0]

class SaveWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, db: database.controller, user: int, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.user = user
        self.db = db

        self.selectedSaveId = -1

        self._saveButton.clicked.connect(self.overwriteSave)

        self.saves = self.db.execute(f'SELECT * FROM saves WHERE user_id = "{self.user}"')

        if self.saves:
            self.saves = self.saves.fetchall()
            self._table.setRowCount(len(self.saves))
            self._table.clicked.connect(self.selectItem)

            for row, save in enumerate(self.saves):
                self._table.setItem(row, 0, QtWidgets.QTableWidgetItem(save[1]))
                self._table.setItem(row, 1, QtWidgets.QTableWidgetItem(datetime.datetime.utcfromtimestamp(float(save[2])).strftime('%H:%M:%S %d-%m-%y')))
                self._table.setItem(row, 2, QtWidgets.QTableWidgetItem(datetime.datetime.utcfromtimestamp(float(save[3])).strftime('%H:%M:%S %d-%m-%y')))
        else:
            utils.log.error('error loading saves from db')

    def selectItem(self, item):
        if isinstance(self.saves, list):
            self.selectedSaveId = self.saves[item.row()][0]

    def overwriteSave(self):

        print('updating save :))')

        channels:list[core.channel] = self.parent().channels

        if not isinstance(self.selectedSaveId, int):
            error = ui.ErrorWindow('You didn\'t select a save to update')
            error.show()
            return

        for num, channel in enumerate(channels):
            channel.updateValuesInDb(self.db, self.selectedSaveId, num + 1)

        self.db.execute(f'UPDATE saves SET updated_at = "{int(time.time())}" WHERE id = {self.selectedSaveId}')

        self.parent().redraw()
