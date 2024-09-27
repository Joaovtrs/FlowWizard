from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSizePolicy


class MainManuButton(QPushButton):
    def __init__(self, text, path=None, parent=None):
        super().__init__(text, parent)

        self.path = path

        self.text = text
        self.setMinimumSize(10, 50)
        self.setMaximumSize(180, 50)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.resizeEvent = lambda args: self.btn_resize()

        self.setStyleSheet(
            """QPushButton:disabled {
         border: 1px solid #aa0000;
         }"""
        )

        if self.path is not None:
            icon = QIcon(self.path)
            self.setIcon(icon)

    def btn_resize(self):

        if not self.icon().isNull():
            if self.width() < 150:
                self.setText("")
            else:
                self.setText(self.text)
