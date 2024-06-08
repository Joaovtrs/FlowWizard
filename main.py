import sys

from PySide6.QtWidgets import QApplication

from ui import MainUI

# from qt_material import apply_stylesheet


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    window = MainUI()
    # apply_stylesheet(qt, theme='dark_blue.xml')
    window.show()

    sys.exit(qt.exec())
