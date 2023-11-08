from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc, time, core
# import osc, core, utils, ui.widgets

QLogin = uic.loadUiType("x32-controller/assets/ui/save-as-window.ui")[0]

class SaveAsWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, db: database.controller, user: int, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.user = user
        self.db = db

        self.saveName = ''

        self._nameEdit.textChanged.connect(self.nameUpdate)
        self._saveButton.clicked.connect(self.savePressed)

    def nameUpdate(self, val):
        self.saveName = val

    def savePressed(self):
        print(len(self.saveName))
        if len(self.saveName) <= 0:
            error = ui.ErrorWindow('Save name should be at least 1 character long')
            error.show()
            return
        else:
            currentTime = int(time.time())
            self.db.execute(f'INSERT INTO saves (name, created_at, updated_at, user_id) VALUES ("{self.saveName}", "{currentTime}", "{currentTime}", "{self.user}")')
            saveId = self.db.cursor.lastrowid if isinstance(self.db.cursor.lastrowid, int) else -1

            if saveId == -1:
                error = ui.ErrorWindow('Could not create save column in database')
                error.show()
            else:
                channels:list[core.channel] = self.parent().channels

                for num, ch in enumerate(channels):
                    ch.saveValuesToDb(self.db, saveId, num + 1)
