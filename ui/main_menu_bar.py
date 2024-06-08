import os

from PySide6.QtWidgets import QFileDialog, QMenuBar, QMessageBox


class MainMenuBar(QMenuBar):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.addMenu('Arquivo')

    def atualizar(self):
        pass
