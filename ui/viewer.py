from PySide6.QtWidgets import QSizePolicy, QStackedWidget

from .view_nodes import ViewNodes
from .view_pipes import ViewPipes
from .viwer_grafo import ViwerGraph


class Viewer(QStackedWidget):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.view_nodes = ViewNodes(self.func_update, self)
        self.view_pipes = ViewPipes(self.func_update, self)
        self.view_graph = ViwerGraph(self.func_update, self)

        self.addWidget(self.view_nodes)
        self.addWidget(self.view_pipes)
        self.addWidget(self.view_graph)

        self.currentChanged.connect(lambda *args: self.func_update())

    def update_(self):
        self.view_nodes.update_()
        self.view_pipes.update_()
        self.view_graph.update_()
