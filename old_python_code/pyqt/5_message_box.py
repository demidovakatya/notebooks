from PyQt5.QtWidgets import *
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 20, 300, 200)
        self.setWindowTitle("Message box")
        self.show()

    # built-in function: how to behave on close
    def closeEvent(self, event):
        # Creates a message box (title, text, options, default)
        reply = QMessageBox.question(self, 'Message',
            'Do you really want to quit?', QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())