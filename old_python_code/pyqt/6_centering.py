import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        # the window is centered by the custom method center()
        self.center()

        self.setWindowTitle("Center")
        self.show()

    def center(self):
        # get geometry of the widget relative to its parent
        qr = self.frameGeometry()
        # get screen resolution and its center
        cp = QDesktopWidget().availableGeometry().center()
        # set the center of the rectangle to the center of the window
        qr.moveCenter(cp)
        # move the top-left point of the app to the top-left point of the widget
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())