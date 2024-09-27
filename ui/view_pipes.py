from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout


class ViewPipes(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_title = QLabel("Trechos")
        self.lbl_title.setAlignment(Qt.AlignHCenter)
        self.lbl_title.setFont(QFont("Times", 20))

        self.separator_title = QFrame(self)
        self.separator_title.setFrameShape(QFrame.HLine)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.separator_title)
        self.grid.addItem(self.spacer)

    def update_(self):
        pass
