from PyQt6.QtWidgets import QMessageBox

class ErrorWindow(QMessageBox):
    def __init__(self,message):
        super(ErrorWindow, self).__init__()
        self.message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Error")
        self.setText(self.message)
        self.setIcon(QMessageBox.Icon.Question)

        x = self.exec()
        self.show()
