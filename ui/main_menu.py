from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout

from .main_menu_buttons import MainManuButton


class MainMenu(QFrame):
    def __init__(self, viewer, parent=None):
        super().__init__(parent)

        self.viewer = viewer

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(80)
        self.setMaximumWidth(80)

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.btn_menu = MainManuButton(' Menu', 'icons/menu.png', self)

        self.separator = QFrame(self)
        self.separator.setFrameShape(QFrame.HLine)

        self.btn_nodes = MainManuButton(
            ' Conexões', 'icons/menu-dots.png', self
        )
        self.btn_pipes = MainManuButton(
            ' Trechos', 'icons/algorithm.png', self
        )
        self.btn_graph = MainManuButton(' Grafo', 'icons/connection.png', self)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.grid.addWidget(self.btn_menu)
        self.grid.addWidget(self.separator)
        self.grid.addWidget(self.btn_nodes)
        self.grid.addWidget(self.btn_pipes)
        self.grid.addWidget(self.btn_graph)
        self.grid.addItem(self.spacer)

        self.btn_menu.clicked.connect(self.func_btn_menu)
        self.btn_nodes.clicked.connect(
            lambda: self.viewer.setCurrentWidget(self.viewer.view_nodes)
        )
        self.btn_pipes.clicked.connect(
            lambda: self.viewer.setCurrentWidget(self.viewer.view_pipes)
        )
        self.btn_graph.clicked.connect(
            lambda: self.viewer.setCurrentWidget(self.viewer.view_graph)
        )

    def func_btn_menu(self):

        anim_max = QPropertyAnimation(self, b'maximumWidth', self)
        anim_min = QPropertyAnimation(self, b'minimumWidth', self)
        anim_max.setDuration(100)
        anim_min.setDuration(100)

        if self.width() == 80:
            anim_max.setStartValue(80)
            anim_min.setStartValue(80)
            anim_max.setEndValue(200)
            anim_min.setEndValue(200)
            anim_max.start()
            anim_min.start()
        elif self.width() == 200:
            anim_max.setStartValue(200)
            anim_min.setStartValue(200)
            anim_max.setEndValue(80)
            anim_min.setEndValue(80)
            anim_max.start()
            anim_min.start()
