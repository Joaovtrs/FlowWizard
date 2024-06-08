from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel, QSizePolicy, QSpacerItem,
                               QVBoxLayout)


class ViewConexoes(QFrame):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_titulo = QLabel('Conexões')
        self.lbl_titulo.setAlignment(Qt.AlignHCenter)
        self.lbl_titulo.setFont(QFont('Times', 20))

        self.separdor_titulo = QFrame(self)
        self.separdor_titulo.setFrameShape(QFrame.HLine)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )

        self.grid.addWidget(self.lbl_titulo)
        self.grid.addWidget(self.separdor_titulo)
        self.grid.addItem(self.spacer)

    def atualizar(self):
        pass
