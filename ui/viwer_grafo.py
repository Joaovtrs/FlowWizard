import matplotlib
import networkx as nx

from system import system

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Plot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        self.parent = parent
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(figure=fig)

        graph = system.circuit.graph()
        if nx.is_planar(graph):
            nx.draw_planar(graph, ax=self.axes, with_labels=True)
        else:
            nx.draw(graph, ax=self.axes, with_labels=True)


class ViwerGraph(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_title = QLabel('Grafo')
        self.lbl_title.setAlignment(Qt.AlignHCenter)
        self.lbl_title.setFont(QFont('Times', 20))

        self.separator_title = QFrame(self)
        self.separator_title.setFrameShape(QFrame.HLine)

        self.plot = Plot(self)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.separator_title)
        self.grid.addWidget(self.plot)
        self.grid.addItem(self.spacer)

    def update_(self):
        self.clear_layout(self.grid)

        self.lbl_title = QLabel('Grafo')
        self.lbl_title.setAlignment(Qt.AlignHCenter)
        self.lbl_title.setFont(QFont('Times', 20))

        self.separator_title = QFrame(self)
        self.separator_title.setFrameShape(QFrame.HLine)

        self.plot = Plot(self)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.separator_title)
        self.grid.addWidget(self.plot)
        self.grid.addItem(self.spacer)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
