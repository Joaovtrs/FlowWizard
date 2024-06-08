import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from system import System
from ui import MainUI

if __name__ == '__main__':
    qt = QApplication(sys.argv)

    window = MainUI(System())
    apply_stylesheet(qt, theme='dark_teal.xml')
    window.show()

    sys.exit(qt.exec())
