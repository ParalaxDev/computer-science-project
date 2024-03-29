# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit-channel-window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 300)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 401, 301))
        self.tabWidget.setDocumentMode(True)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self._linkToggle = QToolButton(self.config)
        self._linkToggle.setObjectName(u"_linkToggle")
        self._linkToggle.setGeometry(QRect(320, 10, 21, 21))
        self._linkToggle.setCheckable(True)
        self._linkToggle.setChecked(False)
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
        self._lowcutToggle.setAutoDefault(False)

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
        self._delayToggle.setAutoDefault(False)

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
        self._gateGraph = QWidget(self.gate)
        self._gateGraph.setObjectName(u"_gateGraph")
        self._gateGraph.setGeometry(QRect(10, 10, 211, 261))
        self.verticalLayoutWidget_4 = QWidget(self.gate)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(230, 0, 161, 271))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self._gateToggle = QPushButton(self.verticalLayoutWidget_4)
        self._gateToggle.setObjectName(u"_gateToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._gateToggle.sizePolicy().hasHeightForWidth())
        self._gateToggle.setSizePolicy(sizePolicy)
        self._gateToggle.setCheckable(True)
        self._gateToggle.setChecked(False)
        self._gateToggle.setAutoDefault(False)
        self._gateToggle.setFlat(False)

        self.verticalLayout_3.addWidget(self._gateToggle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._threshTitle = QLabel(self.verticalLayoutWidget_4)
        self._threshTitle.setObjectName(u"_threshTitle")
        self._threshTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self._threshTitle)

        self._gateThreshSlider = QSlider(self.verticalLayoutWidget_4)
        self._gateThreshSlider.setObjectName(u"_gateThreshSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self._gateThreshSlider.sizePolicy().hasHeightForWidth())
        self._gateThreshSlider.setSizePolicy(sizePolicy1)
        self._gateThreshSlider.setMinimum(-80)
        self._gateThreshSlider.setMaximum(0)
        self._gateThreshSlider.setValue(-80)
        self._gateThreshSlider.setOrientation(Qt.Vertical)
        self._gateThreshSlider.setInvertedAppearance(False)
        self._gateThreshSlider.setInvertedControls(False)

        self.verticalLayout.addWidget(self._gateThreshSlider)

        self._gateThreshLabel = QLabel(self.verticalLayoutWidget_4)
        self._gateThreshLabel.setObjectName(u"_gateThreshLabel")
        self._gateThreshLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self._gateThreshLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self._rangeTitle = QLabel(self.verticalLayoutWidget_4)
        self._rangeTitle.setObjectName(u"_rangeTitle")
        self._rangeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self._rangeTitle)

        self._gateRangeSlider = QSlider(self.verticalLayoutWidget_4)
        self._gateRangeSlider.setObjectName(u"_gateRangeSlider")
        sizePolicy1.setHeightForWidth(self._gateRangeSlider.sizePolicy().hasHeightForWidth())
        self._gateRangeSlider.setSizePolicy(sizePolicy1)
        self._gateRangeSlider.setMinimum(3)
        self._gateRangeSlider.setMaximum(60)
        self._gateRangeSlider.setValue(60)
        self._gateRangeSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self._gateRangeSlider)

        self._gateRangeLabel = QLabel(self.verticalLayoutWidget_4)
        self._gateRangeLabel.setObjectName(u"_gateRangeLabel")
        self._gateRangeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self._gateRangeLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.gate, "")
        self.dynamics = QWidget()
        self.dynamics.setObjectName(u"dynamics")
        self.verticalLayoutWidget_5 = QWidget(self.dynamics)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(230, 0, 171, 271))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self._dynToggle = QPushButton(self.verticalLayoutWidget_5)
        self._dynToggle.setObjectName(u"_dynToggle")
        sizePolicy.setHeightForWidth(self._dynToggle.sizePolicy().hasHeightForWidth())
        self._dynToggle.setSizePolicy(sizePolicy)
        self._dynToggle.setCheckable(True)
        self._dynToggle.setChecked(False)
        self._dynToggle.setAutoDefault(False)
        self._dynToggle.setFlat(False)

        self.verticalLayout_4.addWidget(self._dynToggle)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self._threshDynTitle = QLabel(self.verticalLayoutWidget_5)
        self._threshDynTitle.setObjectName(u"_threshDynTitle")
        self._threshDynTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self._threshDynTitle)

        self._dynThreshSlider = QSlider(self.verticalLayoutWidget_5)
        self._dynThreshSlider.setObjectName(u"_dynThreshSlider")
        sizePolicy1.setHeightForWidth(self._dynThreshSlider.sizePolicy().hasHeightForWidth())
        self._dynThreshSlider.setSizePolicy(sizePolicy1)
        self._dynThreshSlider.setMinimum(-60)
        self._dynThreshSlider.setMaximum(0)
        self._dynThreshSlider.setValue(-60)
        self._dynThreshSlider.setOrientation(Qt.Vertical)
        self._dynThreshSlider.setInvertedAppearance(False)
        self._dynThreshSlider.setInvertedControls(False)

        self.verticalLayout_5.addWidget(self._dynThreshSlider)

        self._dynThreshLabel = QLabel(self.verticalLayoutWidget_5)
        self._dynThreshLabel.setObjectName(u"_dynThreshLabel")
        self._dynThreshLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self._dynThreshLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self._rangeTitle_2 = QLabel(self.verticalLayoutWidget_5)
        self._rangeTitle_2.setObjectName(u"_rangeTitle_2")
        self._rangeTitle_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self._rangeTitle_2)

        self._dynRatioSlider = QSlider(self.verticalLayoutWidget_5)
        self._dynRatioSlider.setObjectName(u"_dynRatioSlider")
        sizePolicy1.setHeightForWidth(self._dynRatioSlider.sizePolicy().hasHeightForWidth())
        self._dynRatioSlider.setSizePolicy(sizePolicy1)
        self._dynRatioSlider.setMinimum(0)
        self._dynRatioSlider.setMaximum(11)
        self._dynRatioSlider.setValue(6)
        self._dynRatioSlider.setOrientation(Qt.Vertical)
        self._dynRatioSlider.setTickPosition(QSlider.NoTicks)
        self._dynRatioSlider.setTickInterval(12)

        self.verticalLayout_6.addWidget(self._dynRatioSlider)

        self._dynRatioLabel = QLabel(self.verticalLayoutWidget_5)
        self._dynRatioLabel.setObjectName(u"_dynRatioLabel")
        self._dynRatioLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self._dynRatioLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self._gateGraph_2 = QWidget(self.dynamics)
        self._gateGraph_2.setObjectName(u"_gateGraph_2")
        self._gateGraph_2.setGeometry(QRect(10, 10, 211, 261))
        self.tabWidget.addTab(self.dynamics, "")
        self.eq = QWidget()
        self.eq.setObjectName(u"eq")
        self._gateGraph_3 = QWidget(self.eq)
        self._gateGraph_3.setObjectName(u"_gateGraph_3")
        self._gateGraph_3.setGeometry(QRect(10, 10, 380, 255))
        self.tabWidget.addTab(self.eq, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(3)
        self._lowcutToggle.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self._linkToggle.setText(QCoreApplication.translate("Dialog", u"L", None))
        self._phantomToggle.setText(QCoreApplication.translate("Dialog", u"48V", None))
        self._channelName.setText(QCoreApplication.translate("Dialog", u"Channel 1", None))
        self._channelName.setPlaceholderText("")
        self._colourDropdown.setItemText(0, QCoreApplication.translate("Dialog", u"Red", None))
        self._colourDropdown.setItemText(1, QCoreApplication.translate("Dialog", u"Green", None))
        self._colourDropdown.setItemText(2, QCoreApplication.translate("Dialog", u"Yellow", None))
        self._colourDropdown.setItemText(3, QCoreApplication.translate("Dialog", u"Blue", None))
        self._colourDropdown.setItemText(4, QCoreApplication.translate("Dialog", u"Magenta", None))
        self._colourDropdown.setItemText(5, QCoreApplication.translate("Dialog", u"Cyan", None))
        self._colourDropdown.setItemText(6, QCoreApplication.translate("Dialog", u"White", None))

        self._sourceLabel.setText(QCoreApplication.translate("Dialog", u"Source", None))
        self._inputSelect.setItemText(0, QCoreApplication.translate("Dialog", u"In01", None))

        self._gainLevel.setText(QCoreApplication.translate("Dialog", u"+0.0db", None))
        self._lowcutLabel.setText(QCoreApplication.translate("Dialog", u"Low Cut", None))
        self._lowcutToggle.setText(QCoreApplication.translate("Dialog", u"Enable", None))
        self._lowcutLevel.setText(QCoreApplication.translate("Dialog", u"20Hz", None))
        self._delayLabel.setText(QCoreApplication.translate("Dialog", u"Delay", None))
        self._delayToggle.setText(QCoreApplication.translate("Dialog", u"Enable", None))
        self._delayLevel.setText(QCoreApplication.translate("Dialog", u"0.3ms", None))
        self._meterLabel.setText(QCoreApplication.translate("Dialog", u"0db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), QCoreApplication.translate("Dialog", u"Config", None))
        self._gateToggle.setText(QCoreApplication.translate("Dialog", u"Enable Gate", None))
        self._threshTitle.setText(QCoreApplication.translate("Dialog", u"Threshold", None))
        self._gateThreshLabel.setText(QCoreApplication.translate("Dialog", u"-80.0db", None))
        self._rangeTitle.setText(QCoreApplication.translate("Dialog", u"Range", None))
        self._gateRangeLabel.setText(QCoreApplication.translate("Dialog", u"60.0db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gate), QCoreApplication.translate("Dialog", u"Gate", None))
        self._dynToggle.setText(QCoreApplication.translate("Dialog", u"Enable Dynamics", None))
        self._threshDynTitle.setText(QCoreApplication.translate("Dialog", u"Threshold", None))
        self._dynThreshLabel.setText(QCoreApplication.translate("Dialog", u"-80.0db", None))
        self._rangeTitle_2.setText(QCoreApplication.translate("Dialog", u"Ratio", None))
        self._dynRatioLabel.setText(QCoreApplication.translate("Dialog", u"60.0db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dynamics), QCoreApplication.translate("Dialog", u"Dynamics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eq), QCoreApplication.translate("Dialog", u"EQ", None))
    # retranslateUi

