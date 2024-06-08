import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel, QSizePolicy, QSpacerItem,
                               QVBoxLayout)


class Plot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(figure=fig)


class ViwerGrafo(QFrame):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_titulo = QLabel('Grafo')
        self.lbl_titulo.setAlignment(Qt.AlignHCenter)
        self.lbl_titulo.setFont(QFont('Times', 20))

        self.separdor_titulo = QFrame(self)
        self.separdor_titulo.setFrameShape(QFrame.HLine)

        self.plot = Plot(self)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )

        self.grid.addWidget(self.lbl_titulo)
        self.grid.addWidget(self.separdor_titulo)
        self.grid.addWidget(self.plot)
        self.grid.addItem(self.spacer)

    def atualizar(self):
        pass
