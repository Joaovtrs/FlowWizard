from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from system import system


def configure_button(btn):
    btn.setMinimumSize(150, 30)
    btn.setMaximumSize(150, 30)
    btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class ViewNodes(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_title = QLabel('Conexões')
        self.lbl_title.setAlignment(Qt.AlignHCenter)
        self.lbl_title.setFont(QFont('Times', 20))

        self.separator_title = QFrame(self)
        self.separator_title.setFrameShape(QFrame.HLine)

        self.table_widget = QWidget(self)
        self.grid_2 = QHBoxLayout(self.table_widget)
        self.grid_2.setContentsMargins(0, 0, 0, 0)

        self.nodes_table = NodesTable(self.func_update, self)

        self.options_widget = OptionsWidget(self.func_update, self)

        self.grid_2.addWidget(self.nodes_table)
        self.grid_2.addWidget(self.options_widget)

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.separator_title)
        self.grid.addWidget(self.table_widget)

    def update_(self):
        self.nodes_table.update_()
        self.options_widget.update_()


class NodesTable(QTableWidget):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setVisible(False)

        self.update_()

    def update_(self):
        self.clear()

        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(
            [
                'Nome',
                'Cota (m)',
                'Pressão (m.c.a.)',
                'Número de Conexões',
                'Trechos Conectados',
            ]
        )
        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 250)
        self.setColumnWidth(2, 250)
        self.setColumnWidth(3, 250)
        self.setColumnWidth(4, 250)

        self.setRowCount(len(system.circuit.nodes))
        for i, node in enumerate(system.circuit.nodes):
            self.add_item(i, 0, str(node.name))
            self.add_item(i, 1, str(node.elevation))
            self.add_item(i, 2, str(node.pressure))
            self.add_item(i, 3, str(node.n_connections))
            self.add_item(i, 4, '')

    def add_item(self, col, line, item):
        item = QTableWidgetItem(item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setItem(col, line, item)


class OptionsWidget(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setFrameShape(QFrame.Panel)
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)

        self.grid = QGridLayout(self)

        self.lbl_title = QLabel('Configurações')
        self.lbl_title.setAlignment(Qt.AlignLeft)
        self.lbl_title.setFont(QFont('Times', 15))

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.btn_add = QPushButton('Adicionar conexão', self)
        configure_button(self.btn_add)

        self.btn_remove = QPushButton('Excluir conexão', self)
        configure_button(self.btn_remove)

        self.btn_save = QPushButton('Salvar Alterações', self)
        configure_button(self.btn_save)

        self.grid.addWidget(self.lbl_title, 0, 0)
        self.grid.addItem(self.spacer, 6, 0)
        self.grid.addWidget(self.btn_add, 7, 0)
        self.grid.addWidget(self.btn_remove, 7, 1)
        self.grid.addWidget(self.btn_save, 7, 2)

        self.btn_add.clicked.connect(self.add_func)

    def update_(self):
        pass

    def add_func(self):
        system.circuit.add_node()
        self.func_update()
