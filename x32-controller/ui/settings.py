from PyQt6 import QtCore, QtGui, QtWidgets, uic
import osc
import ui
import database

QSettings = uic.loadUiType("x32-controller/assets/ui/settings-window.ui")[0]


class SettingsWindow(QtWidgets.QDialog, QSettings):
    def __init__(self, db: database.controller, mainWindow: ui.MainWindow | None = None, user=None, setup=False, oldOsc: osc.controller | None = None, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.osc: None | osc.controller = None
        self.mainWindow = mainWindow
        self.user = user
        self.setup = setup
        self.oldOsc = oldOsc
        self.db = db

        self.ip = [0, 0, 0, 0]
        self.port = 10024
        self.live = False

        res = self.db.execute(
            f'SELECT saved_ip, saved_port, saved_live_mode from users where id = "{user}"')
        if res:
            ip, port, live = res.fetchone()

            if ip:
                ip = ip.split('.')
                self.ip = ip
                self._ipSelect1.setValue(int(ip[0]))
                self._ipSelect2.setValue(int(ip[1]))
                self._ipSelect3.setValue(int(ip[2]))
                self._ipSelect4.setValue(int(ip[3]))
            if port:
                self.port = int(port)
                self._portEdit.setText(port)
            if live:
                self.live = not bool(live)
                self._modeSelect.setCurrentIndex(live)

        if setup:
            self.label_6.setText("Setup")

        self._ipSelect1.valueChanged.connect(lambda val: self.ipUpdate(0, val))
        self._ipSelect2.valueChanged.connect(lambda val: self.ipUpdate(1, val))
        self._ipSelect3.valueChanged.connect(lambda val: self.ipUpdate(2, val))
        self._ipSelect4.valueChanged.connect(lambda val: self.ipUpdate(3, val))

        self._portEdit.textChanged.connect(self.portEdit)

        self._modeSelect.currentIndexChanged.connect(self.modeChange)

        self._testButton.clicked.connect(self.testConnection)

        self._save.clicked.connect(self.saveSettings)

    def testConnection(self):
        if self.live:
            msg = ui.ErrorWindow(
                f'You cannot run a network test whilst in live mode')
            msg.show()
            return

        testOsc = osc.controller('.'.join(str(x)
                                 for x in self.ip), port=self.port, live=True)

        testMsg = osc.construct('/info')
        res = testOsc.send(testMsg)

        if len(res) > 1:
            msg = ui.ErrorWindow(
                f'OSC server {res[1]} is running {res[0]} and {res[2]} is running firmware {res[3]}')
            msg.show()

    def modeChange(self, val):
        self.live = False if val == 0 else True

    def ipUpdate(self, idx, val):
        if val >= 0 and val <= 255:
            self.ip[idx] = val
        else:
            error = ui.ErrorWindow('IP must be a valid ip between 0 and 255')
            error.show()

        print(self.ip)

    def portEdit(self, val):
        try:
            self.port = int(val)
        except:
            error = ui.ErrorWindow('Invalid port number')
            error.show()

    def saveSettings(self, val):
        if self.setup:
            assert (self.mainWindow)
            assert (self.user)
            self.osc = osc.controller(
                '.'.join(str(x) for x in self.ip), port=self.port, live=self.live)

            self.mainWindow.show()
            self.mainWindow.userData = self.user
            self.mainWindow.setGeometry(500, 300, 800, 600)
            self.mainWindow.loadData(self.osc)
        else:
            assert (self.oldOsc)
            self.oldOsc.setIP('.'.join(str(x) for x in self.ip))
            self.oldOsc.setPort(self.port)
            self.oldOsc.setLive(self.live)

        assert (self.user)

        self.db.execute(
            f'UPDATE users SET saved_ip = "{".".join(str(x) for x in self.ip)}", saved_port = "{self.port}", saved_live_mode = {self.live} WHERE id = {self.user}')
        self.hide()
