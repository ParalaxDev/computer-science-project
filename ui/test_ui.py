# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QSizePolicy,
    QSlider, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 801, 561))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.channel1Frame = QFrame(self.horizontalLayoutWidget)
        self.channel1Frame.setObjectName(u"channel1Frame")
        self.channel1Frame.setMaximumSize(QSize(75, 16777215))
        self.faderLayout = QVBoxLayout(self.channel1Frame)
#ifndef Q_OS_MAC
        self.faderLayout.setSpacing(-1)
#endif
        self.faderLayout.setObjectName(u"faderLayout")
        self.faderLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.faderLayout.setContentsMargins(5, 10, 5, 10)
        self.channel1Label = QLabel(self.channel1Frame)
        self.channel1Label.setObjectName(u"channel1Label")
        self.channel1Label.setMaximumSize(QSize(75, 16777215))
        self.channel1Label.setAlignment(Qt.AlignCenter)

        self.faderLayout.addWidget(self.channel1Label)

        self.channel1Fader = QSlider(self.channel1Frame)
        self.channel1Fader.setObjectName(u"channel1Fader")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel1Fader.sizePolicy().hasHeightForWidth())
        self.channel1Fader.setSizePolicy(sizePolicy)
        self.channel1Fader.setMaximumSize(QSize(75, 16777215))
        self.channel1Fader.setOrientation(Qt.Vertical)

        self.faderLayout.addWidget(self.channel1Fader)

        self.channel1Level = QLabel(self.channel1Frame)
        self.channel1Level.setObjectName(u"channel1Level")
        self.channel1Level.setMaximumSize(QSize(75, 16777215))
        self.channel1Level.setAlignment(Qt.AlignCenter)

        self.faderLayout.addWidget(self.channel1Level)


        self.horizontalLayout.addWidget(self.channel1Frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.channel1Label.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.channel1Level.setText(QCoreApplication.translate("MainWindow", u"-5.0db", None))
    # retranslateUi

