from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from .plot_ui import PlotUI


class MainUI(QMainWindow):
    def __init__(self, system, parent=None):
        super().__init__(parent)

        self.resize(800, 600)
        self.setWindowTitle('FlowWizard')
        self.setMinimumSize(800, 600)

        self.system = system

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.plot_ui = PlotUI(self.main_widget)

        self.main_grid.addWidget(self.plot_ui)
