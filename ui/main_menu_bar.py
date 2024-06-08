from PySide6.QtWidgets import QMenuBar


class MainMenuBar(QMenuBar):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.addMenu('Arquivo')

    def update_(self):
        pass
