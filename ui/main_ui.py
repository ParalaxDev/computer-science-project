# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(16777215, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Channel 8", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Channel 9", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Channel 10", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Channel 11", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Channel 12", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Channel 13", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Channel 14", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Channel 15", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Channel 16", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Channel 17", None));
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Channel 18", None));
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Channel 19", None));
        ___qlistwidgetitem19 = self.listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Channel 20", None));
        ___qlistwidgetitem20 = self.listWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Channel 21", None));
        ___qlistwidgetitem21 = self.listWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Channel 22", None));
        ___qlistwidgetitem22 = self.listWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Channel 23", None));
        ___qlistwidgetitem23 = self.listWidget.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Channel 24", None));
        ___qlistwidgetitem24 = self.listWidget.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Channel 25", None));
        ___qlistwidgetitem25 = self.listWidget.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Channel 26", None));
        ___qlistwidgetitem26 = self.listWidget.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Channel 27", None));
        ___qlistwidgetitem27 = self.listWidget.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Channel 28", None));
        ___qlistwidgetitem28 = self.listWidget.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Channel 29", None));
        ___qlistwidgetitem29 = self.listWidget.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Channel 30", None));
        ___qlistwidgetitem30 = self.listWidget.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Channel 31", None));
        ___qlistwidgetitem31 = self.listWidget.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Channel 32", None));
        ___qlistwidgetitem32 = self.listWidget.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Bus 1", None));
        ___qlistwidgetitem33 = self.listWidget.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Bus 2", None));
        ___qlistwidgetitem34 = self.listWidget.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Bus 3", None));
        ___qlistwidgetitem35 = self.listWidget.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Bus 4", None));
        ___qlistwidgetitem36 = self.listWidget.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Bus 5", None));
        ___qlistwidgetitem37 = self.listWidget.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Bus 6", None));
        ___qlistwidgetitem38 = self.listWidget.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Bus 7", None));
        ___qlistwidgetitem39 = self.listWidget.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Bus 8", None));
        ___qlistwidgetitem40 = self.listWidget.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Bus 9", None));
        ___qlistwidgetitem41 = self.listWidget.item(41)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Bus 10", None));
        ___qlistwidgetitem42 = self.listWidget.item(42)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Bus 11", None));
        ___qlistwidgetitem43 = self.listWidget.item(43)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Bus 12", None));
        ___qlistwidgetitem44 = self.listWidget.item(44)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Bus 13", None));
        ___qlistwidgetitem45 = self.listWidget.item(45)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Bus 14", None));
        ___qlistwidgetitem46 = self.listWidget.item(46)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Bus 15", None));
        ___qlistwidgetitem47 = self.listWidget.item(47)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Bus 16", None));
        ___qlistwidgetitem48 = self.listWidget.item(48)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Matrix 1", None));
        ___qlistwidgetitem49 = self.listWidget.item(49)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Matrix 2", None));
        ___qlistwidgetitem50 = self.listWidget.item(50)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Matrix 3", None));
        ___qlistwidgetitem51 = self.listWidget.item(51)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Matrix 4", None));
        ___qlistwidgetitem52 = self.listWidget.item(52)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Matrix 5", None));
        ___qlistwidgetitem53 = self.listWidget.item(53)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Matrix 6", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"-\u221e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"+10db", None))
    # retranslateUi

