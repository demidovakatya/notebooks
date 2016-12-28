import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        # calls constructor for the parent object
        super().__init__()
        # GUI creation is delegated to the initUI() method
        self.initUI()

    def initUI(self):
        # x, y, width, height
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Application Icon")
        self.setWindowIcon(QIcon('web.png'))

        self.show()

if __name__ == '__main__':
    # creates application
    app = QApplication(sys.argv)
    # creates example object, starts the main loop
    ex = Example()
    sys.exit(app.exec_())