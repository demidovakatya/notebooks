import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()    
        self.initUI()

    def initUI(self):
        # Set font for tooltips
        QToolTip.setFont(QFont('SansSerif', 10))

        # Create a tooltip for the main widget
        self.setToolTip('This is a <b>QWidget</b> widget')

        # In the main widget create a button with text Button
        btn = QPushButton('Button', self)
        # Create a tooltop for the button
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # Recommended size for the button
        btn.resize(btn.sizeHint())
        # Locate
        btn.move(50, 50)

        # x, y, width, height
        self.setGeometry(300, 300, 300, 200)
        # window title
        self.setWindowTitle('Tooltips')

        # Display the main widget
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
