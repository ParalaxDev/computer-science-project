# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit-window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(401, 300)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 401, 301))
        self.tabWidget.setDocumentMode(True)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self._linkToggle = QToolButton(self.config)
        self._linkToggle.setObjectName(u"_linkToggle")
        self._linkToggle.setGeometry(QRect(320, 10, 21, 21))
        self._linkToggle.setCheckable(True)
        self._phantomToggle = QToolButton(self.config)
        self._phantomToggle.setObjectName(u"_phantomToggle")
        self._phantomToggle.setGeometry(QRect(350, 10, 31, 21))
        self._phantomToggle.setCheckable(True)
        self._channelName = QLineEdit(self.config)
        self._channelName.setObjectName(u"_channelName")
        self._channelName.setGeometry(QRect(10, 10, 113, 21))
        self._channelName.setFrame(False)
        self._colourDropdown = QComboBox(self.config)
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.addItem("")
        self._colourDropdown.setObjectName(u"_colourDropdown")
        self._colourDropdown.setGeometry(QRect(130, 10, 81, 26))
        self.verticalLayoutWidget = QWidget(self.config)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 40, 311, 241))
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self._sourceLabel = QLabel(self.verticalLayoutWidget)
        self._sourceLabel.setObjectName(u"_sourceLabel")
        self._sourceLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._sourceLabel, 0, 0, 1, 1)

        self._inputSelect = QComboBox(self.verticalLayoutWidget)
        self._inputSelect.addItem("")
        self._inputSelect.setObjectName(u"_inputSelect")
        self._inputSelect.setMinimumContentsLength(1)

        self.gridLayout.addWidget(self._inputSelect, 1, 0, 1, 1)

        self._gainDial = QDial(self.verticalLayoutWidget)
        self._gainDial.setObjectName(u"_gainDial")
        self._gainDial.setMinimum(-12)
        self._gainDial.setMaximum(60)
        self._gainDial.setSingleStep(0)
        self._gainDial.setTracking(True)
        self._gainDial.setOrientation(Qt.Horizontal)
        self._gainDial.setInvertedAppearance(False)
        self._gainDial.setInvertedControls(False)
        self._gainDial.setNotchesVisible(False)

        self.gridLayout.addWidget(self._gainDial, 3, 0, 1, 1)

        self._gainLevel = QLabel(self.verticalLayoutWidget)
        self._gainLevel.setObjectName(u"_gainLevel")
        self._gainLevel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._gainLevel, 2, 0, 1, 1)

        self._lowcutLabel = QLabel(self.verticalLayoutWidget)
        self._lowcutLabel.setObjectName(u"_lowcutLabel")
        self._lowcutLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._lowcutLabel, 0, 1, 1, 1)

        self._lowcutToggle = QPushButton(self.verticalLayoutWidget)
        self._lowcutToggle.setObjectName(u"_lowcutToggle")
        self._lowcutToggle.setCheckable(True)

        self.gridLayout.addWidget(self._lowcutToggle, 1, 1, 1, 1)

        self._lowcutDial = QDial(self.verticalLayoutWidget)
        self._lowcutDial.setObjectName(u"_lowcutDial")
        self._lowcutDial.setMinimum(20)
        self._lowcutDial.setMaximum(400)

        self.gridLayout.addWidget(self._lowcutDial, 3, 1, 1, 1)

        self._lowcutLevel = QLabel(self.verticalLayoutWidget)
        self._lowcutLevel.setObjectName(u"_lowcutLevel")
        self._lowcutLevel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._lowcutLevel, 2, 1, 1, 1)

        self._delayLabel = QLabel(self.verticalLayoutWidget)
        self._delayLabel.setObjectName(u"_delayLabel")
        self._delayLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._delayLabel, 0, 2, 1, 1)

        self._delayToggle = QPushButton(self.verticalLayoutWidget)
        self._delayToggle.setObjectName(u"_delayToggle")
        self._delayToggle.setCheckable(True)

        self.gridLayout.addWidget(self._delayToggle, 1, 2, 1, 1)

        self._delayLevel = QLabel(self.verticalLayoutWidget)
        self._delayLevel.setObjectName(u"_delayLevel")
        self._delayLevel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self._delayLevel, 2, 2, 1, 1)

        self._delayDial = QDial(self.verticalLayoutWidget)
        self._delayDial.setObjectName(u"_delayDial")
        self._delayDial.setMinimum(0)
        self._delayDial.setMaximum(300)
        self._delayDial.setSingleStep(1)

        self.gridLayout.addWidget(self._delayDial, 3, 2, 1, 1)

        self._meter = QWidget(self.config)
        self._meter.setObjectName(u"_meter")
        self._meter.setGeometry(QRect(20, 40, 31, 201))
        self._meterLabel = QLabel(self.config)
        self._meterLabel.setObjectName(u"_meterLabel")
        self._meterLabel.setGeometry(QRect(10, 250, 51, 20))
        self._meterLabel.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.config, "")
        self.gate = QWidget()
        self.gate.setObjectName(u"gate")
        self.tabWidget.addTab(self.gate, "")
        self.dynamics = QWidget()
        self.dynamics.setObjectName(u"dynamics")
        self.tabWidget.addTab(self.dynamics, "")
        self.eq = QWidget()
        self.eq.setObjectName(u"eq")
        self.tabWidget.addTab(self.eq, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self._linkToggle.setText(QCoreApplication.translate("Form", u"L", None))
        self._phantomToggle.setText(QCoreApplication.translate("Form", u"48V", None))
        self._channelName.setText(QCoreApplication.translate("Form", u"Channel 1", None))
        self._channelName.setPlaceholderText("")
        self._colourDropdown.setItemText(0, QCoreApplication.translate("Form", u"Red", None))
        self._colourDropdown.setItemText(1, QCoreApplication.translate("Form", u"Green", None))
        self._colourDropdown.setItemText(2, QCoreApplication.translate("Form", u"Yellow", None))
        self._colourDropdown.setItemText(3, QCoreApplication.translate("Form", u"Blue", None))
        self._colourDropdown.setItemText(4, QCoreApplication.translate("Form", u"Pink", None))
        self._colourDropdown.setItemText(5, QCoreApplication.translate("Form", u"Cyan", None))
        self._colourDropdown.setItemText(6, QCoreApplication.translate("Form", u"White", None))

        self._sourceLabel.setText(QCoreApplication.translate("Form", u"Source", None))
        self._inputSelect.setItemText(0, QCoreApplication.translate("Form", u"In01", None))

        self._gainLevel.setText(QCoreApplication.translate("Form", u"+0.0db", None))
        self._lowcutLabel.setText(QCoreApplication.translate("Form", u"Low Cut", None))
        self._lowcutToggle.setText(QCoreApplication.translate("Form", u"Enable", None))
        self._lowcutLevel.setText(QCoreApplication.translate("Form", u"20Hz", None))
        self._delayLabel.setText(QCoreApplication.translate("Form", u"Delay", None))
        self._delayToggle.setText(QCoreApplication.translate("Form", u"Enable", None))
        self._delayLevel.setText(QCoreApplication.translate("Form", u"0.3ms", None))
        self._meterLabel.setText(QCoreApplication.translate("Form", u"0db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), QCoreApplication.translate("Form", u"Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gate), QCoreApplication.translate("Form", u"Gate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dynamics), QCoreApplication.translate("Form", u"Dynamics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eq), QCoreApplication.translate("Form", u"EQ", None))
    # retranslateUi

