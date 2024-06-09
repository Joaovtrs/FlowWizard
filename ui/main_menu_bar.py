import os

from PySide6.QtWidgets import QFileDialog, QMenuBar, QMessageBox

from system import system

desktop = os.path.join(
    os.path.join(os.environ['USERPROFILE']),
    'OneDrive\\Área de Trabalho'
    )


class MainMenuBar(QMenuBar):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.file = self.addMenu('Arquivo')

        self.new_file = self.file.addAction('Novo projeto')
        self.new_file.setShortcut('Ctrl+N')

        self.open_file = self.file.addAction('Abrir projeto')
        self.open_file.setShortcut('Ctrl+O')

        self.file.addSeparator()

        self.save_file = self.file.addAction('Salvar projeto')
        self.save_file.setShortcut('Ctrl+S')

        self.save_as_file = self.file.addAction('Salvar projeto como')
        self.save_as_file.setShortcut('Ctrl+Shift+S')

        self.new_file.triggered.connect(self.func_new_file)
        self.open_file.triggered.connect(self.func_open_file)
        self.save_file.triggered.connect(self.func_save_file)
        self.save_as_file.triggered.connect(self.func_save_as_file)

    def update_(self):
        pass

    def pop_up(self, texto):
        pop_up_excluir = QMessageBox(self)
        pop_up_excluir.setWindowTitle('Aviso')
        pop_up_excluir.setText(texto)
        pop_up_excluir.setInformativeText(
            'Todas as alterações não salvas serão perdidas'
        )
        pop_up_excluir.setIcon(QMessageBox.Warning)
        pop_up_excluir.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        pop_up_excluir.setButtonText(QMessageBox.No, 'Não')
        pop_up_excluir.setButtonText(QMessageBox.Yes, 'Sim')
        pop_up_excluir.setDefaultButton(QMessageBox.No)

        return pop_up_excluir.exec()

    def func_new_file(self):
        resp = self.pop_up('Deseja criar um novo arquivo?')

        if resp == QMessageBox.Yes:
            system.new()
            self.func_update()

    def func_open_file(self):
        resp = self.pop_up('Deseja abrir outro arquivo?')

        if resp == QMessageBox.Yes:
            path = QFileDialog.getOpenFileName(
                parent=self,
                caption='Abrir',
                filter='*.fww',
                dir=desktop
            )

            if path[0]:
                system.open(path[0])
                self.func_update()

    def func_save_file(self):
        if system.path is not None:
            system.save()
            self.func_update()
        else:
            self.func_save_as_file()

    def func_save_as_file(self):
        path = QFileDialog.getSaveFileName(
            parent=self,
            caption='Salvar como',
            filter='*.fww',
            dir=desktop
        )

        if path[0]:
            system.save_as(path[0])
            self.func_update()
