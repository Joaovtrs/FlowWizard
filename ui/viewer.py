from PySide6.QtWidgets import QSizePolicy, QStackedWidget

from .view_conexoes import ViewConexoes
from .view_trechos import ViewTrechos
from .viwer_grafo import ViwerGrafo


class Viewer(QStackedWidget):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.view_conexoes = ViewConexoes(self.func_atualizar, self)
        self.view_trechos = ViewTrechos(self.func_atualizar, self)
        self.view_grafo = ViwerGrafo(self.func_atualizar, self)

        self.addWidget(self.view_conexoes)
        self.addWidget(self.view_trechos)
        self.addWidget(self.view_grafo)

        self.currentChanged.connect(lambda *args: self.func_atualizar())

    def atualizar(self):
        self.view_conexoes.atualizar()
        self.view_trechos.atualizar()
        self.view_grafo.atualizar()
