import sys
from PyQt5.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # call the statusBar() method of the QMainWindow class
        self.statusBar().showMessage('Ready!')

        self.setGeometry(50, 30, 300, 200)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())