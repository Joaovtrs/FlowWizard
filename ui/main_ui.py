from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from system import system

from .main_menu import MainMenu
from .main_menu_bar import MainMenuBar
from .viewer import Viewer


class MainUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(800, 600)
        self.setWindowTitle('FlowWizard')
        self.setMinimumSize(800, 600)
        self.showMaximized()

        self.menu_bar = MainMenuBar(self.update_, self)
        self.setMenuBar(self.menu_bar)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.viewer = Viewer(self.update_, self.main_widget)
        self.menu = MainMenu(self.viewer, self.main_widget)

        self.main_grid.addWidget(self.menu)
        self.main_grid.addWidget(self.viewer)

    def update_(self):
        if system.path is not None:
            arq = str(system.path).split('/')[-1]
            self.setWindowTitle('FlowWizard: ' + str(arq))
        else:
            self.setWindowTitle('FlowWizard')

        self.menu_bar.update_()
        self.viewer.update_()
