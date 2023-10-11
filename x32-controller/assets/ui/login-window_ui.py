# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login-window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 326)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(27)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self._loginButton = QPushButton(Dialog)
        self._loginButton.setObjectName(u"_loginButton")

        self.gridLayout.addWidget(self._loginButton, 5, 0, 1, 1)

        self._createAccountButton = QPushButton(Dialog)
        self._createAccountButton.setObjectName(u"_createAccountButton")

        self.gridLayout.addWidget(self._createAccountButton, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self._usernameField = QLineEdit(self.frame)
        self._usernameField.setObjectName(u"_usernameField")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self._usernameField)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self._passwordField = QLineEdit(self.frame)
        self._passwordField.setObjectName(u"_passwordField")
        self._passwordField.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self._passwordField)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Virtual X32 Controller", None))
        self._loginButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self._createAccountButton.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

