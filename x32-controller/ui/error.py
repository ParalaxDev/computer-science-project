from PyQt6.QtWidgets import QMessageBox
# from PyQt6.QtGui import*
# from PyQt6.QtCore

class ErrorWindow(QMessageBox):
    def __init__(self,message):
        super(ErrorWindow,self).__init__()     #use super class of QMainWindow
        self.message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Error")
        self.setText(self.message)
        self.setIcon(QMessageBox.Icon.Critical)

        x = self.exec()
