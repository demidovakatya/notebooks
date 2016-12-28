# Necessary import s
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # The QWidget widget is the base class of all user interface objects in PyQt5.
    w = QWidget()
    w.resize(200, 150)
    w.move(30,50)
    w.setWindowTitle("Simple Window")
    # Display the widget on the screen
    w.show()

    # Provides a clean exit
    sys.exit(app.exec_())