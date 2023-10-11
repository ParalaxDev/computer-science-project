from PyQt6 import QtCore, QtGui, QtWidgets, uic
import hashlib, database, ui, re, utils.log, osc
# import osc, core, utils, ui.widgets

QLogin = uic.loadUiType("x32-controller/assets/ui/login-window.ui")[0]

class LoginWindow(QtWidgets.QDialog, QLogin):
    def __init__(self, mainWindow: ui.MainWindow, db: database.controller, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.db = db
        self.mainWindow = mainWindow

        self.username = ''
        self.hashedPassword = ''
        self.password = ''
        self._usernameField.textChanged.connect(self.usernameUpdate)
        self._passwordField.textChanged.connect(self.passwordUpdate)

        self._loginButton.clicked.connect(self.login)
        self._createAccountButton.clicked.connect(self.createAccount)

    def usernameUpdate(self, val):
        self.username = val

    def passwordUpdate(self, val):
        sha256 = hashlib.sha256()
        sha256.update(bytes(val, 'utf-8'))
        self.password = val
        self.hashedPassword = sha256.hexdigest()

    def login(self):
        try:
            user, = self.db.execute(f'SELECT id from users where name = "{self.username}" and hashed_password = "{self.hashedPassword}"').fetchone()
        except:
            user = None
        if not user:
            error = ui.ErrorWindow(f'Your username or password is incorrect')
            error.show()
        else:
            self.mainWindow.show()
            self.mainWindow.userData = user
            self.mainWindow.setGeometry(500, 300, 800, 550)
            self.hide()

            utils.log.info(f'user signed in as {user}')

    def createAccount(self):
        fail = False
        error = None

        if len(self.db.execute(f'SELECT * from users where name = "{self.username}"').fetchall()) > 0:
            error = ui.ErrorWindow(f'A user already exists with the name "{self.username}"')
            fail = True
        elif len(self.password) < 8:
            fail = True
            error = ui.ErrorWindow('Password must be at least 8 characters long')
        elif re.search('[0-9]', self.password) is None:
            fail = True
            error = ui.ErrorWindow('Password must contain a number')
        elif re.search('[A-Z]', self.password) is None:
            fail = True
            error = ui.ErrorWindow('Password must contain a capital letter')
        elif re.search('[$&+,:;=?@#|<>.^*()%!-]', self.password) is None:
            fail = True
            error = ui.ErrorWindow('Password must contain a special character [$&+,:;=?@#|<>.^*()%!-]')

        if fail and error:
            error.show()
            utils.log.warn('Couldn\'t create account')
        else:
            self.db.execute(f'INSERT INTO users (name, hashed_password) VALUES ("{self.username}", "{self.hashedPassword}")')
            error = ui.ErrorWindow('Created Account')
            error.show()
            utils.log.info('Created account')
