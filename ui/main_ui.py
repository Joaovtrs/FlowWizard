from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from .main_menu import MainMenu
from .main_menu_bar import MainMenuBar
from .viewer import Viewer


class MainUI(QMainWindow):
    def __init__(self, system, parent=None):
        super().__init__(parent)

        self.resize(800, 600)
        self.setWindowTitle('FlowWizard')
        self.setMinimumSize(800, 600)

        self.menu_bar = MainMenuBar(self.atualizar, self)
        self.setMenuBar(self.menu_bar)

        self.system = system

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.viewer = Viewer(self.atualizar, self.main_widget)
        self.menu = MainMenu(self.viewer, self.main_widget)

        self.main_grid.addWidget(self.menu)
        self.main_grid.addWidget(self.viewer)

    def atualizar(self):
        pass